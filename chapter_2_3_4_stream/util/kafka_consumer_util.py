import signal
import sys

from kafka import KafkaConsumer
from kafka.structs import TopicPartition
from chapter_2_3_4_stream.util import logging_util
from chapter_2_3_4_stream.config import project_config as conf

logger = logging_util.init_logger('kafka_consumer')


class Consumer(object):
    """
    Kafka Consumer
    """
    def __init__(self, bootstrap_server=None, group_id=conf.kafka_group_id, partitions=None, **kwargs):
        """
        Initialize the kafka consumer;
        1. Set the default kafka topic, node address, consumer group id (use the default value if not passed in)
        2. When you need to set specific parameters, you can directly pass them in kwargs, unpack them and pass them into the original function;
        3. Manually set the offset
        :param topic: Kafka consumer topic
        :param bootstrap_server: Kafka consumer address
        :param group_id: The consumer group id of kafka, the default is start_task, which is mainly the consumer who receives and starts the task_log, and there is only one consumer group id;
        :param partitions: Consumed partitions. When partitions are not used, the default read is all partitions.
        :param kwargs: Other native Kafka consumer parameters
        """

        if bootstrap_server is None:
            bootstrap_server = [conf.kafka_server]  # If the kafka cluster is used, write multiple
        self.consumer = KafkaConsumer(bootstrap_servers=bootstrap_server)

        is_exists = self.is_topic_exists(conf.kafka_topic)
        if not is_exists:
            logger.error("The topic does not exist, please contact the administrator")
            exit("The topic does not exist, please contact the administrator")

        if partitions is not None:
            self.consumer = KafkaConsumer(
                bootstrap_servers=bootstrap_server,
                group_id=group_id,
                # urrently there is only one consumer, and it needs to be modified depending on the situation;
                # when multiple consumers are expanded, it needs to be expanded;
                **kwargs
            )
            # Creating a TopicPartition Object
            self.topic_set = TopicPartition(conf.kafka_topic, int(partitions))
            # Assigning a specific partition
            self.consumer.assign([self.topic_set])
        else:
            # By default, all partitions under the topic are read,
            # but this operation does not support custom offsets because the offset must be in the specified partition;
            self.consumer = KafkaConsumer(
                conf.kafka_topic,
                bootstrap_servers=bootstrap_server,
                group_id=group_id,
                **kwargs
            )

    def is_topic_exists(self, topic):
        """
        Check if the topic in kafka exists;
        :param topic:
        :return: True means existence, False means non-existence;
        """
        topics_set = set(self.consumer.topics())
        if topic not in topics_set:
            return False
        return True

    def recv(self):
        """
        Receiving data in consumption
        :return:
        """
        try:
            for message in self.consumer:
                # This is a permanent blocking process.
                # The producer message will be cached in the message queue and will not be deleted,
                # so each message will have an offset in the message queue.
                yield {"topic": message.topic, "partition": message.partition, "key": message.key,
                       "value": message.value.decode(conf.kafka_encode)}
        except Exception as e:
            logger.error(f"error is: {e}")
        finally:
            self.consumer.close()

    def recv_seek(self, offset):
        """
        Receive data from the consumer and consume it at the specified offset
        :param offset: The consumer position specified in the consumer
        :return: Producer of consumer messages
        """
        try:
            #Set the consumer to a specific offset
            self.consumer.seek(self.topic_set, offset)
            for message in self.consumer:
                yield {"topic": message.topic, "partition": message.partition, "key": message.key,
                       "value": message.value.decode(conf.kafka_encode)}
        except Exception as e:
            logger.error(f"error is: {e}")
        finally:
            self.consumer.close()

    def signal_handler(self, sig, frame):
        """
        Define the signal processing function
        :param sig:
        :param frame:
        :return:
        """
        logger.error('gracefully stopping consumer...')
        self.consumer.close()  # 关闭消费者
        sys.exit(0)

    # Register a signal handler to capture SIGINT (Ctrl+C) and SIGTERM
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


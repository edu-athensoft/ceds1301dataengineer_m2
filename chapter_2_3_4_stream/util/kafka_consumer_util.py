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
    def __init__(self, bootstrap_server=None,
                 group_id=conf.kafka_group_id):
        """
        Initialize the kafka consumer;
        :param bootstrap_server: Kafka consumer address
        :param group_id: The consumer group id of kafka, the default is start_task, which is mainly the consumer who receives and starts the task_log, and there is only one consumer group id;
        """

        if bootstrap_server is None:
            bootstrap_server = [conf.kafka_server]  # If the kafka cluster is used, write multiple
        self.consumer = KafkaConsumer(bootstrap_servers=bootstrap_server)

        is_exists = self.is_topic_exists(conf.kafka_topic)
        if not is_exists:
            logger.error("The topic does not exist, please contact the administrator")
            exit("The topic does not exist, please contact the administrator")

        self.consumer = KafkaConsumer(
                conf.kafka_topic,
                bootstrap_servers=bootstrap_server,
                group_id=group_id
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

    def signal_handler(self, sig, frame):
        """
        Define the signal processing function
        :param sig:
        :param frame:
        :return:
        """
        logger.error('gracefully stopping consumer...')
        self.consumer.close()
        sys.exit(0)

    # Register a signal handler to capture SIGINT (Ctrl+C) and SIGTERM
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


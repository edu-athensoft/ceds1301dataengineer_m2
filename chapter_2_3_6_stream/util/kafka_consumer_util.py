import json
import signal
import sys

from kafka import KafkaConsumer, KafkaProducer
from kafka.structs import TopicPartition
from chapter_2_3_6_stream.util import logging_util

logger = logging_util.init_logger('kafka_consumer')


class KConsumer(object):
    """
    Kafka Consumer
    """

    _server = "localhost:9092"
    _encode = "UTF-8"

    def __init__(self, topics="test_topic", bootstrap_server=None, group_id="start_task", partitions=None, **kwargs):
        """
        Initialize the kafka consumer;
        1. Set the default kafka topic, node address, consumer group id (use the default value if not passed in)
        2. When you need to set specific parameters, you can directly pass them in kwargs, unpack them and pass them into the original function;
        3. Manually set the offset
        :param topics: Kafka consumer topics
        :param bootstrap_server: Kafka consumer address
        :param group_id: The consumer group id of kafka, the default is start_task, which is mainly the consumer who receives and starts the task, and there is only one consumer group id;
        :param partitions: Consumed partitions. When partitions are not used, the default read is all partitions.
        :param kwargs: Other native Kafka consumer parameters
        """

        if bootstrap_server is None:
            bootstrap_server = [self._server]  # If the kafka cluster is used, write multiple
        self.consumer = KafkaConsumer(bootstrap_servers=bootstrap_server)
        exist = self.exist_topics(topics)

        # The required topic does not exist, create one
        if not exist:
            self.create_topics(topics)
        if partitions is not None:
            self.consumer = KafkaConsumer(
                bootstrap_servers=bootstrap_server,
                group_id=group_id,
                # urrently there is only one consumer, and it needs to be modified depending on the situation;
                # when multiple consumers are expanded, it needs to be expanded;
                **kwargs
            )
            # print("指定分区信息:", partitions, topics, type(partitions))
            self.topic_set = TopicPartition(topics, int(partitions))
            self.consumer.assign([self.topic_set])
        else:
            # By default, all partitions under the topic are read,
            # but this operation does not support custom offsets because the offset must be in the specified partition;
            self.consumer = KafkaConsumer(
                topics,
                bootstrap_servers=bootstrap_server,
                group_id=group_id,
                **kwargs
            )

    def exist_topics(self, topics):
        """
        Check if the topic in kafka exists;
        :param topics:
        :return: True means existence, False means non-existence;
        """
        topics_set = set(self.consumer.topics())
        if topics not in topics_set:
            return False
        return True

    def create_topics(self, topics):
        """
        Create relevant kafka topic information
        :param topics:
        :return:
        """
        producer = KafkaProducer(
            bootstrap_servers=self._server,
            key_serializer=lambda k: json.dumps(k).encode('utf-8'),
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        producer.send(topics, key="start", value={"msg": "aaaa"})
        producer.close()

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
                       "value": message.value.decode(self._encode)}
        except Exception as e:
            logger.error(f"Error occurred: {e}")
        finally:
            self.consumer.close()

    def recv_seek(self, offset):
        """
        Receive data from the consumer and consume it at the specified offset
        :param offset: The consumer position specified in the consumer
        :return: Producer of consumer messages
        """
        try:
            self.consumer.seek(self.topic_set, offset)
            for message in self.consumer:
                yield {"topic": message.topic, "partition": message.partition, "key": message.key,
                       "value": message.value.decode(self._encode)}
        except Exception as e:
            logger.error(f"Error occurred: {e}")
        finally:
            self.consumer.close()

    # 定义信号处理函数
    def signal_handler(self, sig, frame):
        """
        Define the signal processing function
        :param sig:
        :param frame:
        :return:
        """
        print('Gracefully stopping consumer...')
        self.consumer.close()  # 关闭消费者
        sys.exit(0)

    # 绑定信号处理函数到 SIGINT 和 SIGTERM
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


if __name__ == '__main__':
    obj = KConsumer()
    for i in obj.recv():
        print(i)
        print(i["value"])

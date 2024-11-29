import kafka

from chapter_2_3_4_stream.util import logging_util
from chapter_2_3_4_stream.config import project_config as conf

logger = logging_util.init_logger('kafka_producer')


class Producer(object):
    """
    Kafka producer
    """

    def __init__(self):
        """
        Initialize and set the kafka producer connection object;
        if the parameter does not exist, use the default connection in the configuration file;
        """
        # Instantiate the producer object
        self.producer = kafka.KafkaProducer(
            bootstrap_servers=conf.kafka_server
        )

    def send(self, message: bytes, partition: int = 0):
        """
        Send a message
        :param message: Byte stream data, encode the string into UTF-8 format
        :param partition: Kafka partition, send the message to the specified partition
        :return:
        """
        future = self.producer.send(conf.kafka_topic, message, partition=partition)
        record_metadata = future.get(timeout=30)
        if future.failed():
            logger.error(f"error is: {future.exception}")

    def close(self):
        """
        Close the kafka connection
        :return:
        """
        self.producer.close()


if __name__ == '__main__':
    kafka_obj = Producer()
    kafka_obj.send("abc".encode())

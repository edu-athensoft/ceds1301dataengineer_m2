import kafka
from chapter_2_3_4_stream.util import logging_util

logger = logging_util.init_logger('kafka_producer')


class Producer(object):
    """
    Kafka producer
    """
    _topic = "test_topic"
    _server = "localhost:9092"
    _encode = "UTF-8"

    def __init__(self,
                 max_request_size=104857600, # config setting specifies the maximum size (in bytes) of a request that the server will accept
                 batch_size=0,  # Instant sending, increasing concurrency can be increased appropriately, but it will cause message delays;
                 **kwargs):
        """
        Initialize and set the kafka producer connection object;
        if the parameter does not exist, use the default connection in the configuration file;
        """
        # self.broker = self._server
        # self.topic = self._topic
        self.max_request_size = max_request_size

        # Instantiate the producer object
        self.producer = kafka.KafkaProducer(
            bootstrap_servers=self._server,
            max_request_size=self.max_request_size,
            batch_size=batch_size,
            **kwargs
        )

    def send(self, message: bytes, partition: int = 0):
        """
        Send a message
        :param message: Byte stream data, encode the string into UTF-8 format
        :param partition: Kafka partition, send the message to the specified partition
        :return:
        """
        future = self.producer.send(self._topic, message, partition=partition)
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
    print(kafka_obj.broker)
    kafka_obj.send("abc".encode())

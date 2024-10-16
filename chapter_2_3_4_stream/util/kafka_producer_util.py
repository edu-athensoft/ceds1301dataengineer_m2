import json
import kafka


class Producer(object):
    """
    Kafka producer model
    """
    _coding = "utf-8"

    def __init__(self,
                 broker='localhost:9092',
                 topic="test_topic",
                 max_request_size=104857600,
                 batch_size=0,  # 即时发送,提高并发可以适当增加,但是会造成消息的延迟;
                 **kwargs):
        """
        Initialize and set the kafka producer connection object;
        if the parameter does not exist, use the default connection in the configuration file;
        """
        self.broker = broker
        self.topic = topic
        self.max_request_size = max_request_size

        # Instantiate the producer object
        self.producer_json = kafka.KafkaProducer(
            bootstrap_servers=self.broker,
            max_request_size=self.max_request_size,
            batch_size=batch_size,
            key_serializer=lambda k: json.dumps(k).encode(self._coding),  # Set the key format to use an anonymous function to convert
            value_serializer=lambda v: json.dumps(v).encode(self._coding),  # When you need to use json transmission, you must add these two parameters
            **kwargs
        )

        self.producer = kafka.KafkaProducer(
            bootstrap_servers=broker,
            max_request_size=self.max_request_size,
            batch_size=batch_size,
            api_version=(0, 10, 1),
            **kwargs
        )

    def send(self, message: bytes, partition: int = 0):
        """
        Send a message
        :param message: Byte stream data, encode the string into UTF-8 format
        :param partition: Kafka partition, send the message to the specified partition
        :return:
        """
        future = self.producer.send(self.topic, message, partition=partition)
        record_metadata = future.get(timeout=30)
        if future.failed():
            raise Exception("send message failed:%s)" % future.exception)

    def send_json(self, key: str, value: dict, partition: int = 0):
        """
        Send data in json format
        :param key: The value of the key in kafka
        :param value: Specific message sent
        :param partition: Partition information
        :return:
        """
        future = self.producer_json.send(self.topic, key=key, value=value, partition=partition)
        record_metadata = future.get(timeout=30)
        if future.failed():  # 发送失败记录异常;
            raise Exception("send json message failed:%s)" % future.exception)

    def close(self):
        """
        Close the kafka connection
        :return:
        """
        self.producer_json.close()
        self.producer.close()


if __name__ == '__main__':
    kafka_obj = Producer()
    print(kafka_obj.broker)
    kafka_obj.send("abc".encode())

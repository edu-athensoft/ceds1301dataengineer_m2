"""
A simulated data generator for backend services to write logs
"""
import datetime
import random
import time
from chapter_2_3_1_log.util import logging_util
from chapter_2_3_4_stream.util import kafka_producer_util

logger = logging_util.init_logger('logs_generate')

generate_files = 1  # How many files are generated in one run
single_log_lines = 5  # How many lines of data does a logs file generate

log_level_array = ['WARN', 'INFO', 'ERROR']

file_name_array = ['barcode_service.py', 'orders_service.py', 'shop_manager.py',
                   'user_manager.py', 'goods_manager.py', 'base_network.py', 'event.py']

visitor_areas_array = {
    'California': ['Los Angeles', 'San Francisco', 'San Diego', 'Oakland'],
    'Texas': ['Houston', 'San Antonio', 'Dallas', 'Austin'],
    'Arizona': ['Phoenix', 'Tucson'],
    'Illinois': ['Chicago', 'Aurora'],
    'New York': ['New York City', 'Buffalo']
}

visitor_state_array = ['California', 'Texas', 'Arizona', 'Illinois', 'New York']


def get_log_str():
    """
    Generate log
    :return:
    """
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    log_level = random.choice(log_level_array)
    file_name = random.choice(file_name_array)
    response_time = random.randint(1, 9999)
    state = random.choice(visitor_state_array)
    city = random.choice(visitor_areas_array[state])
    log_str = f"{date_str}\t[{log_level}]\t{file_name}\tresponse time:{response_time}ms\t{state}\t{city}\t" \
              f"log info......"
    return log_str


kafka_producer = kafka_producer_util.Producer()

for i in range(0, generate_files):
    for j in range(single_log_lines):
        log_str = get_log_str()
        logger.info(f"log is: {log_str}")
        kafka_producer.send(log_str.encode())

    time.sleep(1)

kafka_producer.close()

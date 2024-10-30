"""
A simulated data generator for backend services to write logs
"""
import datetime
import random
import time
from chapter_2_3_1_log.config import project_config as conf
from chapter_2_3_1_log.util import logging_util

logger = logging_util.init_logger('logs_generate')

generate_files = 1  # How many files are generated in one run
single_log_lines = 5  # How many lines of data does a logs file generate

output_path = conf.logs_monitor_path
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


for i in range(0, generate_files):
    write_file_path = f'{output_path}{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log'
    with open(write_file_path, 'w', encoding="UTF-8") as f:
        for j in range(single_log_lines):
            log_str = get_log_str()

            f.write(log_str)
            f.write("\n")

    logger.info(f"The writing of the {i + 1}th file is completed, the file is: {write_file_path}, the number of lines: {single_log_lines}")

    time.sleep(1)

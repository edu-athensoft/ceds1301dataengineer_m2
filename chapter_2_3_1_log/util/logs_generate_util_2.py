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

backend_files_name = ['barcode_service.py', 'orders_service.py', 'shop_manager.py',
                      'user_manager.py', 'goods_manager.py', 'base_network.py', 'event.py']

visitor_areas = {
    'California': ['Los Angeles', 'San Francisco', 'San Diego', 'Oakland'],
    'Texas': ['Houston', 'San Antonio', 'Dallas', 'Austin'],
    'Arizona': ['Phoenix', 'Tucson'],
    'Illinois': ['Chicago', 'Aurora'],
    'New York': ['New York City', 'Buffalo']
}
visitor_state = ['California', 'Texas', 'Arizona', 'Illinois', 'New York']

# weight 30:1 as [1] * 30 + [0]
response_flag = [1, 0]

# weight 5:1 as [1] * 5 + [0]
response_for_error_flag = [1, 0]



def get_log_str():
    """
    Generate log
    :return:
    """
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    log_level = random.choice(log_level_array)
    file_name = random.choice(backend_files_name)
    if not log_level == "ERROR":
        result_response_flag = random.choices(response_flag, weights=[30, 1], k=1)[0]
        if result_response_flag == 1:
            response_time = random.randint(0, 1000)
        else:
            response_time = random.randint(1000, 9999)
    else:
        result_response_for_error_flag = random.choices(response_for_error_flag, weights=[5, 1], k=1)[0]
        if result_response_for_error_flag == 1:
            response_time = random.randint(0, 1000)
        else:
            response_time = random.randint(1000, 9999)
    province = visitor_province[random.randint(0, len(visitor_province) - 1)]
    city = visitor_areas[province][random.randint(0, len(visitor_areas[province]) - 1)]
    log_str = f"{date_str}\t[{log_level}]\t{file_name}\tresponse time:{response_time}ms\t{province}\t{city}\t" \
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

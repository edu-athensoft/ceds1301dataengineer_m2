"""
A simulated data generator for backend services to write logs
"""
import datetime
import random
import time
from chapter_2_3_4_stream.config import project_config as conf
from chapter_2_3_4_stream.util import kafka_producer_util
from chapter_2_3_4_stream.util import logging_util

logger = logging_util.init_logger('logs_generate')

generate_files = 1  # How many files are generated in one run
single_log_lines = 10  # How many lines of data does a logs file generate

output_path = conf.logs_monitor_path
log_level_array = ['WARN', 'WARN', 'WARN', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO',
                   'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO',
                   'ERROR']

backend_files_name = ['barcode_service.py', 'barcode_service.py', 'barcode_service.py',
                      'orders_service.py', 'orders_service.py', 'orders_service.py', 'orders_service.py',
                      'orders_service.py', 'orders_service.py',
                      'shop_manager.py', 'shop_manager.py',
                      'user_manager.py', 'user_manager.py', 'user_manager.py',
                      'goods_manager.py', 'goods_manager.py', 'goods_manager.py', 'goods_manager.py',
                      'goods_manager.py', 'goods_manager.py',
                      'base_network.py', 'base_network.py',
                      'event.py', 'event.py', 'event.py', 'event.py', 'event.py', 'event.py', 'event.py']

visitor_areas = {
    '北京市': ['海淀区', '大兴区', '丰台区', '朝阳区', '昌平区', '海淀区', '怀柔区'],
    '上海市': ['静安区', '黄浦区', '徐汇区', '普陀区', '杨浦区', '宝山区', '浦东新区', '浦东新区'],
    '重庆市': ['万州区', '万州区', '涪陵区', '渝中区', '沙坪坝区', '九龙坡区', '南岸区'],
    '江苏省': ['南京市', '南京市', '南京市', '苏州市', '苏州市', '无锡市', '常州市', '宿迁市', '张家港市'],
    '安徽省': ['阜阳市', '阜阳市', '六安市', '合肥市', '合肥市', '合肥市', '池州市', '铜陵市', '芜湖市'],
    '山东省': ['济南市', '济南市', '青岛市', '青岛市', '青岛市', '菏泽市'],
    '湖北省': ['武汉市', '武汉市', '武汉市', '十堰市', '荆州市', '恩施土家族苗族自治州'],
    '广东省': ['广州市', '广州市', '广州市', '深圳市', '深圳市', '深圳市', '珠海市'],
    '天津市': ['和平区', '河东区', '河西区', '武清区', '宝坻区'],
    '湖南省': ['长沙市', '长沙市', '长沙市', '长沙市', '长沙市', '长沙市', '长沙市', '株洲市', '张家界市', '常德市', '益阳市'],
    '浙江省': ['杭州市', '杭州市', '湖州市', '绍兴市', '舟山市', '金华市', '嘉兴市', '丽水市']
}
visitor_province = ['北京市', '上海市', '重庆市', '江苏省', '安徽省', '山东省', '湖北省', '广东省', '天津市', '湖南省', '浙江省']

response_flag = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
response_for_error_flag = [1, 1, 1, 1, 1, 0]


def get_log_str():
    """
    Generate log
    :return:
    """
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    log_level = log_level_array[random.randint(0, len(log_level_array) - 1)]
    file_name = backend_files_name[random.randint(0, len(backend_files_name) - 1)]
    if not log_level == "ERROR":
        if response_flag[random.randint(0, len(response_flag) - 1)] == 1:
            response_time = random.randint(0, 1000)
        else:
            response_time = random.randint(1000, 9999)
    else:
        if response_for_error_flag[random.randint(0, len(response_for_error_flag) - 1)] == 1:
            response_time = random.randint(0, 1000)
        else:
            response_time = random.randint(1000, 9999)
    province = visitor_province[random.randint(0, len(visitor_province) - 1)]
    city = visitor_areas[province][random.randint(0, len(visitor_areas[province]) - 1)]
    log_str = f"{date_str}\t[{log_level}]\t{file_name}\t响应时间:{response_time}ms\t{province}\t{city}\t" \
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

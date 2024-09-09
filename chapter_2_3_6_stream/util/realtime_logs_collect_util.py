from chapter_2_3_6_stream.config import project_config as conf
from chapter_2_3_6_stream.model.backend_logs_model import BackendLogsModel
from chapter_2_3_6_stream.util import kafka_consumer_util
from chapter_2_3_6_stream.util import logging_util
from chapter_2_3_6_stream.util import mysql_util

logger = logging_util.init_logger('logs_kafka_collect')
logger.info('Log collection started....')

# Collect data for new access log files to be collected
# Create a target database connection
target_util = mysql_util.get_mysql_util(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password
)
# Check if the target database exists, if not, create it
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_logs_table_name,
    tb_cols=conf.target_logs_table_create_cols
)

kafka_consumer = kafka_consumer_util.KConsumer()
for stream_data in kafka_consumer.recv():
    try:
        logger.info(stream_data["value"])
        backend_log_model = BackendLogsModel(stream_data["value"])
        target_util.insert_sql(backend_log_model.insert_sql())
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        continue  # Skip the problematic message and continue processing the next message


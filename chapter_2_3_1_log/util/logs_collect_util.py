import sys, os
import time

from chapter_2_3_1_log.util import mysql_util
from chapter_2_3_1_log.util import file_util
from chapter_2_3_1_log.util import logging_util
from chapter_2_3_1_log.config import project_config as conf
from chapter_2_3_1_log.model.logs_model import LogsModel

logger = logging_util.init_logger('logs_collect')
logger.info('Log collection started....')


# pyinstaller
def app_path():
    # Returns the base application path.
    if hasattr(sys, 'frozen'):
        # Handles PyInstaller
        return sys.executable  #使用pyinstaller打包后的exe目录
    return os.path.dirname(__file__)     #没打包前的py目录

pj_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(app_path()))))
logger.info(f"================Project dir is '{pj_path}'===============")

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS') or hasattr(sys, 'frozen'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

logger.info(f"================Project dir is '{resource_path(conf.logs_monitor_path)}'===============")

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

# Record collection start time
start_time = time.time()

# Get the log files under the background access log folder
all_file_list = file_util.get_dir_files_list(resource_path(conf.logs_monitor_path))

# Query the collected log files in the metadata database table to compare and determine whether to collect new access log files
# Creating a Metabase Connection
metadata_util = mysql_util.get_mysql_util(
    host=conf.metadata_host,
    port=conf.metadata_port,
    user=conf.metadata_user,
    password=conf.metadata_password
)
# Get the collected log files
processed_file_list = mysql_util.get_processed_files(
    util=metadata_util,
    db_name=conf.metadata_db,
    tb_name=conf.logs_monitor_meta_table_name,
    tb_cols=conf.logs_monitor_meta_table_create_cols
)
# Compare and determine the log files to be collected
new_file_list = file_util.get_new_by_compare_lists(processed_file_list, all_file_list)

# What are the new files for recording collection?
if not new_file_list:
    logger.info('Sorry, there is no logs to collect!')
    #exit('Sorry, there is no logs to collect!')
else:
    logger.info(f'The files to be collected are {new_file_list}')

# Traverse the log files to be collected
for file_path in new_file_list:
    # 事务1: 开启事务
    target_util.begin_transaction()
    row_total = 0
    try:
        for row_content in open(file_path, 'r', encoding='utf8'):
            backend_log_model = LogsModel(row_content)
            target_util.insert_sql_without_commit(backend_log_model.insert_sql())
            row_total += 1
    except Exception as e:
        target_util.rollback_transaction()

    # submit a transaction operation
    target_util.commit_transaction()

    # Record the access log files collected this time into the metadata database table
    sql = f'insert into {conf.logs_monitor_meta_table_name}(' \
          f'file_name, process_lines) values' \
          f'("{file_path}","{row_total}");'
    metadata_util.insert_sql(sql)

# Record end time
end_time = time.time()
logger.info(f'This collection collected {len(new_file_list)} files in total, and took {end_time-start_time}s')
# Close the database connection
target_util.close()
metadata_util.close()

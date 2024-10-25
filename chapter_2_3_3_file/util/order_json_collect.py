import os
import sys
import time

from chapter_2_3_3_file.config import project_config as conf
from chapter_2_3_3_file.model.orders_model import OrderModelParser
from chapter_2_3_3_file.util import file_util
from chapter_2_3_3_file.util import logging_util
from chapter_2_3_3_file.util import mysql_util

logger = logging_util.init_logger('json_collect')


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS') or hasattr(sys, 'frozen'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


logger.info(f"================Project dir is '{resource_path(conf.json_data_path)}'===============")

# Record collection start time
start_time = time.time()
# Get the order JSON files under the order folder
all_json_files = file_util.get_dir_files_list(resource_path(conf.json_data_path))

# Query the order JSON files that have been collected in the metadata database table to compare
# and determine whether to collect new order JSON files

# Create a metadata connection
metadata_util = mysql_util.get_mysql_util(
    host=conf.metadata_host,
    user=conf.metadata_user,
    password=conf.metadata_password
)
# Check if the data table exists, if not, create it
metadata_util.check_table_exists_and_create(
    db_name=conf.metadata_db,
    tb_name=conf.orders_json_file_monitor_meta_table_name,
    tb_cols=conf.orders_json_file_monitor_meta_table_create_cols
)

# Get the list of Json file paths that have been collected in the metadata
# sql = f"select * from {conf.orders_json_file_monitor_meta_table_name}"
# processed_json_files_result = metadata_util.query(sql)  # ((1, 'x00'), (2, 'x01'), (3, 'x02'))

processed_json_files_result = mysql_util.get_processed_files(
    util=metadata_util,
    db_name=conf.metadata_db,
    tb_name=conf.orders_json_file_monitor_meta_table_name,
    tb_cols=conf.orders_json_file_monitor_meta_table_create_cols
)
processed_json_files_names = [i[1] for i in processed_json_files_result]
# Compare and determine the new order files to be collected
new_json_files = file_util.get_new_by_compare_lists(processed_json_files_names, all_json_files)

# Collect data for the new order JSON file to be collected
# Create a target database connection object
target_util = mysql_util.get_mysql_util(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password
)
# Check if the target data table exists, if not, create it
# Check order table
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_orders_table_name,
    tb_cols=conf.target_orders_table_create_cols
)
# Check the order details table
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_orders_detail_table_name,
    tb_cols=conf.target_orders_detail_table_create_cols
)

json_file_count = 0
# Iterate through the JSON files to be processed
for json_file in new_json_files:
    try:
        data_count = 0

        #  Read JSON file line by line and create data model
        for json_data in open(json_file, 'r', encoding='utf-8'):
            data_count += 1

            order_model = OrderModelParser(json_data)

            target_util.insert_sql(order_model.order_model.generate_order_insert_sql())
            target_util.insert_sql(order_model.order_detail_model.generate_order_details_insert_sql())

        json_file_count += 1
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        continue  # Skip the problematic message and continue processing the next message

    # Record the collected files in the metadata table
    json_file = json_file.replace('\\', '/')
    sql = f"insert into {conf.orders_json_file_monitor_meta_table_name}(file_name, process_lines) values (" \
          f"'{json_file}', {data_count});"
    metadata_util.insert_sql(sql)

    logger.info(f'{json_file} has been collected successfully!')

# Record end time
end_time = time.time()
logger.info(f'This collection collected {json_file_count} files in total, and took {end_time - start_time}s')

# Close the file and database connection
target_util.close()
metadata_util.close()

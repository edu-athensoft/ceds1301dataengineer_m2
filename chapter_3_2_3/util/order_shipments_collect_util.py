"""
order_shipments collection tools
"""
import time

from chapter_3_2_3.util import mysql_util
from chapter_3_2_3.util import logging_util
from chapter_3_2_3.model.order_shipments_model import OrderShipmentsModel
from chapter_3_2_3.config import project_config as conf

logger = logging_util.init_logger('order_shipments_db')
logger.info('order_shipments data collection starts...')

# - Create a metabase connection object
metadata_util = mysql_util.get_mysql_util(
    host=conf.metadata_host,
    user=conf.metadata_user,
    password=conf.metadata_password
)
# Check if the metadata table exists, if not, create it
metadata_util.check_table_exists_and_create(
    db_name=conf.metadata_db,
    tb_name=conf.metadata_order_shipments_table_name,
    tb_cols=conf.metadata_order_shipments_table_create_cols
)
# Query the maximum updateAt value of the last collected record in the order_shipments collection metadata table
sql = f"select max(time_record) from {conf.metadata_order_shipments_table_name}"
order_shipments_monitor_table_results = metadata_util.query(sql)

if order_shipments_monitor_table_results[0][0]:
    order_shipments_max_time = order_shipments_monitor_table_results[0][0]
else:
    order_shipments_max_time = None

# Create a data source database connection object
source_util = mysql_util.get_mysql_util(
    host=conf.source_host,
    user=conf.source_user,
    password=conf.source_password
)
# Determine whether the data source database exists
if not source_util.check_table_exists(conf.source_data_db, conf.source_order_shipments_table_name):
    logger.error('Sorry, the order_shipments source database table you want to access does not exist!')
    exit('Sorry, the order_shipments source database table you want to access does not exist!')

# Query the metadata database table to obtain the last collection time
# No maximum collection time (initial collection, full collection)
# There is a maximum acquisition time (re-acquisition, incremental acquisition)
if not order_shipments_max_time:
    sql = f"select * from {conf.source_order_shipments_table_name} order by shipment_date;"
else:
    sql = f"select * from {conf.source_order_shipments_table_name} where shipment_date > '{order_shipments_max_time}' order by shipment_date;"

source_order_shipments_table_results = source_util.query(sql)
# Determine the number of collected data entries. If the number of entries is 0, exit the program
if not source_order_shipments_table_results:
    logger.info('Sorry, there is no order_shipments data to collect!')
    exit('Sorry, there is no order_shipments data to collect!')


# Create a target database connection object
target_util = mysql_util.get_mysql_util(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password
)
# Check if the target database table exists, and create it if it does not exist
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_order_shipments_table_name,
    tb_cols=conf.target_order_shipments_table_create_cols
)


# Transaction processing function implementation
# 1. Open the transaction
# 2. Submit a transaction every 100 cycles (read 100 order_shipments data)
# 3. If the insertion fails, roll back the transaction
# 4. Define a data_count variable to record the number of order_shipments read
data_count = 0
# Manually start transaction operation
target_util.begin_transaction()

start = time.time()

for row_data in source_order_shipments_table_results:
    data_count += 1
    try:
        model = OrderShipmentsModel(row_data)
        target_util.insert_sql_without_commit(model.generate_insert_sql())
    except Exception as e:
        target_util.rollback_transaction()
        exit('Failed to insert data, roll back transaction!')

    # Is the number of order_shipments read a multiple of 100， Manually submit a transaction
    if data_count % 100 == 0:
        # Manually submit a transaction operation
        # Write the update_at time of each collected data into the metadata table
        target_util.commit_transaction()
        sql = f"insert into {conf.metadata_order_shipments_table_name}(time_record, gather_line_count) values (" \
              f"'{model.update_at}', 100);"
        metadata_util.insert_sql(sql)
        logger.info(f'{data_count} records have been collected successfully!')
        # It is convenient to reopen the transaction in advance to prepare for the next transaction processing
        target_util.begin_transaction()

# No matter how many data are left, manually submit a transaction
target_util.commit_transaction()

sql = f"insert into {conf.metadata_order_shipments_table_name}(time_record, gather_line_count) values (" \
      f"'{model.update_at}', {data_count % 100});"
metadata_util.insert_sql(sql)

end = time.time()
logger.info(f'This time, a total of {data_count} records were collected, and the total time consumed was {end-start}s')

# Close the database connection
target_util.close()
source_util.close()
metadata_util.close()

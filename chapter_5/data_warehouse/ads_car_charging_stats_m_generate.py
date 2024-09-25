"""
ads_car_charging_stats collection tools
"""
import time

from chapter_5.util import mysql_util
from chapter_5.util import logging_util
from chapter_5.model.ads_car_charging_model import CarChargingStatsModel
from chapter_5.config import project_config as conf

logger = logging_util.init_logger('ads_car_charging_stats')
logger.info('ads_car_charging_stats data collection starts...')

# Create a data source database connection object
source_util = mysql_util.get_mysql_util(
    host=conf.source_host,
    user=conf.source_user,
    password=conf.source_password
)
# Determine whether the data source database exists
if not source_util.check_table_exists(conf.source_data_db, conf.source_dws_car_charging_d_table_name):
    logger.error('Sorry, the product source database table you want to access does not exist!')
    exit('Sorry, the product source database table you want to access does not exist!')

source_car_charging_stats_table_results = source_util.query(conf.target_ads_car_charging_stats_table_select_sql)
# Determine the number of collected data entries. If the number of entries is 0, exit the program
if not source_car_charging_stats_table_results:
    logger.info('Sorry, there is no product data to collect!')
    #exit('Sorry, there is no product data to collect!')

# Create a target database connection object
target_util = mysql_util.get_mysql_util(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password
)
# Check if the target database table exists, and create it if it does not exist
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_ads_car_charging_stats_table_name,
    tb_cols=conf.target_ads_car_charging_stats_table_create_cols
)

source_util.query(conf.target_ads_car_charging_stats_table_delete_sql)

# Transaction processing function implementation
# 1. Open the transaction
# 2. Submit a transaction every 100 cycles (read 100 product data)
# 3. If the insertion fails, roll back the transaction
# 4. Define a data_count variable to record the number of products read
data_count = 0
# Manually start transaction operation
target_util.begin_transaction()

start = time.time()

model = None

for row_data in source_car_charging_stats_table_results:
    try:
        model = CarChargingStatsModel(row_data)
        target_util.insert_sql_without_commit(model.generate_insert_sql())
        data_count += 1
        # Is the number of products read a multiple of 100， Manually submit a transaction
        if data_count % conf.batch_commit == 0:
            # Manually submit a transaction operation
            # Write the update_at time of each collected data into the metadata table
            target_util.commit_transaction()
            logger.info(f'{data_count} records have been collected successfully!')
            # It is convenient to reopen the transaction in advance to prepare for the next transaction processing
            target_util.begin_transaction()
    except Exception as e:
        target_util.rollback_transaction()
        # exit('Failed to insert data, roll back transaction!')

if model == None or data_count == 0:
    pass
else:
    # No matter how many data are left, manually submit a transaction
    target_util.commit_transaction()

end = time.time()
logger.info(f'a total of {data_count} records were collected and the total time consumed was {end - start}s')

# Close the database connection
target_util.close()
source_util.close()

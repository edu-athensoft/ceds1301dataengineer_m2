from chapter_3_2_3.config import project_config as conf
from chapter_3_2_3.util import logging_util
from chapter_3_2_3.util import mysql_util

logger = logging_util.init_logger('dim_store_generate')
logger.info('dim_store_generate started....')


# Create a target database connection
target_util = mysql_util.get_mysql_util(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password
)
# Check if the target database exists, if not, create it
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_dim_store_table_name,
    tb_cols=conf.target_dim_store_table_create_cols
)

cursor = target_util.conn.cursor()

data = [
    (1, 'Store A', 1, '2020-01-01'),
    (2, 'Store B', 2, '2019-06-15'),
    (3, 'Store C', 3, '2018-03-10'),
    (4, 'Store D', 4, '2021-09-23'),
    (5, 'Store E', 5, '2022-11-30')
]

cursor.executemany('''
INSERT INTO dim_store (id, store_name, location_id, open_date) 
VALUES (%s, %s, %s, %s)
''', data)

target_util.conn.commit()

target_util.conn.close()

logger.info("Data inserted successfully into dim_store table")

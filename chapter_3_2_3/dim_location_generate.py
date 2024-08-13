from chapter_3_2_3.config import project_config as conf
from chapter_3_2_3.util import logging_util
from chapter_3_2_3.util import mysql_util

logger = logging_util.init_logger('dim_location_generate')
logger.info('dim_location_generate started....')


# Create a target database connection
target_util = mysql_util.get_mysql_util(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password
)
# Check if the target database exists, if not, create it
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_dim_location_table_name,
    tb_cols=conf.target_dim_location_table_create_cols
)

cursor = target_util.conn.cursor()

data = [
    (1, 'United States', 'New York', 'New York City', '10001', 6),
    (2, 'United States', 'California', 'Los Angeles', '90001', 4),
    (3, 'United States', 'Illinois', 'Chicago', '60601', -1),
    (4, 'United States', 'Texas', 'Houston', '77001', -1),
    (5, 'United States', 'Arizona', 'Phoenix', '85001', -1)
]

cursor.executemany('''
INSERT INTO dim_location (id, country, state, city, postal_code, region_key) 
VALUES (%s, %s, %s, %s, %s, %s)
''', data)


# Check if the target database exists, if not, create it
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_dim_region_table_name,
    tb_cols=conf.target_dim_region_table_create_cols
)

cursor = target_util.conn.cursor()

data = [
    (1, 'North America', 'Continent'),
    (2, 'United States', 'Country'),
    (3, 'California', 'State'),
    (4, 'Los Angeles', 'City'),
    (5, 'New York', 'State'),
    (6, 'New York City', 'City')
]

cursor.executemany('''
INSERT INTO dim_region (id, region_name, region_type) 
VALUES (%s, %s, %s)
''', data)

target_util.conn.commit()

target_util.conn.close()

logger.info("Data inserted successfully into dim_location table")

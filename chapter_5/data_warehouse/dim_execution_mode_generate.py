from chapter_5.config import project_config as conf
from chapter_5.util import logging_util
from chapter_5.util import mysql_util

logger = logging_util.init_logger('dim_execution_mode_generate')
logger.info('dim_execution_mode_generate started....')


# Create a target database connection
target_util = mysql_util.get_mysql_util(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password
)
# Check if the target database exists, if not, create it
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_dim_execution_mode_table_name,
    tb_cols=conf.target_dim_execution_mode_table_create_cols
)

cursor = target_util.conn.cursor()

data = [
    ('ELECTRICITY', 1),
    ('HYBRID', 2),
    ('FUEL', 3)
]

cursor.executemany('''
INSERT INTO dim_execution_mode (name, type) 
VALUES (%s, %s)
''', data)

target_util.conn.commit()

target_util.conn.close()

logger.info("Data inserted successfully into dim_execution_mode table")

"""
生成dim_time维度表
"""
from datetime import datetime, timedelta

from chapter_3_2_3.config import project_config as conf
from chapter_3_2_3.util import logging_util
from chapter_3_2_3.util import mysql_util

logger = logging_util.init_logger('dim_time_generate')
logger.info('dim_time_generate started....')


# Create a target database connection
target_util = mysql_util.get_mysql_util(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password
)
# Check if the target database exists, if not, create it
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_dim_time_table_name,
    tb_cols=conf.target_dim_time_table_create_cols
)

cursor = target_util.conn.cursor()

# Generate all dates from 2023 to 2024
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)
current_date = start_date

data = []
time_key = 1
while current_date <= end_date:
    year = current_date.year
    quarter = (current_date.month - 1) // 3 + 1
    month = current_date.month
    day = current_date.day
    day_of_week = current_date.strftime('%A')

    data.append((time_key, current_date.strftime('%Y-%m-%d'), year, quarter, month, day, day_of_week))

    current_date += timedelta(days=1)
    time_key += 1

# Insert data in batches
cursor.executemany('''
INSERT INTO dim_time (id, date, year, quarter, month, day, day_of_week) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
''', data)

# commit transaction
target_util.conn.commit()

# close connection
target_util.conn.close()

logger.info("Data inserted successfully into dim_time table")

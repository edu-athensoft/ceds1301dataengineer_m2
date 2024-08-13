
from chapter_3_2_3.config import project_config as conf
from chapter_3_2_3.util import logging_util
from chapter_3_2_3.util import mysql_util

logger = logging_util.init_logger('dim_user_generate')
logger.info('dim_user_generate started....')


# Create a target database connection
target_util = mysql_util.get_mysql_util(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password
)
# Check if the target database exists, if not, create it
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_dim_user_table_name,
    tb_cols=conf.target_dim_user_table_create_cols
)

cursor = target_util.conn.cursor()

data = [
    ('1', 'John Doe', 'Male', '1985-05-15', 'johndoe@example.com', '123-456-7890', '123 Elm St', 'New York', 'New York', 'United States', '10001', '2023-01-01', '2023-03-04', 0),
    ('2', 'Jane Smith', 'Female', '1990-07-20', 'janesmith@example.com', '234-567-8901', '456 Oak St', 'Los Angeles', 'California', 'United States', '90001', '2023-01-01', '9999-12-31', 1),
    ('3', 'Mike Johnson', 'Male', '1982-10-30', 'mikejohnson@example.com', '345-678-9012', '789 Pine St', 'Chicago', 'Illinois', 'United States', '60601', '2023-01-01', '9999-12-31', 1),
    ('4', 'Emily Davis', 'Female', '1995-12-05', 'emilydavis@example.com', '456-789-0123', '321 Maple St', 'Houston', 'Texas', 'United States', '77001', '2023-01-01', '9999-12-31', 1),
    ('5', 'David Wilson', 'Male', '1978-03-25', 'davidwilson@example.com', '567-890-1234', '654 Cedar St', 'Phoenix', 'Arizona', 'United States', '85001', '2023-01-01', '9999-12-31', 1),
    ('1', 'John Doe', 'Male', '1985-05-15', 'johndoe@example.com', '789-546-7890', '7659 Elm St', 'New York', 'New York', 'United States', '10001', '2023-03-05', '9999-12-31', 1)
]

cursor.executemany('''
INSERT INTO dim_user (user_id, user_name, gender, birth_date, email, phone_number, address, city, state, country, postal_code, start_date, end_date, status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
''', data)

target_util.conn.commit()

target_util.conn.close()

logger.info("Data inserted successfully into dim_user table")

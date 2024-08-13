from chapter_3_2_3.config import project_config as conf
from chapter_3_2_3.util import logging_util
from chapter_3_2_3.util import mysql_util

logger = logging_util.init_logger('dim_product_generate')
logger.info('dim_product_generate started....')


# Create a target database connection
target_util = mysql_util.get_mysql_util(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password
)
# Check if the target database exists, if not, create it
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_dim_product_table_name,
    tb_cols=conf.target_dim_product_table_create_cols
)

cursor = target_util.conn.cursor()

data = [
    (1, 'Apple iPhone 14', 'Smartphones', 'Apple', 'Apple Inc.', 799.00, 'Unit', False, '2023-09-01'),
    (2, 'Samsung Galaxy S22', 'Smartphones', 'Samsung', 'Samsung Electronics', 749.00, 'Unit', False, '2023-08-15'),
    (3, 'Sony WH-1000XM4', 'Headphones', 'Sony', 'Sony Corporation', 299.99, 'Unit', False, '2023-05-20'),
    (4, 'Dell XPS 13', 'Laptops', 'Dell', 'Dell Technologies', 999.99, 'Unit', False, '2023-07-10'),
    (5, 'Nike Air Max 270', 'Footwear', 'Nike', 'Nike Inc.', 150.00, 'Pair', False, '2023-03-25')
]

cursor.executemany('''
INSERT INTO dim_product (id, product_name, category, brand, supplier, unit_price, unit_of_measure, is_discontinued, launch_date) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
''', data)

target_util.conn.commit()

target_util.conn.close()

logger.info("Data inserted successfully into dim_product table")

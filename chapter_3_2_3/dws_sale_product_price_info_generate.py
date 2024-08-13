from chapter_3_2_3.config import project_config as conf
from chapter_3_2_3.util import logging_util
from chapter_3_2_3.util import mysql_util

logger = logging_util.init_logger('dws_sale_product_price_info_generate')
logger.info('dws_sale_product_price_info_generate started....')


# Create a target database connection
target_util = mysql_util.get_mysql_util(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password
)
# Check if the target database exists, if not, create it
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_dws_sale_product_price_info_table_name,
    tb_cols=conf.target_dws_sale_product_price_info_table_create_cols
)

cursor = target_util.conn.cursor()

cursor.execute('''
INSERT INTO dws_sale_product_price_info (date_ts, product_id, product_name, sale_price_count) 
SELECT  DATE_FORMAT(a.date_ts, '%Y-%m-%d') as date_ts,  b.id, b.product_name, sum(pay_price)
FROM dwd_sale_order_fact a, dim_product b 
WHERE a.product_id = b.id
GROUP BY DATE_FORMAT(a.date_ts, '%Y-%m-%d'), b.id, b.product_name
ORDER BY date_ts
''')

target_util.conn.commit()

target_util.conn.close()

logger.info("Data inserted successfully into dws_sale_product_price_info table")

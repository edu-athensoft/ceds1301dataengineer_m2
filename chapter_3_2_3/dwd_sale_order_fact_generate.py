from chapter_3_2_3.config import project_config as conf
from chapter_3_2_3.util import logging_util
from chapter_3_2_3.util import mysql_util

logger = logging_util.init_logger('dwd_sale_order_fact_generate')
logger.info('dwd_sale_order_fact_generate started....')


# Create a target database connection
target_util = mysql_util.get_mysql_util(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password
)
# Check if the target database exists, if not, create it
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_dwd_sale_order_fact_table_name,
    tb_cols=conf.target_dwd_sale_order_fact_table_create_cols
)

cursor = target_util.conn.cursor()

cursor.execute('''
INSERT INTO dwd_sale_order_fact (order_id, user_id, store_id, product_id, pay_price, pay_type, date_ts) 
SELECT  a.order_id, a.user_id, a.store_id, b.product_id, b.price_per, a.pay_type, a.date_ts
FROM ods_orders a, ods_orders_detail b 
WHERE a.order_id = b.order_id
''')

target_util.conn.commit()

target_util.conn.close()

logger.info("Data inserted successfully into dwd_sale_order_fact table")

from chapter_3_2_3.config import project_config as conf
from chapter_3_2_3.util import logging_util
from chapter_3_2_3.util import mysql_util

logger = logging_util.init_logger('dwd_sale_order_lifecycle_fact_generate')
logger.info('dwd_sale_order_lifecycle_fact_generate started....')


# Create a target database connection
target_util = mysql_util.get_mysql_util(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password
)
# Check if the target database exists, if not, create it
target_util.check_table_exists_and_create(
    db_name=conf.target_data_db,
    tb_name=conf.target_dwd_sale_order_lifecycle_fact_table_name,
    tb_cols=conf.target_dwd_sale_order_lifecycle_fact_table_create_cols
)

cursor = target_util.conn.cursor()

cursor.execute('''
INSERT INTO dwd_sale_order_lifecycle_fact (order_id, user_id, payments_date, shipments_date, completions_date, pay_total) 
SELECT a.order_id, a.user_id, b.update_at as payments_date, c.update_at as shipments_date, d.update_at as completions_date, a.pay_total
FROM ods_orders a, ods_order_payments b, ods_order_shipments c, ods_order_completions d
WHERE a.order_id = b.order_id
AND a.order_id = c.order_id
AND a.order_id = d.order_id
''')

target_util.conn.commit()

target_util.conn.close()

logger.info("Data inserted successfully into dwd_sale_order_lifecycle_fact table")

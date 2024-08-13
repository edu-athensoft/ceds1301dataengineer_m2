from chapter_3_2_3.util import str_util
from chapter_3_2_3.config import project_config as conf


class OrderShipmentsModel(object):
    """
    OrderShipments information model class
    contain: order_payments, order_shipments, order_completions
    """

    def __init__(self, data_tuple: tuple):
        """
        """
        self.id = data_tuple[0]
        self.order_id = data_tuple[1]
        self.update_at = str(data_tuple[2])

    def generate_insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        sql = f"REPLACE INTO {conf.target_order_shipments_table_name}(" \
              f"id,order_id,update_at) VALUES(" \
              f"'{self.id}', " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.order_id)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.update_at)} " \
              f")"

        return sql

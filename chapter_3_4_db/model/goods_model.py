from chapter_3_4_db.util import str_util
from chapter_3_4_db.config import project_config as conf


class GoodsModel(object):
    """
    goods information model class
    """

    def __init__(self, data_tuple: tuple):
        """
        Use the goods barcode library field information as attributes
        The data is sent to data_tuple as a tuple => ('123987002321',
            'machine', '', '', '', 'pcs',
            'null', 0.0000, 0.0000, '2024-09-19 13:32:53', '', 0, 'null', 'null')
        """
        self.code = data_tuple[0]
        self.name = str_util.clear_str(data_tuple[1])
        self.spec = str_util.clear_str(data_tuple[2])
        self.trademark = str_util.clear_str(data_tuple[3])
        self.addr = str_util.clear_str(data_tuple[4])
        self.units = str_util.clear_str(data_tuple[5])
        self.factory_name = str_util.clear_str(data_tuple[6])
        self.trade_price = data_tuple[7]
        self.retail_price = data_tuple[8]
        self.update_at = str(data_tuple[9])
        self.wholeunit = str_util.clear_str(data_tuple[10])
        self.wholenum = data_tuple[11]
        self.img = data_tuple[12]
        self.src = data_tuple[13]

    def generate_insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        sql = f"REPLACE INTO {conf.target_goods_table_name}(" \
              f"code,name,spec,trademark,addr,units,factory_name,trade_price," \
              f"retail_price,update_at,wholeunit,wholenum,img,src) VALUES(" \
              f"'{self.code}', " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.name)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.spec)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.trademark)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.addr)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.units)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.factory_name)}, " \
              f"{str_util.check_number_null_and_transform_to_sql_null(self.trade_price)}, " \
              f"{str_util.check_number_null_and_transform_to_sql_null(self.retail_price)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.update_at)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.wholeunit)}, " \
              f"{str_util.check_number_null_and_transform_to_sql_null(self.wholenum)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.img)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.src)}" \
              f")"

        return sql

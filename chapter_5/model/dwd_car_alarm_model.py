from chapter_5.util import str_util
from chapter_5.config import project_config as conf


class CarAlarmModel(object):
    """
    caralarm information model class
    """

    def __init__(self, data_tuple: tuple):
        """
        Use the caralarm library field information as attributes
        The data is sent to data_tuple as a tuple => ('123987002321',
            'machine', '', '', '', 'pcs',
            'null', 0.0000, 0.0000, '2024-09-19 13:32:53', '', 0, 'null', 'null')
        """
        self.vin = data_tuple[0]
        self.date_ts = data_tuple[1]
        self.alarm_level = data_tuple[2]
        self.alarm_sign = data_tuple[3]
        self.battery_alarm_count = data_tuple[4]
        self.battery_alarm_list = data_tuple[5]
        self.motor_alarm_count = data_tuple[6]
        self.motor_alarm_list = data_tuple[7]
        self.engine_alarm_count = data_tuple[8]
        self.engine_alarm_list = data_tuple[9]
        self.other_alarm_count = data_tuple[10]
        self.other_alarm_list = data_tuple[11]

    def generate_insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        sql = f"REPLACE INTO {conf.target_dwd_car_alarm_fact_table_name} {conf.target_dwd_car_alarm_fact_table_insert_cols}" \
              f"VALUES(" \
              f"'{self.vin}', " \
              f"'{self.date_ts}'," \
              f"{self.alarm_level}, " \
              f"{self.alarm_sign}, " \
              f"{self.battery_alarm_count}, " \
              f"'{self.battery_alarm_list}', " \
              f"{self.motor_alarm_count}, " \
              f"'{self.motor_alarm_list}', " \
              f"{self.engine_alarm_count}, " \
              f"'{self.engine_alarm_list}', " \
              f"{self.other_alarm_count}, " \
              f"'{self.other_alarm_list}' " \
              f")"

        return sql

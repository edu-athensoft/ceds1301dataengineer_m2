from chapter_5.config import project_config as conf


class CarAlarmStatsModel(object):
    """
    caralarmstats information model class
    """
    def __init__(self, data_tuple: tuple):
        """
        Use the caralarmstats library field information as attributes
        The data is sent to data_tuple as a tuple => ('123987002321',
            'machine', '', '', '', 'pcs',
            'null', 0.0000, 0.0000, '2024-09-19 13:32:53', '', 0, 'null', 'null')
        """
        self.time_window = data_tuple[0]
        self.date_ts = data_tuple[1]
        self.total_alarm_count = data_tuple[2]
        self.alarm_level_1_count = data_tuple[3]
        self.alarm_level_2_count = data_tuple[4]
        self.alarm_level_3_count = data_tuple[5]
        self.battery_alarm_count = data_tuple[6]
        self.motor_alarm_count = data_tuple[7]
        self.engine_alarm_count = data_tuple[8]
        self.other_alarm_count = data_tuple[9]

    def generate_insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        sql = f"REPLACE INTO {conf.target_ads_car_alarm_stats_table_name} {conf.target_ads_car_alarm_stats_table_insert_cols}" \
              f"VALUES(" \
              f"'{self.time_window}', " \
              f"'{self.date_ts}'," \
              f"'{self.total_alarm_count}', " \
              f"'{self.alarm_level_1_count}', " \
              f"{self.alarm_level_2_count}, " \
              f"{self.alarm_level_3_count}, " \
              f"{self.battery_alarm_count}, " \
              f"{self.motor_alarm_count}, " \
              f"{self.engine_alarm_count}, " \
              f"{self.other_alarm_count} " \
              f")"
        return sql

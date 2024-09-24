from chapter_5.config import project_config as conf


class CarChargingStatsModel(object):
    """
    carchargingstats information model class
    """
    def __init__(self, data_tuple: tuple):
        """
        Use the carchargingstats library field information as attributes
        The data is sent to data_tuple as a tuple => ('123987002321',
            'machine', '', '', '', 'pcs',
            'null', 0.0000, 0.0000, '2024-09-19 13:32:53', '', 0, 'null', 'null')
        """
        self.vin = data_tuple[0]
        self.date_ts = data_tuple[1]
        self.charge_start_time = data_tuple[2]
        self.charge_end_time = data_tuple[3]
        self.total_voltage = data_tuple[4]
        self.total_current = data_tuple[5]
        self.start_soc = data_tuple[6]
        self.end_soc = data_tuple[7]
        self.charge_duration = data_tuple[8]
        self.car_status = 2
        self.charge_status = 1
        self.execution_mode = 'null'

    def generate_insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        sql = f"REPLACE INTO {conf.target_dws_car_charging_stats_d_table_name} {conf.target_dws_car_charging_stats_d_table_insert_cols}" \
              f"VALUES(" \
              f"'{self.vin}', " \
              f"'{self.date_ts}'," \
              f"'{self.charge_start_time}', " \
              f"'{self.charge_end_time}', " \
              f"{self.total_voltage}, " \
              f"{self.total_current}, " \
              f"{self.start_soc}, " \
              f"{self.end_soc}, " \
              f"{self.charge_duration} " \
              f")"
        return sql

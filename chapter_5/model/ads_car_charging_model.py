from chapter_5.config import project_config as conf


class CarChargingStatsModel(object):
    """
    carchargingtats information model class
    """
    def __init__(self, data_tuple: tuple):
        """
        Use the carchargingtats library field information as attributes
        The data is sent to data_tuple as a tuple => ('123987002321',
            'machine', '', '', '', 'pcs',
            'null', 0.0000, 0.0000, '2024-09-19 13:32:53', '', 0, 'null', 'null')
        """
        self.time_window = data_tuple[0]
        self.vin = data_tuple[1]
        self.charging_count = data_tuple[2]
        self.total_charge_duration = data_tuple[3]

    def generate_insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        sql = f"REPLACE INTO {conf.target_ads_car_charging_stats_m_table_name} {conf.target_ads_car_charging_stats_m_table_insert_cols}" \
              f"VALUES(" \
              f"'{self.time_window}', " \
              f"'{self.vin}'," \
              f"{self.charging_count}, " \
              f"{self.total_charge_duration} " \
              f")"
        return sql

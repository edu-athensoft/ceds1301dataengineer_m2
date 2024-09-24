from chapter_5.config import project_config as conf


class CarDrivingStatsModel(object):
    """
    cardrivingstats information model class
    """
    def __init__(self, data_tuple: tuple):
        """
        Use the cardrivingstats library field information as attributes
        The data is sent to data_tuple as a tuple => ('123987002321',
            'machine', '', '', '', 'pcs',
            'null', 0.0000, 0.0000, '2024-09-19 13:32:53', '', 0, 'null', 'null')
        """
        self.vin = data_tuple[0]
        self.date_ts = data_tuple[1]
        self.avg_velocity = data_tuple[2]
        self.total_mileage = data_tuple[3]
        self.avg_voltage = data_tuple[4]
        self.max_temperature = data_tuple[5]
        self.car_status = data_tuple[6]
        self.charge_status = data_tuple[7]
        self.execution_mode = data_tuple[8]

    def generate_insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        sql = f"REPLACE INTO {conf.target_ads_car_electric_driving_stats_m_table_name} {conf.target_ads_car_electric_driving_stats_m_table_insert_cols}" \
              f"VALUES(" \
              f"'{self.vin}', " \
              f"'{self.date_ts}-01'," \
              f"{self.avg_velocity}, " \
              f"{self.total_mileage}, " \
              f"{self.avg_voltage}, " \
              f"{self.max_temperature}, " \
              f"{self.car_status}, " \
              f"{self.charge_status}, " \
              f"{self.execution_mode} " \
              f")"
        return sql

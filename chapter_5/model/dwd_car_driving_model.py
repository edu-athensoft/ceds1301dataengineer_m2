from chapter_5.config import project_config as conf


class CarDrivingModel(object):
    """
    cardriving information model class
    """

    def __init__(self, data_tuple: tuple):
        """
        Use the cardriving library field information as attributes
        The data is sent to data_tuple as a tuple => ('123987002321',
            'machine', '', '', '', 'pcs',
            'null', 0.0000, 0.0000, '2024-09-19 13:32:53', '', 0, 'null', 'null')
        """
        self.vin = data_tuple[0]
        self.car_status = data_tuple[1]
        self.charge_status = data_tuple[2]
        self.execution_mode = data_tuple[3]
        self.velocity = data_tuple[4]
        self.mileage = data_tuple[5]
        self.soc = data_tuple[6]
        self.voltage = data_tuple[7]
        self.electric_current = data_tuple[8]
        self.motor_count = data_tuple[9]
        self.max_voltage_battery_pack_id = data_tuple[10]
        self.max_voltage_battery_id = data_tuple[11]
        self.max_voltage = data_tuple[12]
        self.min_voltage_battery_pack_id = data_tuple[13]
        self.min_voltage_battery_id = data_tuple[14]
        self.min_voltage = data_tuple[15]
        self.date_ts = data_tuple[16]
        self.max_temperature = data_tuple[17]

    def generate_insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        sql = f"REPLACE INTO {conf.target_dwd_car_electric_driving_fact_table_name} {conf.target_dwd_car_electric_driving_fact_table_insert_cols}" \
              f"VALUES(" \
              f"'{self.vin}', " \
              f"{self.car_status}, " \
              f"{self.charge_status}, " \
              f"{self.execution_mode}, " \
              f"{self.velocity}, " \
              f"{self.mileage}, " \
              f"{self.soc}, " \
              f"{self.voltage}, " \
              f"{self.electric_current}, " \
              f"{self.motor_count}, " \
              f"{self.max_voltage_battery_pack_id}, " \
              f"{self.max_voltage_battery_id}, " \
              f"{self.max_voltage}, " \
              f"{self.min_voltage_battery_pack_id}, " \
              f"{self.min_voltage_battery_id}, " \
              f"{self.min_voltage}, " \
              f"'{self.date_ts}'," \
              f"{self.max_temperature} " \
              f")"

        return sql

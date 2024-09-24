from chapter_5.util import str_util
from chapter_5.config import project_config as conf

class CarChargingModel(object):
    """
    carcharging information model class
    """

    def __init__(self, data_tuple: tuple):
        """
        Use the carcharging library field information as attributes
        The data is sent to data_tuple as a tuple => ('123987002321',
            'machine', '', '', '', 'pcs',
            'null', 0.0000, 0.0000, '2024-09-19 13:32:53', '', 0, 'null', 'null')
        """
        self.vin = data_tuple[0]
        self.date_ts = data_tuple[1]
        self.car_status = data_tuple[2]
        self.charge_status = data_tuple[3]
        self.execution_mode = data_tuple[4]
        self.soc = data_tuple[5]
        self.voltage = data_tuple[6]
        self.electric_current = data_tuple[7]
        self.motor_count = data_tuple[8]
        self.max_voltage_battery_pack_id = data_tuple[9]
        self.max_voltage_battery_id = data_tuple[10]
        self.max_voltage = data_tuple[11]
        self.min_voltage_battery_pack_id = data_tuple[12]
        self.min_voltage_battery_id = data_tuple[13]
        self.min_voltage = data_tuple[14]
        self.max_temperature = data_tuple[15]
        self.battery_count = data_tuple[16]
        self.battery_pack_count = data_tuple[17]
        self.battery_voltages = data_tuple[18]
        self.battery_temperature_probe_count = data_tuple[19]
        self.battery_pack_temperature_count = data_tuple[20]
        self.battery_temperatures = data_tuple[21]

    def generate_insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        sql = f"REPLACE INTO {conf.target_dwd_car_charging_fact_table_name} {conf.target_dwd_car_charging_fact_table_insert_cols}" \
              f"VALUES(" \
              f"'{self.vin}', " \
              f"'{self.date_ts}'," \
              f"{self.car_status}, " \
              f"{self.charge_status}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.execution_mode)}, " \
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
              f"{self.max_temperature}, " \
              f"{self.battery_count}, " \
              f"{self.battery_pack_count}, " \
              f"'{self.battery_voltages}', " \
              f"{self.battery_temperature_probe_count}, " \
              f"{self.battery_pack_temperature_count}, " \
              f"'{self.battery_temperatures}' " \
              f")"

        return sql

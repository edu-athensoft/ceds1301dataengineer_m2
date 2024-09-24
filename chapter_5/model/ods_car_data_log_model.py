import json
from chapter_5.util import str_util, time_util
from chapter_5.config import project_config as conf


class CarDataLogModel(object):
    """
    CarDataLog information model class
    """

    def __init__(self, data):
        """
        Define related attributes. The class should have as many attributes as the target table has fields. The data source is JSON (string).
        Initialize the car_data_log model object => table name maps to class name, and fields in the table are mapped to object attributes => Pay attention to case sensitivity, object attributes are lowercase, and JSON parsing is case sensitive
        """
        data = json.loads(data)

        self.vin = data["vin"]
        self.car_status = data["car_status"]
        self.charge_status = data["charge_status"]
        self.execution_mode = data["execution_mode"]
        self.velocity = data["velocity"]
        self.mileage = data["mileage"]
        self.voltage = data["voltage"]
        self.electric_current = data["electric_current"]
        self.soc = data["soc"]
        self.dc_status = data["dc_status"]
        self.gear = data["gear"]
        self.insulation_resistance = data["insulation_resistance"]
        self.motor_count = data["motor_count"]
        self.fuel_cell_voltage = data["fuel_cell_voltage"]
        self.fuel_cell_current = data["fuel_cell_current"]
        self.fuel_cell_consume_rate = data["fuel_cell_consume_rate"]
        self.fuel_cell_temperature_probe_count = data["fuel_cell_temperature_probe_count"]
        self.fuel_cell_temperature = data["fuel_cell_temperature"]
        self.fuel_cell_max_temperature = data["fuel_cell_max_temperature"]
        self.fuel_cell_max_temperature_probe_id = data["fuel_cell_max_temperature_probe_id"]
        self.fuel_cell_max_hydrogen_consistency = data["fuel_cell_max_hydrogen_consistency"]
        self.fuel_cell_max_hydrogen_consistency_probe_id = data["fuel_cell_max_hydrogen_consistency_probe_id"]
        self.fuel_cell_max_hydrogen_pressure = data["fuel_cell_max_hydrogen_pressure"]
        self.fuel_cell_max_hydrogen_pressure_probe_id = data["fuel_cell_max_hydrogen_pressure_probe_id"]
        self.fuel_cell_dc_status = data["fuel_cell_dc_status"]
        self.engine_status = data["engine_status"]
        self.crankshaft_speed = data["crankshaft_speed"]
        self.fuel_consume_rate = data["fuel_consume_rate"]
        self.max_voltage_battery_pack_id = data["max_voltage_battery_pack_id"]
        self.max_voltage_battery_id = data["max_voltage_battery_id"]
        self.max_voltage = data["max_voltage"]
        self.min_temperature_subsystem_id = data["min_temperature_subsystem_id"]
        self.min_voltage_battery_id = data["min_voltage_battery_id"]
        self.min_voltage = data["min_voltage"]
        self.max_temperature_subsystem_id = data["max_temperature_subsystem_id"]
        self.max_temperature_probe_id = data["max_temperature_probe_id"]
        self.max_temperature = data["max_temperature"]
        self.min_voltage_battery_pack_id = data["min_voltage_battery_pack_id"]
        self.min_temperature_probe_id = data["min_temperature_probe_id"]
        self.min_temperature = data["min_temperature"]
        self.alarm_level = data["alarm_level"]
        self.alarm_sign = data["alarm_sign"]
        self.custom_battery_alarm_count = data["custom_battery_alarm_count"]
        self.custom_battery_alarm_list = data["custom_battery_alarm_list"]
        self.custom_motor_alarm_count = data["custom_motor_alarm_count"]
        self.custom_motor_alarm_list = data["custom_motor_alarm_list"]
        self.custom_engine_alarm_count = data["custom_engine_alarm_count"]
        self.custom_engine_alarm_list = data["custom_engine_alarm_list"]
        self.other_alarm_count = data["other_alarm_count"]
        self.other_alarm_list = data["other_alarm_list"]
        self.battery_count = data["battery_count"]
        self.battery_pack_count = data["battery_pack_count"]
        self.battery_voltages = data["battery_voltages"]
        self.battery_temperature_probe_count = data["battery_temperature_probe_count"]
        self.battery_pack_temperature_count = data["battery_pack_temperature_count"]
        self.battery_temperatures = data["battery_temperatures"]
        self.date_ts = data["timestamp"]
        self.date_timestamp = data["timestamp"]

    def generate_car_data_log_insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        return f"INSERT INTO {conf.target_ods_car_data_logs_table_name} {conf.target_ods_car_data_logs_table_insert_cols}" \
               f"VALUES (" \
               f"'{self.vin}'," \
               f"'{self.car_status}'," \
               f"'{self.charge_status}'," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.execution_mode)}," \
               f"'{self.velocity}'," \
               f"'{self.mileage}'," \
               f"'{self.voltage}'," \
               f"'{self.electric_current}'," \
               f"'{self.soc}'," \
               f"'{self.dc_status}'," \
               f"'{self.gear}'," \
               f"'{self.insulation_resistance}'," \
               f"'{self.motor_count}'," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.fuel_cell_voltage)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.fuel_cell_current)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.fuel_cell_consume_rate)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.fuel_cell_temperature_probe_count)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.fuel_cell_temperature)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.fuel_cell_max_temperature)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.fuel_cell_max_temperature_probe_id)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.fuel_cell_max_hydrogen_consistency)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.fuel_cell_max_hydrogen_consistency_probe_id)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.fuel_cell_max_hydrogen_pressure)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.fuel_cell_max_hydrogen_pressure_probe_id)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.fuel_cell_dc_status)}," \
               f"'{self.engine_status}'," \
               f"'{self.crankshaft_speed}'," \
               f"'{self.fuel_consume_rate}'," \
               f"'{self.max_voltage_battery_pack_id}'," \
               f"'{self.max_voltage_battery_id}'," \
               f"'{self.max_voltage}'," \
               f"'{self.min_temperature_subsystem_id}'," \
               f"'{self.min_voltage_battery_id}'," \
               f"'{self.min_voltage}'," \
               f"'{self.max_temperature_subsystem_id}'," \
               f"'{self.max_temperature_probe_id}'," \
               f"'{self.max_temperature}'," \
               f"'{self.min_voltage_battery_pack_id}'," \
               f"'{self.min_temperature_probe_id}'," \
               f"'{self.min_temperature}'," \
               f"'{self.alarm_level}'," \
               f"'{self.alarm_sign}'," \
               f"'{self.custom_battery_alarm_count}'," \
               f"'{self.custom_battery_alarm_list}'," \
               f"'{self.custom_motor_alarm_count}'," \
               f"'{self.custom_motor_alarm_list}'," \
               f"'{self.custom_engine_alarm_count}'," \
               f"'{self.custom_engine_alarm_list}'," \
               f"'{self.other_alarm_count}'," \
               f"'{self.other_alarm_list}'," \
               f"'{self.battery_count}'," \
               f"'{self.battery_pack_count}'," \
               f"'{self.battery_voltages}'," \
               f"'{self.battery_temperature_probe_count}'," \
               f"'{self.battery_pack_temperature_count}'," \
               f"'{self.battery_temperatures}'," \
               f"'{time_util.ts13_to_date_str(self.date_ts)}'," \
               f"'{self.date_timestamp}'" \
               f");"


class SingleCarDataMotorModel(object):
    """
    Build CarDataMotor model => An CarDataLog may contain multiple products. Since CarDataLog details are composed of multiple sold products
    Define related attributes. Since the product must belong to a certain CarDataLog, vin needs to be passed;
    """

    def __init__(self, vin, car_data_motor):
        self.vin = vin
        self.motor_list_id = car_data_motor['id']
        self.status = car_data_motor['status']
        self.rev = car_data_motor['rev']
        self.torque = car_data_motor['torque']
        self.controller_temperature = car_data_motor['controller_temperature']
        self.temperature = car_data_motor['temperature']
        self.voltage = car_data_motor['voltage']
        self.electric_current = car_data_motor['electric_current']

    def generate_value_segment_for_sql_insert(self):
        """
        Used to generate SQL statements for inserting product data => Do not generate field information, only generate the value to insert that part of the data
        insert into CarDataMotor values (value generated by product model),(value generated by product model),(value generated by product model)
        ('001', '123456', 'apple', 1, 9.98, 9.98, 8, 10, 1),('002', '123456', 'Oreo', 1, 9.98, 9.98, 8, 10, 1)
        :return:
        """
        return f"(" \
               f"'{self.vin}'," \
               f"{self.motor_list_id}," \
               f"{self.status}," \
               f"{self.rev}," \
               f"{self.torque}," \
               f"{self.controller_temperature}," \
               f"{self.temperature}," \
               f"{self.voltage}," \
               f"{self.electric_current}" \
               f")"


class CarDataMotorListModel(object):
    def __init__(self, data):
        """
        CarData details model writing => CarDataMotorModel => MySQL actually writes CarDataMotor data
        """
        data = json.loads(data)

        motor_list = data['motor_list']
        self.vin = data['vin']

        # Define a products_detail attribute to save all single product sales model objects Traverse
        # obtain the JSON information of each product and pass it to the SingleProductSoldModel
        # model to generate a product model object
        self.motor_list = []
        for single_motor in motor_list:
            motor = SingleCarDataMotorModel(self.vin, single_motor)
            self.motor_list.append(motor)

    def generate_car_data_motor_insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        sql = f"insert into {conf.target_ods_car_data_motor_list_table_name} {conf.target_ods_car_data_motor_list_table_insert_cols} " \
              "values "

        for single_motor in self.motor_list:
            sql += single_motor.generate_value_segment_for_sql_insert() + ', '

        # In SQL, the last parenthesis in the statement has an extra comma + space , insert into T values(), (), (),
        # the last space is -1, the last comma is -2
        sql = sql[:-2]
        return sql


class AnalysisCarDataLogModel(object):
    """
    Specially used to receive data in JSON format, and then generate CarDataLogModel and CarDataMotorListModel.
    The model needs to obtain a data => json format CarDataLog data, and then split it into two models: CarDataLog model + CarDataMotorList model
    """

    def __init__(self, data):
        self.car_data_log_model = CarDataLogModel(data)
        self.car_data_motor_list_model = CarDataMotorListModel(data)

    def get_car_data_log_model(self):
        """
        Get the car_data_log model object
        """
        return self.car_data_log_model

    def get_car_data_motor_list_model(self):
        """
        Get the car_data_motor_list details model object
        """
        return self.car_data_motor_list_model


if __name__ == '__main__':
    print("test")

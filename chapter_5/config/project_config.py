import time

# Common configuration of log module, requirements: set the public storage location of project log
# log file name (generate .log file every hour)
log_path = '/Users/kevin/workspace/python/etl/logs/'
log_name = f"pyetl-{time.strftime('%Y-%m-%d_%H', time.localtime())}.log"

batch_commit = 1000

# ################## --Metadata configuration items-- ###################
# Metadata configuration
metadata_host = 'localhost'
metadata_port = 3306
metadata_user = 'root'
metadata_password = '12345678'
metadata_db = 'metadata'

# Source database configuration
source_host = 'localhost'
source_port = 3306
source_user = 'root'
source_password = '12345678'
source_logs_db = "logs"
source_data_db = "data_warehouse"
source_ods_car_data_logs_table_name = 'ods_car_data_logs'
source_dwd_car_electric_driving_fact_table_name = 'dwd_car_electric_driving_fact'
source_dwd_car_charging_fact_table_name = 'dwd_car_charging_fact'
source_dwd_car_alarm_fact_table_name = 'dwd_car_alarm_fact'
source_dws_car_alarm_stats_d_table_name = 'dws_car_alarm_stats_d'
source_dws_car_electric_driving_d_table_name = 'dws_car_electric_driving_stats_d'
source_dws_car_charging_d_table_name = 'dws_car_charging_stats_d'

# Target database configuration
target_host = 'localhost'
target_port = 3306
target_user = 'root'
target_password = '12345678'
target_logs_db = "logs"
target_data_db = "data_warehouse"

# ################## --car JSON data collection configuration items-- ####################
# File path of JSON car data source
json_data_path = '/Users/kevin/workspace/python/etl/etl/chapter_5/file/json/'

# ################### --car JSON data collection configuration items-- ###################
# Collect car JSON data, metadata table configuration items
metadata_ods_car_data_logs_monitor_table_name = "ods_car_data_logs_monitor"
metadata_ods_car_data_logs_monitor_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT, " \
                                      "file_name VARCHAR(255) NOT NULL COMMENT 'Processing file name', " \
                                      "process_lines INT NULL COMMENT 'Number of file processing lines', " \
                                      "process_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'File processing time'" \
                                      ") engine=innodb default charset=utf8 COMMENT='';"

# ################## --Metadata DWD configuration items-- ###################

metadata_dwd_car_driving_monitor_table_name = "dwd_car_driving_monitor"
metadata_dwd_car_driving_monitor_table_create_cols = \
    "id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Auto-increment ID', " \
    "time_record TIMESTAMP NOT NULL COMMENT 'The maximum time of this collection record', " \
    "gather_line_count INT NULL COMMENT 'The number of collection records this time'" \
    ") engine=innodb default charset=utf8 COMMENT='';"
metadata_dwd_car_driving_monitor_table_insert_cols = "(time_record, gather_line_count)"


metadata_dwd_car_charging_monitor_table_name = "dwd_car_charging_monitor"
metadata_dwd_car_charging_monitor_table_create_cols = \
    "id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Auto-increment ID', " \
    "time_record TIMESTAMP NOT NULL COMMENT 'The maximum time of this collection record', " \
    "gather_line_count INT NULL COMMENT 'The number of collection records this time'" \
    ") engine=innodb default charset=utf8 COMMENT='';"
metadata_dwd_car_charging_monitor_table_insert_cols = "(time_record, gather_line_count)"


metadata_dwd_car_alarm_monitor_table_name = "dwd_car_alarm_monitor"
metadata_dwd_car_alarm_monitor_table_create_cols = \
    "id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Auto-increment ID', " \
    "time_record TIMESTAMP NOT NULL COMMENT 'The maximum time of this collection record', " \
    "gather_line_count INT NULL COMMENT 'The number of collection records this time'" \
    ") engine=innodb default charset=utf8 COMMENT='';"
metadata_dwd_car_alarm_monitor_table_insert_cols = "(time_record, gather_line_count)"

# ################## --Metadata DWD configuration items-- ###################


# ################## --Metadata DWS configuration items-- ###################
metadata_dws_car_driving_stats_monitor_table_name = "dws_car_driving_stats_monitor"
metadata_dws_car_driving_stats_monitor_table_create_cols = \
    "id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Auto-increment ID', " \
    "time_record TIMESTAMP NOT NULL COMMENT 'The maximum time of this collection record', " \
    "gather_line_count INT NULL COMMENT 'The number of collection records this time'" \
    ") engine=innodb default charset=utf8 COMMENT='';"

metadata_dws_car_driving_stats_monitor_table_insert_cols = "(time_record, gather_line_count)"


metadata_dws_car_charging_stats_monitor_table_name = "dws_car_charging_stats_monitor"
metadata_dws_car_charging_stats_monitor_table_create_cols = \
    "id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Auto-increment ID', " \
    "time_record TIMESTAMP NOT NULL COMMENT 'The maximum time of this collection record', " \
    "gather_line_count INT NULL COMMENT 'The number of collection records this time'" \
    ") engine=innodb default charset=utf8 COMMENT='';"

metadata_dws_car_charging_stats_monitor_table_insert_cols = "(time_record, gather_line_count)"


metadata_dws_car_alarm_stats_monitor_table_name = "dws_car_alarm_monitor"
metadata_dws_car_alarm_stats_monitor_table_create_cols = \
    "id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Auto-increment ID', " \
    "time_record TIMESTAMP NOT NULL COMMENT 'The maximum time of this collection record', " \
    "gather_line_count INT NULL COMMENT 'The number of collection records this time'" \
    ") engine=innodb default charset=utf8 COMMENT='';"

metadata_dws_car_alarm_stats_monitor_table_insert_cols = "(time_record, gather_line_count)"

# ################## --Metadata DWS configuration items-- ###################

# ods_car_data_logs table name
target_ods_car_data_logs_table_name = "ods_car_data_logs"
# ods_car_data_logs table MySQL database table creation statement column information
target_ods_car_data_logs_table_create_cols = \
    "id                                          BIGINT PRIMARY KEY AUTO_INCREMENT," \
    "vin                                         VARCHAR(50) COMMENT '汽车唯一ID'," \
    "car_status                                  INT COMMENT '车辆状态'," \
    "charge_status                               INT COMMENT '充电状态'," \
    "execution_mode                              varchar(255) COMMENT '运行模式'," \
    "velocity                                    INT COMMENT '车速'," \
    "mileage                                     INT COMMENT '里程'," \
    "voltage                                     INT COMMENT '总电压'," \
    "electric_current                            INT COMMENT '总电流'," \
    "soc                                         INT COMMENT 'SOC'," \
    "dc_status                                   INT COMMENT 'DC-DC状态'," \
    "gear                                        INT COMMENT '挡位'," \
    "insulation_resistance                       INT COMMENT '绝缘电阻'," \
    "motor_count                                 INT COMMENT '驱动电机个数'," \
    "fuel_cell_voltage                           varchar(255) COMMENT '燃料电池电压'," \
    "fuel_cell_current                           varchar(255) COMMENT '燃料电池电流'," \
    "fuel_cell_consume_rate                      varchar(255) COMMENT '燃料消耗率'," \
    "fuel_cell_temperature_probe_count           varchar(255) COMMENT '燃料电池温度探针总数'," \
    "fuel_cell_temperature                       varchar(255) COMMENT '燃料电池温度值'," \
    "fuel_cell_max_temperature                   varchar(255) COMMENT '氢系统中最高温度'," \
    "fuel_cell_max_temperature_probe_id          varchar(255) COMMENT '氢系统中最高温度探针号'," \
    "fuel_cell_max_hydrogen_consistency          varchar(255) COMMENT '氢气最高浓度'," \
    "fuel_cell_max_hydrogen_consistency_probe_id varchar(255) COMMENT '氢气最高浓度传感器代号'," \
    "fuel_cell_max_hydrogen_pressure             varchar(255) COMMENT '氢气最高压力'," \
    "fuel_cell_max_hydrogen_pressure_probe_id    varchar(255) COMMENT '氢气最高压力传感器代号'," \
    "fuel_cell_dc_status                         varchar(255) COMMENT '高压DC-DC状态'," \
    "engine_status                               INT COMMENT '发动机状态'," \
    "crankshaft_speed                            INT COMMENT '曲轴转速'," \
    "fuel_consume_rate                           INT COMMENT '燃料消耗率'," \
    "max_voltage_battery_pack_id                 INT COMMENT '最高电压电池子系统号'," \
    "max_voltage_battery_id                      INT COMMENT '最高电压电池单体代号'," \
    "max_voltage                                 INT COMMENT '电池单体电压最高值'," \
    "min_temperature_subsystem_id                INT COMMENT '最低电压电池子系统号'," \
    "min_voltage_battery_id                      INT COMMENT '最低电压电池单体代号'," \
    "min_voltage                                 INT COMMENT '电池单体电压最低值'," \
    "max_temperature_subsystem_id                INT COMMENT '最高温度子系统号'," \
    "max_temperature_probe_id                    INT COMMENT '最高温度探针号'," \
    "max_temperature                             INT COMMENT '最高温度值'," \
    "min_voltage_battery_pack_id                 INT COMMENT '最低温度子系统号'," \
    "min_temperature_probe_id                    INT COMMENT '最低温度探针号'," \
    "min_temperature                             INT COMMENT '最低温度值'," \
    "alarm_level                                 INT COMMENT '报警级别'," \
    "alarm_sign                                  INT COMMENT '通用报警标志'," \
    "custom_battery_alarm_count                  INT COMMENT '可充电储能装置故障总数N1'," \
    "custom_battery_alarm_list                   VARCHAR(500) COMMENT '可充电储能装置故障代码列表'," \
    "custom_motor_alarm_count                    INT COMMENT '驱动电机故障总数N2'," \
    "custom_motor_alarm_list                     VARCHAR(500) COMMENT '驱动电机故障代码列表'," \
    "custom_engine_alarm_count                   INT COMMENT '发动机故障总数N3'," \
    "custom_engine_alarm_list                    VARCHAR(500) COMMENT '发动机故障代码列表'," \
    "other_alarm_count                           INT COMMENT '其他故障总数N4'," \
    "other_alarm_list                            VARCHAR(500) COMMENT '其他故障代码列表'," \
    "battery_count                               INT COMMENT '单体电池总数'," \
    "battery_pack_count                          INT COMMENT '单体电池包总数'," \
    "battery_voltages                            VARCHAR(500) COMMENT '单体电池电压值列表'," \
    "battery_temperature_probe_count             INT COMMENT '单体电池温度探针总数'," \
    "battery_pack_temperature_count              INT COMMENT '单体电池包总数'," \
    "battery_temperatures                        VARCHAR(500) COMMENT '单体电池温度值列表'," \
    "date_timestamp                              BIGINT COMMENT '日志采集时间戳'," \
    "date_ts                                     timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '日志采集时间', " \
    "INDEX (vin), INDEX(date_ts), INDEX(car_status), INDEX(charge_status), INDEX(execution_mode) " \
    ") engine=innodb default charset=utf8 COMMENT='汽车日志表';"

target_ods_car_data_logs_table_insert_cols = " (vin,car_status,charge_status,execution_mode,velocity,mileage,voltage,electric_current,soc,dc_status,gear,insulation_resistance,motor_count,fuel_cell_voltage,fuel_cell_current,fuel_cell_consume_rate,fuel_cell_temperature_probe_count,fuel_cell_temperature,fuel_cell_max_temperature,fuel_cell_max_temperature_probe_id,fuel_cell_max_hydrogen_consistency,fuel_cell_max_hydrogen_consistency_probe_id,fuel_cell_max_hydrogen_pressure,fuel_cell_max_hydrogen_pressure_probe_id,fuel_cell_dc_status,engine_status,crankshaft_speed,fuel_consume_rate,max_voltage_battery_pack_id ,max_voltage_battery_id,max_voltage,min_temperature_subsystem_id,min_voltage_battery_id,min_voltage,max_temperature_subsystem_id,max_temperature_probe_id,max_temperature,min_voltage_battery_pack_id,min_temperature_probe_id,min_temperature,alarm_level,alarm_sign,custom_battery_alarm_count,custom_battery_alarm_list,custom_motor_alarm_count,custom_motor_alarm_list,custom_engine_alarm_count,custom_engine_alarm_list,other_alarm_count,other_alarm_list,battery_count,battery_pack_count,battery_voltages,battery_temperature_probe_count,battery_pack_temperature_count,battery_temperatures,date_ts,date_timestamp) "

# car_data_motor_list table name
target_ods_car_data_motor_list_table_name = "ods_car_data_motor_list"
# car_data_motor_list table column information
target_ods_car_data_motor_list_table_create_cols = \
    "id                        BIGINT PRIMARY KEY AUTO_INCREMENT, " \
    "vin                       VARCHAR(50) COMMENT '汽车唯一ID', " \
    "motor_list_id             INT COMMENT '驱动电机序号', " \
    "status                    INT COMMENT '驱动电机状态', " \
    "rev                       INT COMMENT '驱动电机转速', " \
    "torque                    INT COMMENT '驱动电机转矩', " \
    "controller_temperature    INT COMMENT '驱动电机控制器温度', " \
    "temperature               INT COMMENT '驱动电机温度', " \
    "voltage                   INT COMMENT '电机控制器输入电压', " \
    "electric_current          INT COMMENT '电机控制器直流母线电流', " \
    "INDEX (vin)                    " \
    ") engine=innodb default charset=utf8 COMMENT='驱动电机列表';"

target_ods_car_data_motor_list_table_insert_cols = " (vin,motor_list_id,status,rev,torque,controller_temperature,temperature,voltage,electric_current) "


# dim_car_status table name
target_dim_car_status_table_name = "dim_car_status"
target_dim_car_status_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT, " \
                                     "name VARCHAR(100) comment '名称', " \
                                     "type INT comment '类型'" \
                                     ") engine=innodb default charset=utf8 COMMENT='';"

# dim_charge_status table name
target_dim_charge_status_table_name = "dim_charge_status"
target_dim_charge_status_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT, " \
                                          "name VARCHAR(100) comment '名称', " \
                                          "type INT comment '类型'" \
                                          ") engine=innodb default charset=utf8 COMMENT='';"

# dim_execution_mode table name
target_dim_execution_mode_table_name = "dim_execution_mode"
target_dim_execution_mode_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT, " \
                                          "name VARCHAR(100) comment '名称', " \
                                          "type INT comment '类型'" \
                                          ") engine=innodb default charset=utf8 COMMENT='';"

# dim_motor_status table name
target_dim_motor_status_table_name = "dim_motor_status"
target_dim_motor_status_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT, " \
                                          "name VARCHAR(100) comment '名称', " \
                                          "type INT comment '类型'" \
                                          ") engine=innodb default charset=utf8 COMMENT='';"


# ################## -- datawarehouse DWD configuration items-- ###################
target_dwd_car_electric_driving_fact_table_name = "dwd_car_electric_driving_fact"

target_dwd_car_electric_driving_fact_table_create_cols =   \
   "id                            BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT," \
   "vin                           VARCHAR(50) DEFAULT NULL COMMENT '车辆唯一ID'," \
   "date_ts                       TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '行驶记录时间'," \
   "car_status                    INT DEFAULT NULL COMMENT '车辆状态'," \
   "charge_status                 INT DEFAULT NULL COMMENT '充电状态'," \
   "execution_mode                INT DEFAULT NULL COMMENT '运行模式'," \
   "velocity                      INT DEFAULT NULL COMMENT '车速'," \
   "mileage                       INT DEFAULT NULL COMMENT '行驶里程'," \
   "soc                           INT DEFAULT NULL COMMENT '电池电量状态（SOC）'," \
   "voltage                       INT DEFAULT NULL COMMENT '总电压'," \
   "electric_current              INT DEFAULT NULL COMMENT '总电流'," \
   "motor_count                   INT DEFAULT NULL COMMENT '驱动电机个数'," \
   "max_voltage_battery_pack_id   INT DEFAULT NULL COMMENT '最高电压电池子系统号'," \
   "max_voltage_battery_id        INT DEFAULT NULL COMMENT '最高电压电池单体代号'," \
   "max_voltage                   INT DEFAULT NULL COMMENT '电池单体电压最高值'," \
   "min_voltage_battery_pack_id   INT DEFAULT NULL COMMENT '最低电压电池子系统号'," \
   "min_voltage_battery_id        INT DEFAULT NULL COMMENT '最低电压电池单体代号'," \
   "min_voltage                   INT DEFAULT NULL COMMENT '电池单体电压最低值'," \
   "max_temperature               INT COMMENT '最高温度值'," \
   "INDEX (vin), INDEX(date_ts), INDEX(car_status), INDEX(charge_status), INDEX(execution_mode) " \
   ") engine=innodb default charset=utf8 COMMENT='电动模式行驶事实表';"

target_dwd_car_electric_driving_fact_table_insert_cols = "(vin,car_status,charge_status,execution_mode,velocity,mileage,soc,voltage,electric_current,motor_count,max_voltage_battery_pack_id,max_voltage_battery_id,max_voltage,min_voltage_battery_pack_id,min_voltage_battery_id,min_voltage,date_ts,max_temperature)"


target_dwd_car_charging_fact_table_name = "dwd_car_charging_fact"

target_dwd_car_charging_fact_table_create_cols = \
    "id                                     BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT," \
    "vin                                    VARCHAR(50) DEFAULT NULL COMMENT '车辆唯一ID'," \
    "date_ts                                TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '行驶记录时间'," \
    "car_status                             INT DEFAULT NULL COMMENT '车辆状态'," \
    "charge_status                          INT DEFAULT NULL COMMENT '充电状态'," \
    "execution_mode                         INT DEFAULT NULL COMMENT '运行模式'," \
    "soc                                    INT DEFAULT NULL COMMENT '电池电量状态（SOC）'," \
    "voltage                                INT DEFAULT NULL COMMENT '总电压'," \
    "electric_current                       INT DEFAULT NULL COMMENT '总电流'," \
    "motor_count                            INT DEFAULT NULL COMMENT '驱动电机个数'," \
    "max_voltage_battery_pack_id            INT DEFAULT NULL COMMENT '最高电压电池子系统号'," \
    "max_voltage_battery_id                 INT DEFAULT NULL COMMENT '最高电压电池单体代号'," \
    "max_voltage                            INT DEFAULT NULL COMMENT '电池单体电压最高值'," \
    "min_voltage_battery_pack_id            INT DEFAULT NULL COMMENT '最低电压电池子系统号'," \
    "min_voltage_battery_id                 INT DEFAULT NULL COMMENT '最低电压电池单体代号'," \
    "min_voltage                            INT DEFAULT NULL COMMENT '电池单体电压最低值'," \
    "max_temperature                        INT COMMENT '最高温度值'," \
    "battery_count                          INT COMMENT '单体电池总数'," \
    "battery_pack_count                     INT COMMENT '单体电池包总数'," \
    "battery_voltages                       VARCHAR(500) COMMENT '单体电池电压值列表'," \
    "battery_temperature_probe_count        INT COMMENT '单体电池温度探针总数'," \
    "battery_pack_temperature_count         INT COMMENT '单体电池包总数'," \
    "battery_temperatures                   VARCHAR(500) COMMENT '单体电池温度值列表'," \
    "INDEX (vin), INDEX(date_ts), INDEX(car_status), INDEX(charge_status), INDEX(execution_mode) " \
    ") engine=innodb default charset=utf8 COMMENT='电动模式行驶事实表';"

target_dwd_car_charging_fact_table_insert_cols = "(vin,date_ts,car_status,charge_status,execution_mode,soc,voltage,electric_current,motor_count,max_voltage_battery_pack_id,max_voltage_battery_id,max_voltage,min_voltage_battery_pack_id,min_voltage_battery_id,min_voltage,max_temperature,battery_count,battery_pack_count,battery_voltages,battery_temperature_probe_count,battery_pack_temperature_count,battery_temperatures)"

target_dwd_car_alarm_fact_table_name = "dwd_car_alarm_fact"

target_dwd_car_alarm_fact_table_create_cols = \
    "id                           BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT," \
    "vin                          VARCHAR(50) NOT NULL COMMENT '车辆唯一标识'," \
    "date_ts                      TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '故障发生时间'," \
    "alarm_level                  INT DEFAULT NULL COMMENT '报警级别'," \
    "alarm_sign                   INT DEFAULT NULL COMMENT '通用报警标志'," \
    "custom_battery_alarm_count   INT DEFAULT NULL COMMENT '储能装置故障总数'," \
    "custom_battery_alarm_list    VARCHAR(500) DEFAULT NULL COMMENT '储能装置故障代码列表'," \
    "custom_motor_alarm_count     INT DEFAULT NULL COMMENT '驱动电机故障总数'," \
    "custom_motor_alarm_list      VARCHAR(500) DEFAULT NULL COMMENT '驱动电机故障代码列表'," \
    "custom_engine_alarm_count    INT DEFAULT NULL COMMENT '发动机故障总数'," \
    "custom_engine_alarm_list     VARCHAR(500) DEFAULT NULL COMMENT '发动机故障代码列表'," \
    "other_alarm_count            INT DEFAULT NULL COMMENT '其他故障总数'," \
    "other_alarm_list             VARCHAR(500) DEFAULT NULL COMMENT '其他故障代码列表'," \
    "INDEX (vin), INDEX(date_ts) " \
    ") engine=innodb default charset=utf8 COMMENT='故障告警事实表';"

target_dwd_car_alarm_fact_table_insert_cols = "(vin,date_ts,alarm_level,alarm_sign,custom_battery_alarm_count,custom_battery_alarm_list,custom_motor_alarm_count,custom_motor_alarm_list,custom_engine_alarm_count,custom_engine_alarm_list,other_alarm_count,other_alarm_list)"


#
# target_dwd_car_hybrid_driving_fact_table_name =
#
# target_dwd_car_hybrid_driving_fact_table_create_cols =
#
# target_dwd_car_hybrid_driving_fact_table_insert_cols =



# ################## -- datawarehouse DWS configuration items-- ###################
target_dws_car_electric_driving_stats_d_table_name = "dws_car_electric_driving_stats_d"

target_dws_car_electric_driving_stats_d_table_create_cols = \
    "id                BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT, " \
    "vin               VARCHAR(50) DEFAULT NULL COMMENT '汽车唯一ID'," \
    "date_ts           TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '日期'," \
    "avg_velocity      DECIMAL(10,2) DEFAULT NULL COMMENT '平均行驶速度'," \
    "total_mileage     INT DEFAULT NULL COMMENT '总行驶里程'," \
    "avg_voltage       DECIMAL(10,2) DEFAULT NULL COMMENT '平均电池电压'," \
    "max_temperature   INT DEFAULT NULL COMMENT '最高温度值'," \
    "car_status        INT DEFAULT NULL COMMENT '车辆状态'," \
    "charge_status     INT DEFAULT NULL COMMENT '充电状态'," \
    "execution_mode    INT DEFAULT NULL COMMENT '运行模式'," \
    "INDEX (vin), INDEX(date_ts) " \
    ") engine=innodb default charset=utf8 COMMENT='电动模式行驶单日累计表';"

target_dws_car_electric_driving_stats_d_table_select_cols = "(vin,date(date_ts) AS date_ts,AVG(velocity)/10 AS avg_velocity,max(mileage)-min(mileage) AS total_mileage,AVG(voltage) AS avg_voltage,MAX(max_temperature) AS max_temperature,car_status,charge_status,execution_mode)"
target_dws_car_electric_driving_stats_d_table_insert_cols = "(vin,date_ts,avg_velocity,total_mileage,avg_voltage,max_temperature,car_status,charge_status,execution_mode)"


target_dws_car_charging_stats_d_table_name = "dws_car_charging_stats_d"

target_dws_car_charging_stats_d_table_create_cols = \
    "id                BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT, " \
    "vin               VARCHAR(50) DEFAULT NULL COMMENT '汽车唯一ID'," \
    "date_ts           TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '日期'," \
    "charge_start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '充电开始时间'," \
    "charge_end_time   TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '充电结束时间'," \
    "total_voltage     DECIMAL(10, 2) DEFAULT NULL COMMENT '充电时的总电压'," \
    "total_current     DECIMAL(10, 2) DEFAULT NULL COMMENT '充电时的总电流'," \
    "start_soc         INT DEFAULT NULL COMMENT '充电开始时的SOC'," \
    "end_soc           INT DEFAULT NULL COMMENT '充电结束时的SOC'," \
    "charge_duration   INT DEFAULT NULL COMMENT '充电持续时间（秒）'," \
    "INDEX (vin), INDEX(date_ts) " \
    ") engine=innodb default charset=utf8 COMMENT='充电单日累计表';"

target_dws_car_charging_stats_d_table_select_cols = "(vin,DATE(date_ts) AS date_ts,MIN(date_ts) AS charge_start_time,MAX(date_ts) AS charge_end_time,AVG(voltage) AS total_voltage,AVG(electric_current) AS total_current,MIN(soc) AS start_soc,MAX(soc) AS end_soc,TIMESTAMPDIFF(SECOND, MIN(date_ts), MAX(date_ts)) AS charge_duration)"
target_dws_car_charging_stats_d_table_insert_cols = "(vin,date_ts,charge_start_time,charge_end_time,total_voltage,total_current,start_soc,end_soc,charge_duration)"


target_dws_car_alarm_stats_d_table_name = "dws_car_alarm_stats_d"

target_dws_car_alarm_stats_d_table_create_cols = \
    "id                     BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT, " \
    "vin                    VARCHAR(50) NOT NULL COMMENT '车辆唯一标识'," \
    "date_ts                TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '统计日期'," \
    "total_alarm_count      INT DEFAULT NULL COMMENT '总报警次数'," \
    "alarm_level_1_count    INT DEFAULT NULL COMMENT '报警等级1次数'," \
    "alarm_level_2_count    INT DEFAULT NULL COMMENT '报警等级2次数'," \
    "alarm_level_3_count    INT DEFAULT NULL COMMENT '报警等级3次数'," \
    "battery_alarm_count    INT DEFAULT NULL COMMENT '电池报警次数'," \
    "motor_alarm_count      INT DEFAULT NULL COMMENT '驱动电机报警次数'," \
    "engine_alarm_count     INT DEFAULT NULL COMMENT '发动机报警次数'," \
    "other_alarm_count      INT DEFAULT NULL COMMENT '其他报警次数'," \
    "INDEX (vin), INDEX(date_ts) " \
    ") engine=innodb default charset=utf8 COMMENT='故障告警单日累计表';"

target_dws_car_alarm_stats_d_table_select_cols = \
    "(vin,DATE(date_ts) AS date_ts," \
    " COUNT(*) AS total_alarm_count,"\
    " SUM(CASE WHEN alarm_level = 1 THEN 1 ELSE 0 END) AS alarm_level_1_count,"\
    " SUM(CASE WHEN alarm_level = 2 THEN 1 ELSE 0 END) AS alarm_level_2_count,"\
    " SUM(CASE WHEN alarm_level = 3 THEN 1 ELSE 0 END) AS alarm_level_3_count,"\
    " SUM(custom_battery_alarm_count) AS battery_alarm_count,"\
    " SUM(custom_motor_alarm_count) AS motor_alarm_count,"\
    " SUM(custom_engine_alarm_count) AS engine_alarm_count," \
    " SUM(other_alarm_count) AS other_alarm_count )"

target_dws_car_alarm_stats_d_table_insert_cols = "(vin,date_ts,total_alarm_count,alarm_level_1_count,alarm_level_2_count,alarm_level_3_count,battery_alarm_count,motor_alarm_count,engine_alarm_count,other_alarm_count)"


# ################## -- datawarehouse ADS configuration items-- ###################
target_ads_car_alarm_stats_table_name = "ads_car_alarm_stats"
target_ads_car_alarm_stats_table_create_cols = \
    "id                     BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT, " \
    "time_window            VARCHAR(50) NOT NULL COMMENT '车辆唯一标识'," \
    "total_alarm_count      INT DEFAULT NULL COMMENT '总报警次数'," \
    "alarm_level_1_count    INT DEFAULT NULL COMMENT '报警等级1次数'," \
    "alarm_level_2_count    INT DEFAULT NULL COMMENT '报警等级2次数'," \
    "alarm_level_3_count    INT DEFAULT NULL COMMENT '报警等级3次数'," \
    "battery_alarm_count    INT DEFAULT NULL COMMENT '电池报警次数'," \
    "motor_alarm_count      INT DEFAULT NULL COMMENT '驱动电机报警次数'," \
    "engine_alarm_count     INT DEFAULT NULL COMMENT '发动机报警次数'," \
    "other_alarm_count      INT DEFAULT NULL COMMENT '其他报警次数'," \
    "date_ts              TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '统计日期'" \
    ") engine=innodb default charset=utf8 COMMENT='告警最近1/7/30天累计表';"

target_ads_car_alarm_stats_table_select_sql = \
    "SELECT " \
    "'1D' AS time_window, " \
    "CURRENT_DATE AS date_ts,      " \
    "SUM(total_alarm_count) AS total_alarm_count,     " \
    "SUM(alarm_level_1_count) AS alarm_level_1_count, " \
    "SUM(alarm_level_2_count) AS alarm_level_2_count, " \
    "SUM(alarm_level_3_count) AS alarm_level_3_count, " \
    "SUM(battery_alarm_count) AS battery_alarm_count, " \
    "SUM(motor_alarm_count) AS motor_alarm_count,     " \
    "SUM(engine_alarm_count) AS engine_alarm_count,   " \
    "SUM(other_alarm_count) AS other_alarm_count     " \
    "FROM " \
    "dws_car_alarm_stats_d " \
    "WHERE " \
    "date_ts >= DATE_SUB(CURRENT_DATE, INTERVAL 1 DAY) " \
    "union all " \
    "SELECT " \
    "'7D' AS time_window,  " \
    "CURRENT_DATE AS date_ts,      " \
    "SUM(total_alarm_count) AS total_alarm_count,     " \
    "SUM(alarm_level_1_count) AS alarm_level_1_count, " \
    "SUM(alarm_level_2_count) AS alarm_level_2_count, " \
    "SUM(alarm_level_3_count) AS alarm_level_3_count, " \
    "SUM(battery_alarm_count) AS battery_alarm_count, " \
    "SUM(motor_alarm_count) AS motor_alarm_count,     " \
    "SUM(engine_alarm_count) AS engine_alarm_count,   " \
    "SUM(other_alarm_count) AS other_alarm_count     " \
    "FROM " \
    "dws_car_alarm_stats_d " \
    "WHERE " \
    "date_ts >= DATE_SUB(CURRENT_DATE, INTERVAL 7 DAY) " \
    "union all " \
    "SELECT " \
    "'30D' AS time_window, " \
    "CURRENT_DATE AS date_ts,      " \
    "SUM(total_alarm_count) AS total_alarm_count, " \
    "SUM(alarm_level_1_count) AS alarm_level_1_count, " \
    "SUM(alarm_level_2_count) AS alarm_level_2_count, " \
    "SUM(alarm_level_3_count) AS alarm_level_3_count, " \
    "SUM(battery_alarm_count) AS battery_alarm_count, " \
    "SUM(motor_alarm_count) AS motor_alarm_count,     " \
    "SUM(engine_alarm_count) AS engine_alarm_count,   " \
    "SUM(other_alarm_count) AS other_alarm_count     " \
    "FROM " \
    "dws_car_alarm_stats_d " \
    "WHERE " \
    "date_ts >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)" \

target_ads_car_alarm_stats_table_delete_sql = "truncate table ads_car_alarm_stats "
target_ads_car_alarm_stats_table_insert_cols = "(time_window,date_ts,total_alarm_count,alarm_level_1_count,alarm_level_2_count,alarm_level_3_count,battery_alarm_count,motor_alarm_count,engine_alarm_count,other_alarm_count)"


target_ads_car_electric_driving_stats_m_table_name = "ads_car_electric_driving_stats_m"
target_ads_car_electric_driving_stats_m_table_create_cols = \
    "id                BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT, " \
    "vin               VARCHAR(50) DEFAULT NULL COMMENT '汽车唯一ID'," \
    "date_ts           TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '日期'," \
    "avg_velocity      DECIMAL(10,2) DEFAULT NULL COMMENT '平均行驶速度'," \
    "total_mileage     INT DEFAULT NULL COMMENT '总行驶里程'," \
    "avg_voltage       DECIMAL(10,2) DEFAULT NULL COMMENT '平均电池电压'," \
    "max_temperature   INT DEFAULT NULL COMMENT '最高温度值'," \
    "car_status        INT DEFAULT NULL COMMENT '车辆状态'," \
    "charge_status     INT DEFAULT NULL COMMENT '充电状态'," \
    "execution_mode    INT DEFAULT NULL COMMENT '运行模式'," \
    "INDEX (vin), INDEX(date_ts) " \
    ") engine=innodb default charset=utf8 COMMENT='电动模式行驶月累计表';"

target_ads_car_electric_driving_stats_m_table_select_sql = \
    "select " \
    "vin, " \
    "DATE_FORMAT(date_ts, '%Y-%m') AS date_ts, " \
    "AVG(avg_velocity) AS avg_velocity, " \
    "AVG(total_mileage) AS total_mileage, " \
    "AVG(avg_voltage) AS avg_voltage, " \
    "MAX(max_temperature) AS max_temperature, " \
    "car_status,charge_status,execution_mode " \
    "FROM dws_car_electric_driving_stats_d " \
    "group by vin,car_status,charge_status,execution_mode,DATE_FORMAT(date_ts, '%Y-%m') " \
    "order by DATE_FORMAT(date_ts, '%Y-%m')" \

target_ads_car_electric_driving_stats_m_table_delete_sql = "truncate table ads_car_electric_driving_stats_m"
target_ads_car_electric_driving_stats_m_table_insert_cols = "(vin,date_ts,avg_velocity,total_mileage,avg_voltage,max_temperature,car_status,charge_status,execution_mode)"


target_ads_car_charging_stats_table_name = "ads_car_charging_stats"
target_ads_car_charging_stats_table_create_cols = \
    "id                       BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT, " \
    "time_window              VARCHAR(50) NOT NULL COMMENT '车辆唯一标识'," \
    "vin                      VARCHAR(50) DEFAULT NULL COMMENT '汽车唯一ID'," \
    "charging_count           INT DEFAULT NULL COMMENT '充电次数'," \
    "total_charge_duration    INT DEFAULT NULL COMMENT '充电时长'," \
    "INDEX (vin) " \
    ") engine=innodb default charset=utf8 COMMENT='车辆充电最近1/7/30天累计表';"

target_ads_car_charging_stats_table_select_sql = \
    "SELECT '1D' AS time_window,vin,COUNT(*) AS charging_count,SUM(charge_duration) AS total_charge_duration " \
    "FROM dws_car_charging_stats_d " \
    "WHERE charge_end_time >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY) " \
    "GROUP BY vin " \
    "UNION ALL " \
    "SELECT '7D' AS time_window,vin,COUNT(*) AS charging_count,SUM(charge_duration) AS total_charge_duration " \
    "FROM dws_car_charging_stats_d " \
    "WHERE charge_end_time >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY) " \
    "GROUP BY vin " \
    "UNION ALL " \
    "SELECT '30D' AS time_window,vin,COUNT(*) AS charging_count,SUM(charge_duration) AS total_charge_duration " \
    "FROM dws_car_charging_stats_d " \
    "WHERE charge_end_time >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) " \
    "GROUP BY vin"

target_ads_car_charging_stats_table_delete_sql = "truncate table ads_car_charging_stats"
target_ads_car_charging_stats_table_insert_cols = "(time_window,vin,charging_count,total_charge_duration)"

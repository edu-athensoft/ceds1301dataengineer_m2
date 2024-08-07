import time

# Common configuration of log module, requirements: set the public storage location of project log
# log file name (generate .log file every hour)
log_path = '/Users/kevin/workspace/python/etl/logs/'
log_name = f"pyetl-{time.strftime('%Y-%m-%d_%H', time.localtime())}.log"

# ################## --Metadata configuration items-- ###################

# Target database configuration
target_host = 'localhost'
target_port = 3306
target_user = 'root'
target_password = '123456'
target_logs_db = "logs"
target_data_db = "data_warehouse"

# ################## --Background log data collection configuration items-- ####################
# Collect background log data, metadata table configuration items
logs_monitor_path = '/Users/kevin/workspace/python/etl/logs/log_monitor/'
logs_monitor_meta_table_name = "backend_logs_monitor"
logs_monitor_meta_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT, " \
                                      "file_name VARCHAR(255) NOT NULL COMMENT 'Processing file name', " \
                                      "process_lines INT NULL COMMENT 'Number of file processing lines', " \
                                      "process_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'File processing time'"


# Backend log table name
target_dim_time_table_name = "dim_time"
target_dim_time_table_create_cols = "TimeKey INT PRIMARY KEY, " \
                                "Date DATE, " \
                                "Year INT, " \
                                "Quarter INT, " \
                                "Month INT, " \
                                "Day INT, " \
                                "DayOfWeek VARCHAR(10) "

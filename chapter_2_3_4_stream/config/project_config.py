import time

# Common configuration of log module, requirements: set the public storage location of project log
# log file name (generate .log file every hour)
log_path = '/Users/kevin/workspace/python/etl/logs/'
log_name = f"pyetl-{time.strftime('%Y-%m-%d_%H', time.localtime())}.log"

# Target database configuration
target_host = 'localhost'
target_port = 3306
target_user = 'root'
target_password = '12345678'
target_logs_db = "logs"
target_data_db = "data_warehouse"

# Backend log table name
target_logs_table_name = "ods_backend_logs"
target_logs_table_create_cols = "id int PRIMARY KEY AUTO_INCREMENT COMMENT 'Auto-increment ID', " \
                                "log_time TIMESTAMP(6) COMMENT 'Log time, accurate to 6 milliseconds', " \
                                "log_level VARCHAR(10) COMMENT 'Log level', " \
                                "log_module VARCHAR(50) COMMENT 'Function module name for output log', " \
                                "response_time INT COMMENT 'Interface response time in milliseconds', " \
                                "state VARCHAR(30) COMMENT 'Visitor state', " \
                                "city VARCHAR(30) COMMENT 'Visitor city', " \
                                "log_text VARCHAR(255) COMMENT 'Log text', " \
                                "INDEX(log_time)"

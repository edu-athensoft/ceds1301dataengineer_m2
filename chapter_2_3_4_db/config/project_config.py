import time

# Common configuration of log module, requirements: set the public storage location of project log
# log file name (generate .log file every hour)
log_path = '/Users/kevin/workspace/python/etl/logs/'
log_name = f"pyetl-{time.strftime('%Y-%m-%d_%H', time.localtime())}.log"

# ################## --Metadata configuration items-- ###################
# Metadata configuration
metadata_host = 'localhost'
metadata_port = 3306
metadata_user = 'root'
metadata_password = '123456'
metadata_db = 'metadata'

# Target database configuration
target_host = 'localhost'
target_port = 3306
target_user = 'root'
target_password = '123456'
target_logs_db = "logs"
target_data_db = "data_warehouse"

# ################## --Database products commodity data collection configuration item-- ###################
# Metadatabase configuration
# Products business: the name of the monitoring table for the update_at field
metadata_products_table_name = 'products_monitor'
# Products business: column information of the table creation statement of the monitoring table of the update_at field
metadata_products_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Auto-increment ID', " \
                                   "time_record TIMESTAMP NOT NULL COMMENT 'The maximum time of this collection record', " \
                                   "gather_line_count INT NULL COMMENT 'The number of collection records this time'"

# Data source library configuration
source_host = 'localhost'
source_user = 'root'
source_password = '123456'
source_port = 3306
source_data_db = 'source_data'
# Data source table name
source_products_table_name = 'sys_products'

# product table name
target_products_table_name = 'ods_sys_products'
target_products_table_create_cols = "code varchar(50) PRIMARY KEY COMMENT 'Product barcode', " \
                                 "name varchar(200) DEFAULT '' COMMENT 'Product name'," \
                                 "spec varchar(200) DEFAULT '' COMMENT 'Product specifications'," \
                                 "trademark varchar(100) DEFAULT '' COMMENT 'Product trademark'," \
                                 "addr varchar(200) DEFAULT '' COMMENT 'Product origin'," \
                                 "units varchar(50) DEFAULT '' COMMENT 'Product unit (piece, cup, box, etc.)'," \
                                 "factory_name varchar(200) DEFAULT '' COMMENT 'Manufacturer'," \
                                 "trade_price DECIMAL(50, 5) DEFAULT 0.0 COMMENT 'Trade price (guiding purchase price)'," \
                                 "retail_price DECIMAL(50, 5) DEFAULT 0.0 COMMENT 'Retail price (suggested selling price)'," \
                                 "update_at timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time'," \
                                 "wholeunit varchar(50) DEFAULT NULL COMMENT 'Large packaging unit'," \
                                 "wholenum int(11) DEFAULT NULL COMMENT 'Large packaging quantity'," \
                                 "img varchar(500) DEFAULT NULL COMMENT 'Product image'," \
                                 "src varchar(20) DEFAULT NULL COMMENT 'Source information', " \
                                 "INDEX (update_at)"


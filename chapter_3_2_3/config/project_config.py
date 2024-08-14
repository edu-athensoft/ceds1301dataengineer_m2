import time

# Common configuration of log module, requirements: set the public storage location of project log
# log file name (generate .log file every hour)
log_path = '/Users/kevin/workspace/python/etl/logs/'
log_name = f"pyetl-{time.strftime('%Y-%m-%d_%H', time.localtime())}.log"

# Target database configuration
target_host = 'localhost'
target_port = 3306
target_user = 'root'
target_password = '123456'
target_logs_db = "logs"
target_data_db = "data_warehouse"


# dim_time table name
target_dim_time_table_name = "dim_time"
target_dim_time_table_create_cols = "id INT PRIMARY KEY, " \
                                "date DATE, " \
                                "year INT, " \
                                "quarter INT, " \
                                "month INT, " \
                                "day INT, " \
                                "day_of_week VARCHAR(10) "

# dim_store table name
target_dim_store_table_name = "dim_store"
target_dim_store_table_create_cols = "id INT PRIMARY KEY, " \
                                    "store_name VARCHAR(100), " \
                                    "location_id INT, " \
                                    "open_date DATE"


# dim_user table name
target_dim_user_table_name = "dim_user"
target_dim_user_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT, " \
                                    "user_id VARCHAR(100), " \
                                    "user_name VARCHAR(100), " \
                                    "gender VARCHAR(10), " \
                                    "birth_date DATE, " \
                                    "email VARCHAR(100), " \
                                    "phone_number VARCHAR(20), " \
                                    "address VARCHAR(200), " \
                                    "city VARCHAR(100), " \
                                    "state VARCHAR(100), " \
                                    "country VARCHAR(100), " \
                                    "postal_code VARCHAR(20), " \
                                    "start_date DATE, " \
                                    "end_date DATE, " \
                                    "status INT "


# dim_product table name
target_dim_product_table_name = "dim_product"
target_dim_product_table_create_cols = "id INT PRIMARY KEY, " \
                                       "product_name VARCHAR(100), " \
                                       "category VARCHAR(100), " \
                                       "brand VARCHAR(100), " \
                                       "supplier VARCHAR(100), " \
                                       "unit_price DECIMAL(10, 2), " \
                                       "unit_of_measure VARCHAR(50), " \
                                       "is_discontinued BOOLEAN, " \
                                       "launch_date DATE"


# dim_location table name
target_dim_location_table_name = "dim_location"
target_dim_location_table_create_cols = "id INT PRIMARY KEY, " \
                                        "country VARCHAR(100)," \
                                        "state VARCHAR(100)," \
                                        "city VARCHAR(100)," \
                                        "postal_code VARCHAR(20)," \
                                        "region_key INT "

# dim_region table name
target_dim_region_table_name = "dim_region"
target_dim_region_table_create_cols = "id INT PRIMARY KEY, " \
                                       "region_name VARCHAR(100), " \
                                       "region_type VARCHAR(50) "


# dwd_sale_order_fact table name
target_dwd_sale_order_fact_table_name = "dwd_sale_order_fact"
target_dwd_sale_order_fact_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT, "\
                                          "order_id varchar(255), " \
                                          "user_id INT, " \
                                          "store_id INT, " \
                                          "product_id INT, " \
                                          "pay_price DECIMAL(10, 5), " \
                                          "pay_type VARCHAR(10) , " \
                                          "date_ts timestamp  "

# dws_sale_product_info table name
target_dws_sale_product_price_info_table_name = "dws_sale_product_price_info"
target_dws_sale_product_price_info_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT, " \
                                                     "product_id INT, " \
                                                     "product_name VARCHAR(100), " \
                                                     "sale_price_count DECIMAL(10, 5), " \
                                                     "date_ts VARCHAR(100)  "

# dwd_sale_order_lifecycle_fact table name
target_dwd_sale_order_lifecycle_fact_table_name = "dwd_sale_order_lifecycle_fact"
target_dwd_sale_order_lifecycle_fact_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT, " \
                                                         "order_id varchar(255), " \
                                                         "user_id INT, " \
                                                         "payments_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, " \
                                                         "shipments_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  " \
                                                         "completions_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  " \
                                                         "pay_total DECIMAL(10, 5)"


# Data source library configuration
source_host = 'localhost'
source_user = 'root'
source_password = '123456'
source_port = 3306
source_data_db = 'source_data'
# Data source table name
source_order_payments_table_name = 'order_payments'
source_order_shipments_table_name = 'order_shipments'
source_order_completions_table_name = 'order_completions'

# Metadatabase configuration
metadata_host = 'localhost'
metadata_port = 3306
metadata_user = 'root'
metadata_password = '123456'
metadata_db = 'metadata'

# order_payments business: the name of the monitoring table for the update_at field
metadata_order_payments_table_name = 'order_payments_monitor'
# order_payments business: column information of the table creation statement of the monitoring table of the update_at field
metadata_order_payments_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Auto-increment ID', " \
                                      "time_record TIMESTAMP NOT NULL COMMENT 'The maximum time of this collection record', " \
                                      "gather_line_count INT NULL COMMENT 'The number of collection records this time'"

# order_shipments business: the name of the monitoring table for the update_at field
metadata_order_shipments_table_name = 'order_shipments_monitor'
# order_shipments business: column information of the table creation statement of the monitoring table of the update_at field
metadata_order_shipments_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Auto-increment ID', " \
                                            "time_record TIMESTAMP NOT NULL COMMENT 'The maximum time of this collection record', " \
                                            "gather_line_count INT NULL COMMENT 'The number of collection records this time'"

# order_completions business: the name of the monitoring table for the update_at field
metadata_order_completions_table_name = 'order_completions_monitor'
# order_completions business: column information of the table creation statement of the monitoring table of the update_at field
metadata_order_completions_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Auto-increment ID', " \
                                            "time_record TIMESTAMP NOT NULL COMMENT 'The maximum time of this collection record', " \
                                            "gather_line_count INT NULL COMMENT 'The number of collection records this time'"


# order_payments table name
target_order_payments_table_name = 'ods_order_payments'
target_order_payments_table_create_cols = "id INT PRIMARY KEY COMMENT '', " \
                                    "order_id varchar(200) DEFAULT '' COMMENT ''," \
                                    "update_at timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time'," \
                                    "INDEX (update_at)"

# order_shipments table name
target_order_shipments_table_name = 'ods_order_shipments'
target_order_shipments_table_create_cols = "id INT PRIMARY KEY COMMENT '', " \
                                          "order_id varchar(200) DEFAULT '' COMMENT ''," \
                                          "update_at timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time'," \
                                          "INDEX (update_at)"

# order_completions table name
target_order_completions_table_name = 'ods_order_completions'
target_order_completions_table_create_cols = "id INT PRIMARY KEY COMMENT '', " \
                                          "order_id varchar(200) DEFAULT '' COMMENT ''," \
                                          "update_at timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time'," \
                                          "INDEX (update_at)"

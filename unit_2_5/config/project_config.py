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

# ################## --Order JSON data collection configuration items-- ####################
# File path of JSON order data source
json_data_path = '/Users/kevin/workspace/python/etl/json/'

# ################### --Order JSON data collection configuration items-- ###################
# Collect order JSON data, metadata table configuration items
orders_json_file_monitor_meta_table_name = "orders_json_file_monitor"
orders_json_file_monitor_meta_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT, " \
                                      "file_name VARCHAR(255) NOT NULL COMMENT 'Processing file name', " \
                                      "process_lines INT NULL COMMENT 'Number of file processing lines', " \
                                      "process_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'File processing time'"

# Order table name
target_orders_table_name = "ods_orders"
# Order table MySQL database table creation statement column information
target_orders_table_create_cols = \
    f"order_id VARCHAR(255) PRIMARY KEY, " \
    f"store_id INT COMMENT 'Store ID', " \
    f"store_name VARCHAR(30) COMMENT 'Store name', " \
    f"store_status VARCHAR(10) COMMENT 'Store status (open, close)', " \
    f"store_own_user_id INT COMMENT 'Store owner id', " \
    f"store_own_user_name VARCHAR(50) COMMENT 'Store owner name', " \
    f"store_own_user_tel VARCHAR(15) COMMENT 'Store owner mobile phone number', " \
    f"store_category VARCHAR(10) COMMENT 'Store type (normal, test)', " \
    f"store_address VARCHAR(255) COMMENT 'Store address', " \
    f"store_shop_no VARCHAR(255) COMMENT 'Store third-party payment ID', " \
    f"store_province VARCHAR(10) COMMENT 'Store province', " \
    f"store_city VARCHAR(10) COMMENT 'Store city', " \
    f"store_district VARCHAR(10) COMMENT 'Store district', " \
    f"store_gps_name VARCHAR(255) COMMENT 'Store gps name', " \
    f"store_gps_address VARCHAR(255) COMMENT 'Store gps address', " \
    f"store_gps_longitude VARCHAR(255) COMMENT 'Store gps longitude', " \
    f"store_gps_latitude VARCHAR(255) COMMENT 'Store gps latitude', " \
    f"is_signed TINYINT COMMENT 'Whether third-party payment is signed (0,1)', " \
    f"operator VARCHAR(10) COMMENT 'Operator', " \
    f"operator_name VARCHAR(50) COMMENT 'Operator name', " \
    f"face_id VARCHAR(255) COMMENT 'Customer facial recognition ID', " \
    f"member_id VARCHAR(255) COMMENT 'Customer member ID', " \
    f"store_create_date_ts TIMESTAMP COMMENT 'Store creation time', " \
    f"origin VARCHAR(255) COMMENT 'Original information (useless)', " \
    f"day_order_seq INT COMMENT 'This order is the order of the day', " \
    f"discount_rate DECIMAL(10, 5) COMMENT 'Discount rate', " \
    f"discount_type TINYINT COMMENT 'discount type', " \
    f"discount DECIMAL(10, 5) COMMENT 'discount amount', " \
    f"money_before_whole_discount DECIMAL(10, 5) COMMENT 'total amount before discount', " \
    f"receivable DECIMAL(10, 5) COMMENT 'receivable amount', " \
    f"erase DECIMAL(10, 5) COMMENT 'erase amount', " \
    f"small_change DECIMAL(10, 5) COMMENT 'change amount', " \
    f"total_no_discount DECIMAL(10, 5) COMMENT 'total price (no discount)', " \
    f"pay_total DECIMAL(10, 5) COMMENT 'payment amount', " \
    f"pay_type VARCHAR(10) COMMENT 'payment type', " \
    f"payment_channel TINYINT COMMENT 'payment channel', " \
    f"payment_scenarios VARCHAR(15) COMMENT 'payment description (useless)', " \
    f"product_count INT COMMENT 'How many products were sold in this order', " \
    f"date_ts timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Order time', " \
    f"INDEX (receivable), INDEX (date_ts)"

# Order details table name
target_orders_detail_table_name = "ods_orders_detail"
# Order details table column information
target_orders_detail_table_create_cols = \
    f"order_id VARCHAR(255) COMMENT 'Order ID', " \
    f"barcode VARCHAR(255) COMMENT 'Product barcode', " \
    f"name VARCHAR(255) COMMENT 'Product name', " \
    f"count INT COMMENT 'Quantity of this product sold in this order', " \
    f"price_per DECIMAL(10, 5) COMMENT 'Actual selling price', " \
    f"retail_price DECIMAL(10, 5) COMMENT 'Retail suggested price', " \
    f"trade_price DECIMAL(10, 5) COMMENT 'Trade price (purchase price)', " \
    f"category_id INT COMMENT 'Product category ID', " \
    f"unit_id INT COMMENT 'Product unit ID (package, bag, box, etc.)', " \
    f"PRIMARY KEY (order_id, barcode)"

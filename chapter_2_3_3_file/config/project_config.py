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
metadata_password = '12345678'
metadata_db = 'metadata'

# Target database configuration
target_host = 'localhost'
target_port = 3306
target_user = 'root'
target_password = '12345678'
target_logs_db = "logs"
target_data_db = "data_warehouse"

# ################## --Order JSON data collection configuration items-- ####################
# File path of JSON order data source
json_data_path = '/Users/kevin/workspace/python/etl/etl/chapter_2_3_3_file/file/json/'

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
    "order_id VARCHAR(255) PRIMARY KEY, " \
    "store_id INT COMMENT 'Store ID', " \
    "store_name VARCHAR(30) COMMENT 'Store name', " \
    "store_status VARCHAR(10) COMMENT 'Store status (open, close)', " \
    "store_own_user_id INT COMMENT 'Store owner id', " \
    "store_own_user_name VARCHAR(50) COMMENT 'Store owner name', " \
    "store_own_user_tel VARCHAR(15) COMMENT 'Store owner mobile phone number', " \
    "store_category VARCHAR(10) COMMENT 'Store type (normal, test)', " \
    "store_address VARCHAR(255) COMMENT 'Store address', " \
    "store_shop_no VARCHAR(255) COMMENT 'Store third-party payment ID', " \
    "store_gps_name VARCHAR(255) COMMENT 'Store gps name', " \
    "store_gps_address VARCHAR(255) COMMENT 'Store gps address', " \
    "store_gps_longitude VARCHAR(255) COMMENT 'Store gps longitude', " \
    "store_gps_latitude VARCHAR(255) COMMENT 'Store gps latitude', " \
    "is_signed TINYINT COMMENT 'Whether third-party payment is signed (0,1)', " \
    "operator VARCHAR(10) COMMENT 'Operator', " \
    "operator_name VARCHAR(50) COMMENT 'Operator name', " \
    "face_id VARCHAR(255) COMMENT 'Customer facial recognition ID', " \
    "member_id VARCHAR(255) COMMENT 'Customer member ID', " \
    "store_create_date_ts TIMESTAMP COMMENT 'Store creation time', " \
    "origin VARCHAR(255) COMMENT 'Original information (useless)', " \
    "day_order_seq INT COMMENT 'This order is the order of the day', " \
    "discount_rate DECIMAL(10, 5) COMMENT 'Discount rate', " \
    "discount_type TINYINT COMMENT 'discount type', " \
    "discount DECIMAL(10, 5) COMMENT 'discount amount', " \
    "money_before_whole_discount DECIMAL(10, 5) COMMENT 'total amount before discount', " \
    "receivable DECIMAL(10, 5) COMMENT 'receivable amount', " \
    "erase DECIMAL(10, 5) COMMENT 'erase amount', " \
    "small_change DECIMAL(10, 5) COMMENT 'change amount', " \
    "total_no_discount DECIMAL(10, 5) COMMENT 'total price (no discount)', " \
    "pay_total DECIMAL(10, 5) COMMENT 'payment amount', " \
    "pay_type VARCHAR(10) COMMENT 'payment type', " \
    "payment_channel TINYINT COMMENT 'payment channel', " \
    "payment_scenarios VARCHAR(15) COMMENT 'payment description (useless)', " \
    "product_count INT COMMENT 'How many products were sold in this order', " \
    "date_ts timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Order time', " \
    "user_id INT , " \
    "INDEX (receivable), INDEX (date_ts)"

# Order details table name
target_orders_detail_table_name = "ods_orders_detail"
# Order details table column information
target_orders_detail_table_create_cols = \
    "order_id VARCHAR(255) COMMENT 'Order ID', " \
    "barcode VARCHAR(255) COMMENT 'Product barcode', " \
    "name VARCHAR(255) COMMENT 'Product name', " \
    "count INT COMMENT 'Quantity of this product sold in this order', " \
    "price_per DECIMAL(10, 5) COMMENT 'Actual selling price', " \
    "retail_price DECIMAL(10, 5) COMMENT 'Retail suggested price', " \
    "trade_price DECIMAL(10, 5) COMMENT 'Trade price (purchase price)', " \
    "category_id INT COMMENT 'Product category ID', " \
    "unit_id INT COMMENT 'Product unit ID (package, bag, box, etc.)', " \
    "product_id INT, " \
    "PRIMARY KEY (order_id, barcode)"

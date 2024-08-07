import json
from chapter_2_3_5_file.util import str_util, time_util
from chapter_2_3_5_file.config import project_config as conf


class OrdersModel(object):
    """
    order information model class
    """

    def __init__(self, data):
        """
        Define related attributes. The class should have as many attributes as the target table has fields. The data source is JSON (string).
        Initialize the order data model object => table name maps to class name, and fields in the table are mapped to object attributes => Pay attention to case sensitivity, object attributes are lowercase, and JSON parsing is case sensitive
        """
        data = json.loads(data)

        self.discount_rate = data['discountRate']  # Discount rate
        self.store_shop_no = data['storeShopNo']  # Store number (useless column)
        self.day_order_seq = data['dayOrderSeq']  # This order is the order of the day
        self.store_district = data['storeDistrict']  # Administrative district where the store is located
        self.is_signed = data['isSigned']  # Whether the store is signed (signed with a third-party payment system)
        self.store_province = data['storeProvince']  # Province where the store is located
        self.origin = data['origin']  # Original information (useless)
        self.store_gps_longitude = data['storeGPSLongitude']  # Store GPS longitude
        self.discount = data['discount']  # Discount amount
        self.store_id = data['storeID']  # Store ID
        self.product_count = data['productCount']  # Number of items sold in this order
        self.operator_name = data['operatorName']  # Operator name
        self.operator = data['operator']  # Operator ID
        self.store_status = data['storeStatus']  # Store status
        self.store_own_user_tel = data['storeOwnUserTel']  # Store owner phone number
        self.pay_total = data['payedTotal']  # Total payment amount
        self.pay_type = data['payType']  # Payment type
        self.discount_type = data['discountType']  # Discount type
        self.store_name = data['storeName']  # Store name
        self.store_own_user_name = data['storeOwnUserName']  # Store owner name
        self.date_ts = data['dateTS']  # Order time
        self.small_change = data['smallChange']  # Change amount
        self.store_gps_name = data['storeGPSName']  # Store GPS name
        self.erase = data['erase']  # Whether to round off
        self.store_gps_address = data['storeGPSAddress']  # Store GPS address
        self.order_id = data['orderID']  # Order ID
        self.money_before_whole_discount = data['moneyBeforeWholeDiscount']  # Amount before discount
        self.store_category = data['storeCategory']  # Store category
        self.receivable = data['receivable']  # Amount receivable
        self.face_id = data['faceID']  # Facial recognition ID
        self.store_own_user_id = data['storeOwnUserId']  # Store owner ID
        self.payment_channel = data['paymentChannel']  # Payment channel
        self.payment_scenarios = data['paymentScenarios']  # Payment scenario (useless)
        self.store_address = data['storeAddress']  # Store address
        self.total_no_discount = data['totalNoDiscount']  # Total price (no discount)
        self.payed_total = data['payedTotal']  # Paid amount
        self.store_gps_latitude = data['storeGPSLatitude']  # Store GPS latitude
        self.store_create_date_ts = data['storeCreateDateTS']  # Store creation time
        self.store_city = data['storeCity']  # Store city
        self.member_id = data['memberID']  # Member ID

    def generate_order_insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        return f"insert ignore into {conf.target_orders_table_name}(order_id,store_id,store_name,store_status,store_own_user_id,store_own_user_name,store_own_user_tel,store_category,store_address,store_shop_no,store_province,store_city,store_district,store_gps_name,store_gps_address,store_gps_longitude,store_gps_latitude,is_signed,operator,operator_name,face_id,member_id,store_create_date_ts,origin,day_order_seq,discount_rate,discount_type,discount,money_before_whole_discount,receivable,erase,small_change,total_no_discount,pay_total,pay_type,payment_channel,payment_scenarios,product_count,date_ts) values (" \
               f"'{self.order_id}'," \
               f"{self.store_id}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_name)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_status)}," \
               f"{self.store_own_user_id}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_own_user_name)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_own_user_tel)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_category)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_address)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_shop_no)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_province)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_city)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_district)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_name)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_address)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_longitude)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_latitude)}," \
               f"{self.is_signed}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.operator)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.operator_name)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.face_id)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.member_id)}," \
               f"'{time_util.ts13_to_date_str(self.store_create_date_ts)}'," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.origin)}," \
               f"{self.day_order_seq}," \
               f"{self.discount_rate}," \
               f"{self.discount_type}," \
               f"{self.discount}," \
               f"{self.money_before_whole_discount}," \
               f"{self.receivable}," \
               f"{self.erase}," \
               f"{self.small_change}," \
               f"{self.total_no_discount}," \
               f"{self.payed_total}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.pay_type)}," \
               f"{self.payment_channel}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.payment_scenarios)}," \
               f"{self.product_count}," \
               f"'{time_util.ts13_to_date_str(self.date_ts)}'" \
               f");"


class SingleProductSoldModel(object):
    """
    Build order details model => An order may contain multiple products. Since order details are composed of multiple sold products
    Define related attributes. Since the product must belong to a certain order, an order_id needs to be passed;
    """

    def __init__(self, order_id, product_detail):
        self.order_id = order_id
        self.barcode = product_detail['barcode']
        self.name = product_detail['name']
        self.count = product_detail['count']
        self.price_per = product_detail['pricePer']
        self.retail_price = product_detail['retailPrice']
        self.trade_price = product_detail['tradePrice']
        self.category_id = product_detail['categoryID']
        self.unit_id = product_detail['unitID']

    def generate_value_segment_for_sql_insert(self):
        """
        Used to generate SQL statements for inserting product data => Do not generate field information, only generate the value to insert that part of the data
        insert into orders_detail values (value generated by product model),(value generated by product model),(value generated by product model)
        ('001', '123456', 'apple', 1, 9.98, 9.98, 8, 10, 1),('002', '123456', 'Oreo', 1, 9.98, 9.98, 8, 10, 1)
        :return:
        """
        return f"(" \
               f"'{self.order_id}'," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.barcode)}," \
               f"{str_util.check_str_null_and_transform_to_sql_null(self.name)}," \
               f"{self.count}," \
               f"{self.price_per}," \
               f"{self.retail_price}," \
               f"{self.trade_price}," \
               f"{self.category_id}," \
               f"{self.unit_id}" \
               f")"


class OrdersDetailModel(object):
    def __init__(self, data):
        """
        Order details model writing => OrdersDetailModel => MySQL actually writes order details data
        """
        data = json.loads(data)
        # Extract all product data in JSON order
        order_products_list = data['product']
        # Extract the order number
        self.order_id = data['orderID']

        # Define a products_detail attribute to save all single product sales model objects Traverse
        # orders_products_list, obtain the JSON information of each product and pass it to the SingleProductSoldModel
        # model to generate a product model object
        self.products_detail = []
        for single_product in order_products_list:
            product = SingleProductSoldModel(self.order_id, single_product)
            self.products_detail.append(product)

    def generate_order_detail_insert_sql(self):
        """
        Generate SQL statement to insert data
        """
        sql = f"insert ignore into {conf.target_orders_detail_table_name}(order_id, barcode, name, count, price_per, retail_price, trade_price, category_id, unit_id) values "

        for single_product in self.products_detail:
            sql += single_product.generate_value_segment_for_sql_insert() + ', '

        # In SQL, the last parenthesis in the statement has an extra comma + space , insert into T values(), (), (),
        # the last space is -1, the last comma is -2
        sql = sql[:-2]
        return sql


class AnalysisOrderModel(object):
    """
    Specially used to receive data in JSON format, and then generate order model and order details model.
    The model needs to obtain a data => json format order data, and then split it into two models: order model + order details model
    """

    def __init__(self, data):
        self.order_model = OrdersModel(data)
        self.order_detail_model = OrdersDetailModel(data)

    def get_order_model(self):
        """
        Get the order model object
        """
        return self.order_model

    def get_order_detail_model(self):
        """
        Get the order details model object
        """
        return self.order_detail_model


if __name__ == '__main__':
    orders = OrdersModel(
        '{"discountRate": 1, "storeShopNo": "277551753310004", "dayOrderSeq": 26, "storeDistrict": "开福区", "isSigned": 1, "storeProvince": "湖南省", "origin": 0, "storeGPSLongitude": "112.99564674496649", "discount": 0, "storeID": 622, "productCount": 3, "operatorName": "OperatorName", "operator": "NameStr", "storeStatus": "open", "storeOwnUserTel": 12345678910, "payType": "cash", "discountType": 2, "storeName": "刘伟明便利店", "storeOwnUserName": "OwnUserNameStr", "dateTS": 1542436507000, "smallChange": 0, "storeGPSName": "None", "erase": 0, "product": [{"count": 1, "name": "健达缤纷乐T40g", "unitID": 3, "barcode": "80177609", "pricePer": 8, "retailPrice": 8, "tradePrice": 6, "categoryID": 1}, {"count": 1, "name": "娃哈哈氧道饮用水 550ml", "unitID": 2, "barcode": "6902083901233", "pricePer": 2, "retailPrice": 2, "tradePrice": 0, "categoryID": 1}, {"count": 1, "name": "红牛维生素功能饮料250ml", "unitID": 4, "barcode": "6920202888883", "pricePer": 6, "retailPrice": 6, "tradePrice": 0, "categoryID": 1}], "storeGPSAddress": "None", "orderID": "15424365069006223306", "moneyBeforeWholeDiscount": 16, "storeCategory": "normal", "receivable": 16, "faceID": "", "storeOwnUserId": 463, "paymentChannel": 0, "paymentScenarios": "OTHER", "storeAddress": "StoreAddress", "totalNoDiscount": 16, "payedTotal": 16, "storeGPSLatitude": "28.249745727366196", "storeCreateDateTS": 1531790437000, "storeCity": "长沙市", "memberID": "0"}')
    print(orders.generate_order_insert_sql())

    orders_detail = OrdersDetailModel(
        '{"discountRate": 1, "storeShopNo": "277551753310004", "dayOrderSeq": 26, "storeDistrict": "开福区", "isSigned": 1, "storeProvince": "湖南省", "origin": 0, "storeGPSLongitude": "112.99564674496649", "discount": 0, "storeID": 622, "productCount": 3, "operatorName": "OperatorName", "operator": "NameStr", "storeStatus": "open", "storeOwnUserTel": 12345678910, "payType": "cash", "discountType": 2, "storeName": "刘伟明便利店", "storeOwnUserName": "OwnUserNameStr", "dateTS": 1542436507000, "smallChange": 0, "storeGPSName": "None", "erase": 0, "product": [{"count": 1, "name": "健达缤纷乐T40g", "unitID": 3, "barcode": "80177609", "pricePer": 8, "retailPrice": 8, "tradePrice": 6, "categoryID": 1}, {"count": 1, "name": "娃哈哈氧道饮用水 550ml", "unitID": 2, "barcode": "6902083901233", "pricePer": 2, "retailPrice": 2, "tradePrice": 0, "categoryID": 1}, {"count": 1, "name": "红牛维生素功能饮料250ml", "unitID": 4, "barcode": "6920202888883", "pricePer": 6, "retailPrice": 6, "tradePrice": 0, "categoryID": 1}], "storeGPSAddress": "None", "orderID": "15424365069006223306", "moneyBeforeWholeDiscount": 16, "storeCategory": "normal", "receivable": 16, "faceID": "", "storeOwnUserId": 463, "paymentChannel": 0, "paymentScenarios": "OTHER", "storeAddress": "StoreAddress", "totalNoDiscount": 16, "payedTotal": 16, "storeGPSLatitude": "28.249745727366196", "storeCreateDateTS": 1531790437000, "storeCity": "长沙市", "memberID": "0"}')
    print(orders_detail.generate_order_detail_insert_sql())

CREATE TABLE order_payments (
    id INT PRIMARY KEY AUTO_INCREMENT,           -- 付款ID
    order_id varchar(255),                         -- 关联的订单ID
    payment_date timestamp                   -- 付款日期
);


CREATE TABLE order_shipments (
    id INT PRIMARY KEY AUTO_INCREMENT,          -- 发货ID
    order_id varchar(255),                         -- 关联的订单ID
    shipment_date timestamp                   -- 发货日期
);

CREATE TABLE order_completions (
    id INT PRIMARY KEY AUTO_INCREMENT,        -- 完成ID
    order_id varchar(255),                           -- 关联的订单ID
    completion_date timestamp                -- 订单完成日期
);


INSERT INTO `order_payments` VALUES (1, '154243845718910972315', '2018-11-19 10:57:54');
INSERT INTO `order_payments` VALUES (2, '154243845543910972315', '2018-11-19 11:31:14');
INSERT INTO `order_payments` VALUES (3, '154243844464316629102', '2018-11-17 15:07:36');
INSERT INTO `order_payments` VALUES (4, '154241234464316629102', '2018-11-17 23:46:26');
INSERT INTO `order_payments` VALUES (5, '154243844464768629102', '2018-11-17 20:26:26');
INSERT INTO `order_payments` VALUES (6, '154244034215713099309', '2018-11-18 10:57:54');


INSERT INTO `order_shipments` VALUES (1, '154241234464316629102', '2018-11-19 23:46:26');
INSERT INTO `order_shipments` VALUES (2, '154243844464316629102', '2018-11-22 15:07:36');
INSERT INTO `order_shipments` VALUES (3, '154243844464768629102', '2018-11-21 13:26:26');
INSERT INTO `order_shipments` VALUES (4, '154243845543910972315', '2018-11-23 11:31:14');
INSERT INTO `order_shipments` VALUES (5, '154243845718910972315', '2018-11-21 12:57:54');
INSERT INTO `order_shipments` VALUES (6, '154244034215713099309', '2018-11-20 10:57:54');


INSERT INTO `order_completions` VALUES (1, '154243845718910972315', '2018-11-28 10:57:54');
INSERT INTO `order_completions` VALUES (2, '154243845543910972315', '2018-11-26 20:31:14');
INSERT INTO `order_completions` VALUES (3, '154243844464316629102', '2018-11-25 15:07:36');
INSERT INTO `order_completions` VALUES (4, '154241234464316629102', '2018-11-20 23:46:26');
INSERT INTO `order_completions` VALUES (5, '154243844464768629102', '2018-11-23 20:26:26');
INSERT INTO `order_completions` VALUES (6, '154244034215713099309', '2018-11-25 10:57:54');
DROP TABLE IF EXISTS `sys_products`;
CREATE TABLE `sys_products` (
  `code` varchar(50) NOT NULL,
  `name` varchar(200) DEFAULT '',
  `spec` varchar(200) DEFAULT '',
  `trademark` varchar(100) DEFAULT '',
  `addr` varchar(200) DEFAULT '',
  `units` varchar(50) DEFAULT '',
  `factory_name` varchar(200) DEFAULT '',
  `trade_price` varchar(20) DEFAULT '0.0000',
  `retail_price` varchar(20) DEFAULT '0.0000',
  `updateAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `wholeunit` varchar(50) DEFAULT NULL,
  `wholenum` int(11) DEFAULT NULL,
  `img` varchar(500) DEFAULT NULL,
  `src` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `sys_products` VALUES ('1', 'Apple iPhone 14', '', '', '', 'Unit', '', '799.00', '0.0000', '2024-08-08 11:25:37', NULL, NULL, NULL, NULL);
INSERT INTO `sys_products` VALUES ('2', 'Samsung Galaxy S22', '', '', '', 'Unit', '', '749.00', '0.0000', '2024-08-08 11:25:37', NULL, NULL, NULL, NULL);
INSERT INTO `sys_products` VALUES ('3', 'Sony WH-1000XM4', '', '', '', 'Unit', '', '299.99', '0.0000', '2024-08-08 11:25:37', NULL, NULL, NULL, NULL);
INSERT INTO `sys_products` VALUES ('4', 'Dell XPS 13', '', '', '', 'Unit', '', '999.99', '0.0000', '2024-08-08 11:25:37', NULL, NULL, NULL, NULL);
INSERT INTO `sys_products` VALUES ('5', 'Nike Air Max 270', '', '', '', 'Pair', '', '150.00', '0.0000', '2024-08-08 11:25:37', NULL, NULL, NULL, NULL);
CREATE DATABASE 8_db;

USE 8_db;

SET time_zone = 'Asia/Ho_Chi_Minh';

CREATE TABLE products (
    id int(11) NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    slug varchar(255) NOT NULL,
    category varchar(50) NOT NULL,
    brand varchar(50) NOT NULL,
    price double NOT NULL,
    image_url varchar(255) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE product_audits (
  id int(11) NOT NULL AUTO_INCREMENT,
  action enum('insert','update','delete') NOT NULL,
  created_at datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY(id)
);

DELIMITER $$
CREATE TRIGGER product_after_insert AFTER INSERT ON products FOR EACH ROW BEGIN
   INSERT INTO product_audits
   VALUES (null, 'insert', NOW());
END
$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER product_after_update AFTER UPDATE ON products FOR EACH ROW BEGIN
   INSERT INTO product_audits
   VALUES (null, 'update', NOW());
END;
$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER product_after_delete AFTER DELETE ON products FOR EACH ROW BEGIN
   INSERT INTO product_audits
   VALUES (null, 'delete', NOW());
END
$$
DELIMITER ;
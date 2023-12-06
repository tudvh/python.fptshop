CREATE DATABASE 8_db;

USE 8_db;

CREATE TABLE products (
    id int(11) NOT NULL AUTO_INCREMENT,
    category varchar(50) NOT NULL,
    name varchar(100) NOT NULL,
    slug varchar(100) NOT NULL,
    price double NOT NULL,
    images_url varchar(255) NOT NULL,
    PRIMARY KEY(id)
);
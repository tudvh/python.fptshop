CREATE DATABASE 8_db;

USE 8_db;

CREATE TABLE products (
    id int(11) NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    slug varchar(100) NOT NULL,
    category varchar(50) NOT NULL,
    brand varchar(50) NOT NULL,
    price double NOT NULL,
    images_url varchar(255) NOT NULL,
    PRIMARY KEY(id)
);

-- CREATE TABLE product_history_changes (
--     id int(11) NOT NULL AUTO_INCREMENT,
--     inserted int(11) NOT NULL DEFAULT 0,
--     updated int(11) NOT NULL DEFAULT 0,
--     deleted int(11) NOT NULL DEFAULT 0,
--     created_at datetime NOT NULL DEFAULT current_timestamp(),
--     PRIMARY KEY(id)
-- );
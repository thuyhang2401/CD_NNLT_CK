CREATE DATABASE glasses_db;
USE glasses_db;
CREATE TABLE glasses (
    glasses_id varchar(20) NOT NULL ,
    link varchar(255) NOT NULL ,
    glasses_name varchar(100) NOT NULL ,
    brand_name varchar(100) NOT NULL,
    price float NOT NULL,
    img_url varchar(255) NOT NULL,
    PRIMARY KEY (glasses_id)
);

DELIMITER $
CREATE PROCEDURE search_glasses_by_price(
    IN min_price float,
    IN max_price float
  )
  BEGIN
    SELECT *
    FROM glasses
    WHERE price between min_price AND  max_price;
END$


CREATE PROCEDURE search_glasses_by_name(
    IN name_gl varchar(100)
  )
BEGIN
    IF name_gl IS NULL THEN
        SELECT * FROM glasses;
    ELSE
        SELECT *
        FROM glasses
        WHERE glasses_name LIKE CONCAT('%', name_gl, '%');
    END IF;
END$


CREATE PROCEDURE search_glasses_by_brand(
    IN name_brand varchar(100)
  )
BEGIN
    IF name_brand IS NULL THEN
        SELECT * FROM glasses;
    ELSE
        SELECT *
        FROM glasses
        WHERE brand_name  LIKE CONCAT('%', name_brand, '%');
    END IF;
END$

CREATE PROCEDURE insert_one_glasses(
    IN p_glasses_id VARCHAR(20),
    IN p_link VARCHAR(255),
    IN p_glasses_name VARCHAR(100),
    IN p_brand_name VARCHAR(100),
    IN p_price FLOAT,
    IN p_img_url VARCHAR(255)
)
BEGIN
    INSERT INTO glasses (glasses_id, link, glasses_name, brand_name, price, img_url)
    VALUES (p_glasses_id, p_link, p_glasses_name, p_brand_name, p_price, p_img_url);
END$

CREATE PROCEDURE get_all()
BEGIN
    SELECT * FROM glasses;
END$

CREATE PROCEDURE get_brands()
BEGIN
    SELECT DISTINCT brand_name FROM glasses;
END$
DELIMITER $
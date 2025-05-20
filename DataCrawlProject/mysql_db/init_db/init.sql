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

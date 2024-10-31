DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS seller;

CREATE TABLE seller (
    id int(11) NOT NULL AUTO_INCREMENT,
    name varchar(300) NOT NULL DEFAULT '',
    email varchar(300) NOT NULL DEFAULT '',
    status varchar(300) NOT NULL DEFAULT '',
    PRIMARY KEY (id)
);


CREATE TABLE item (
    id int(11) NOT NULL AUTO_INCREMENT,
    seller_id int(11) NOT NULL,
    item_name varchar(300) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (seller_id) REFERENCES seller(id)
);


INSERT INTO seller (name, email, status) VALUES
    ('Alice Smith', 'alice@example.com', 'ACTIVE'),
    ('Bob Johnson', 'bob@example.com', 'INACTIVE'),
    ('Charlie Brown', 'charlie@example.com', 'ACTIVE'),
    ('Dana White', 'dana@example.com', 'INACTIVE'),
    ('Eve Black', 'eve@example.com', 'ACTIVE'),
    ('Frank Green', 'frank@example.com', 'ACTIVE'),
    ('Grace Blue', 'grace@example.com', 'INACTIVE'),
    ('Hank Purple', 'hank@example.com', 'ACTIVE'),
    ('Ivy Orange', 'ivy@example.com', 'INACTIVE'),
    ('Jack Gray', 'jack@example.com', 'ACTIVE');


INSERT INTO item (seller_id, item_name, price) VALUES
    (1, 'Laptop', 999.99),
    (2, 'Smartphone', 599.99),
    (3, 'Tablet', 399.99),
    (4, 'Monitor', 199.99),
    (5, 'Keyboard', 49.99),
    (6, 'Mouse', 29.99),
    (7, 'Desk', 129.99),
    (8, 'Chair', 89.99),
    (9, 'Headphones', 79.99),
    (10, 'Webcam', 39.99),
    (1, 'Laptop Sleeve', 19.99),
    (2, 'Charger', 25.99),
    (3, 'USB Cable', 9.99),
    (4, 'HDMI Cable', 14.99),
    (5, 'Mouse Pad', 5.99),
    (6, 'External HDD', 79.99),
    (7, 'Desk Lamp', 34.99),
    (8, 'Office Chair Mat', 49.99),
    (9, 'Bluetooth Speaker', 49.99),
    (10, 'Docking Station', 74.99);


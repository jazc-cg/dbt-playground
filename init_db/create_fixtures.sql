CREATE TABLE IF NOT EXISTS orders (
    id INT,
    created_timestamp timestamp,
    product_id INT
);

CREATE TABLE IF NOT EXISTS products (
    id INT,
    name VARCHAR,
    description VARCHAR,
    created_timestamp timestamp
);

insert into orders values
(1, now(), 1001),
(2, now(), 1002),
(3, now(), 1003),
(4, now(), 1001),
(5, now(), 1002),
(6, now(), 1001),
(7, now(), 1003),
(8, now(), 1002),
(9, now(), 1004),
(10, now(), 1002);

insert into products values
(1001, 'product_1', 'product 1 description'),
(1002, 'product_2', 'product 2 description'),
(1003, 'product_3', 'product 3 description'),
(1004, 'product_4', 'product 4 description');

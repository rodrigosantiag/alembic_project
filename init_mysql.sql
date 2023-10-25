CREATE TABLE IF NOT EXISTS products
(
    id   INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    slug VARCHAR(100) UNIQUE
);

TRUNCATE TABLE products;

INSERT INTO products (name, slug)
VALUES ('Product 1', 'product_1'),
       ('Product 2', 'product_2'),
       ('Product 3', 'product_3');

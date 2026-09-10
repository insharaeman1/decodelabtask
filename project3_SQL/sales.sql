CREATE TABLE sales (
    order_id INTEGER,
    customer TEXT,
    city TEXT,
    product TEXT,
    quantity INTEGER,
    price REAL
);

INSERT INTO sales (order_id, customer, city, product, quantity, price)
VALUES
(1, 'Ali', 'Lahore', 'Laptop', 1, 80000),
(2, 'Ahmed', 'Karachi', 'Mouse', 2, 2000),
(3, 'Sara', 'Lahore', 'Laptop', 1, 80000),
(4, 'Hamza', 'Islamabad', 'Keyboard', 3, 3000),
(5, 'Ayesha', 'Karachi', 'Monitor', 2, 25000),
(6, 'Zara', 'Lahore', 'Mouse', 4, 2000);

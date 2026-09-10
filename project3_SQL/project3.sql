-- PROJECT 3: SQL DATA ANALYSIS

-- 1. SELECT
SELECT *
FROM sales;

-- 2. WHERE
SELECT *
FROM sales
WHERE city = 'Lahore';

-- 3. ORDER BY
SELECT *
FROM sales
ORDER BY price DESC;

-- 4. COUNT
SELECT COUNT(*) AS total_orders
FROM sales;

-- 5. SUM
SELECT SUM(quantity * price) AS total_sales
FROM sales;

-- 6. AVG
SELECT AVG(price) AS average_price
FROM sales;

-- 7. GROUP BY + COUNT
SELECT city, COUNT(*) AS total_orders
FROM sales
GROUP BY city;

-- 8. GROUP BY + SUM
SELECT city, SUM(quantity * price) AS total_sales
FROM sales
GROUP BY city
ORDER BY total_sales DESC;

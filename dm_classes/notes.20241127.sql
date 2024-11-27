-- departments(department_id, department)
-- aisles(aisle_id, aisle)
-- products(product_id, product_name, aisle_id, department_id)
-- orders(order_id, user_id, order_number, order_dow, order_hour_of_day, days_since_prior_order)
-- order_products(order_id, product_id, add_to_cart_order, reordered)

-- tick the statement that cannot generate an error
A. DELETE FROM aisles WHERE aisle_id = 5;
B. DELETE FROM departments WHERE department_id = 8;
C. UPDATE aisles SET aisle_id = 4 WHERE aisle_id = 5;
D. UPDATE departments SET department_id = 7 WHERE department_id = 8;
E. UPDATE departments SET department = 'data science' WHERE department_id = 8; -- correct answer


-- tick the statement that generates an error
A. DELETE FROM order_products WHERE order_id = 5;
B. DELETE FROM products WHERE product_id = 8292;
C. DELETE FROM orders WHERE order_id = 4848; -- correct answer
D. DELETE FROM order_products WHERE product_id = 0494;


-- Retrieve the order_id and the product_name for each order submitted on Monday (order_dow = 1)
SELECT o.order_id, product_name
FROM order o, order_products op, products p
WHERE o.order_id = op.order_id AND op.product_id = p.product_id
AND order_dow = 1;


-- Retrieve the order_id and the name of products that are added as first in the cart of each order (add_to_cart_order = 1)
SELECT op.order_id, product_name
FROM order_products op, products p
WHERE op.product_id = p.product_id
AND op.add_to_cart_order = 1;

-- alternative syntax
SELECT op.order_id, product_name
FROM order_products op INNER JOIN products p ON op.product_id = p.product_id
WHERE p.add_to_cart_order = 1;


-- Retrieve the order_id and the product_name for each order submitted between the hours 15 and 17
SELECT order_products.order_id, product_name
FROM order_products INNER JOIN products ON order_products.product_id = products.product_id INNER JOIN orders ON order_products.order_id = orders.order_id
WHERE order_hour_of_day >= 15 AND order_hour_of_day <= 17;


-- Retrieve the id of orders where the first product added to the cart is the same as the one in the order_id = 2411567
-- nested query (subquery)
SELECT order_id
FROM order_products
WHERE add_to_cart_order = 1 AND product_id IN (
SELECT product_id
FROM order_products
WHERE order_id = '2411567' AND add_to_cart_order = 1)

-- CTE
with first_item_2411567 as (
    SELECT product_id
    FROM order_products
    WHERE order_id = '2411567' AND add_to_cart_order = 1
)
SELECT order_id
FROM order_products op, first_item_2411567 fi
WHERE add_to_cart_order = 1 AND op.product_id = fi.product_id;

-- self join
SELECT op.order_id
FROM order_products op INNER JOIN order_products fi ON op.product_id = fi.product_id
WHERE op.add_to_cart_order = 1 AND fi.add_to_cart_order = 1 AND fi.order_id = '2411567';


-- Retrieve the name of products that are ordered on Monday (order_dow = 1) from the coffee aisle. Sort the result by the product name
SELECT DISTINCT product_name
FROM products INNER JOIN order_products ON order_products.product_id = products.product_id INNER JOIN aisles ON products.aisle_id = aisles.aisle_id INNER JOIN orders ON order_products.order_id = orders.order_id
WHERE aisles.aisle = 'coffee' AND order_dow = 1
ORDER BY product_name;


-- Retrieve the id of products that are never ordered on Tuesday (order_dow = 2)

-- consider the following solution. is it ok? no because a product can be sold on tuesday and another day and it is still in the result (and it is wrong)
SELECT distinct product_id
FROM order_products op INNER JOIN orders o ON op.order_id = o.order_id
WHERE order_dow <> 2;

-- except solution
-- A except B

-- A part:
SELECT product_id
FROM products
EXCEPT
-- B part:
SELECT distinct product_id
FROM order_products op INNER JOIN orders o ON op.order_id = o.order_id
WHERE order_dow = 2;

-- nested query solution
SELECT product_id
FROM products
WHERE product_id NOT IN (
SELECT distinct product_id
FROM order_products op INNER JOIN orders o ON op.order_id = o.order_id
WHERE order_dow = 2);


-- Retrieve the id of products from the coffee aisle that are never ordered on Tuesay (order_dow = 2)
SELECT product_id
FROM products INNER JOIN aisles ON products.aisle_id = aisles.aisle_id
WHERE aisle = 'coffee'
EXCEPT
SELECT product_id
FROM order_products INNER JOIN orders ON order_products.order_id = orders.order_id
WHERE order_dow = 2;


-- Retrieve the id of users that submitted orders on BOTH Monday (order_dow = 1) and Tuesday (order_dow = 2).
SELECT user_id
FROM orders
WHERE order_dow = 1
INTERSECT
SELECT user_id
FROM orders
WHERE order_dow = 2;


-- Retrieve the average number of products in the orders
WITH order_count as (SELECT order_id, count(*) as product_count
FROM order_products
GROUP BY order_id)
SELECT avg(product_count)
FROM order_count


-- For each department, retrieve the number of ordered products. Show the department_name in the result. Sort the result by the number of products in descending order
SELECT d.department, count(op.product_id) as p_count
FROM departments d INNER JOIN products p ON d.department_id = p.department_id INNER JOIN order_products op ON p.product_id = op.product_id
GROUP BY d.department_id, d.department
ORDER by p_count DESC
-- order by 2 desc


-- Refine the previous query by returning only the departments with more than 1M of ordered products
SELECT d.department, count(op.product_id) as p_count
FROM departments d INNER JOIN products p ON d.department_id = p.department_id INNER JOIN order_products op ON p.product_id = op.product_id
GROUP BY d.department_id, d.department
HAVING count(*) > 1000000
order by 2 desc;


-- For each product in the coffee aisle, retrieve the number of orders submitted on Tuesday (order_dow = 2). Include in the result the products that are never ordered (if they exist)
SELECT products.product_id, product_name, count(orders.order_id) 
FROM aisles INNER JOIN products ON products.aisle_id = aisles.aisle_id LEFT JOIN order_products ON order_products.product_id = products.product_id
LEFT JOIN orders ON (order_products.order_id = orders.order_id AND order_dow = 2) 
WHERE aisles.aisle = 'coffee'
GROUP BY products.product_id, product_name
ORDER BY 3;



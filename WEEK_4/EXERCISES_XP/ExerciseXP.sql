-- create table customers (
-- id serial primary key,
-- Name varchar,
-- Surname varchar )
-- ;

-- create table items (
-- id serial primary key,
-- furnuture varchar,
-- price float ) 
-- ;

-- SELECT * FROM customers
-- SELECT * FROM items

-- INSERT INTO customers (name, surname)
-- VALUES ('Greg', 'Jones'),
-- 		('Sandra', 'Jones'),
-- 		('Scott', 'Scott'), 
-- 		('Trevor', 'Green'),
-- 		('Melanie', 'Johnson')
		
-- INSERT INTO items (furnuture, price)
-- VALUES ('Small Desk', 100),
-- 		('Large Desk', 300),
-- 		('Fan', 80)

-- SELECT * FROM customers

-- SELECT * FROM items
-- SELECT furnuture, price from items where price > 80
-- SELECT furnuture, price from items where price < 300 OR price = 300

-- SELECT name, surname from customers where surname = 'Smith' 
-- -- shows just empty columns under the fields
-- SELECT name, surname from customers where surname = 'Jones' 
SELECT name, surname from customers where name != 'Scott' 




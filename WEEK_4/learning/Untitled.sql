-- create table house_expenses (
-- id serial primary key,
-- 	date_paid date,
-- 	electricity float,
-- 	water float,
-- 	paid_by varchar(50)

-- );

-- INSERT INTO house_expenses (date_paid, electricity, water, paid_by)
-- VALUES 
-- ('2023-11-12', 200.03, 54.43, 'Ola');
-- INSERT INTO house_expenses (date_paid, electricity, water, paid_by)
-- VALUES 
-- ('2023-12-12', 199.03, 53.43, 'Ola'),
-- ('2024-01-12', 230.03, 56.43, 'Max'),
-- ('2024-02-12', 210.03, 51.43, 'Ola'),
-- ('2024-03-12', 205.03, 59.43, 'Max'),
-- ('2024-04-12', 219.03, 61.43, 'Max');

-- SELECT * FROM house_expenses
-- SELECT electricity FROM house_expenses
-- SELECT electricity, water FROM house_expenses


-- SELECT * from house_expenses WHERE id = 1 OR id = 2
-- SELECT * from house_expenses WHERE id < 3

-- SELECT * from house_expenses WHERE id in (1,2);
-- SELECT * from house_expenses WHERE paid_by != 'Ola'
-- SELECT * from house_expenses WHERE paid_by = 'Ola'

-- COUNT() MAX() MIN() SUM() AVG()

-- SELECT MAX(water) from house_expenses 
-- SELECT MIN(electricity) from house_expenses
-- SELECT AVG(electricity + water) as average_sum from house_expenses where paid_by != 'Max'

--  SELECT sum(electricity) from house_expenses
--  GROUP BY paid_by 
--  SELECT paid_by, sum(electricity) from house_expenses
--  GROUP BY paid_by 
 
-- SELECT paid_by, sum(electricity + water), max(electricity + water), avg(electricity + water) 
-- from house_expenses 
-- -- where electricity > 200

-- GROUP BY paid_by

-- UPDATE house_expenses
-- SET electricity = 250, water = 70
-- WHERE id  = 6

-- SELECT * FROM house_expenses

-- UPDATE house_expenses
-- SET electricity = 250, water = 70
-- WHERE id  = 5

-- SELECT * FROM house_expenses

-- UPDATE house_expenses
-- SET paid_by = 'Max'
-- WHERE id  = 1

-- SELECT * FROM house_expenses

-- UPDATE house_expenses
-- SET paid_by = 'Max'
-- WHERE id  = 1


-- UPDATE house_expenses
-- SET electricity = 0
-- WHERE paid_by = 'Ola'

-- DELETE FROM house_expenses WHERE electricity < 50
-- DELETE FROM house_expenses WHERE date_paid > '2024-03-13'
 
--  delete all data and restart the table TRUNCATE TABLE table_name RESTART IDENTITY;
-- delete the table DROP TABLE IF EXISTS table_name;


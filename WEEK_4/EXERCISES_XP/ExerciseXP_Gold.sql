-- create table students (
-- id serial primary key,
-- first_name varchar,
-- last_name varchar,
-- birth_date date )
-- ;

-- INSERT INTO students(first_name, last_name, birth_date)
-- VALUES 
-- ('Marc', 'Benichou', '1998-11-02'),
-- ('Yoan', 'Cohen', '2010-12-03'),
-- ('Lea', 'Benichou', '1987-07-27'),
-- ('Amelia', 'Dux', '1996-04-07'),
-- ('David', 'Grez', '2003-06-14'),
-- ('Omer', 'Simpson', '1980-10-03')

-- SELECT * FROM students
-- SELECT first_name, last_name FROM students
-- SELECT first_name, last_name FROM students where id = 2
-- SELECT first_name, last_name FROM students where last_name = 'Benichou' AND first_name = 'Marc'
-- SELECT first_name, last_name FROM students where last_name = 'Benichou' OR first_name = 'Marc'
-- SELECT first_name, last_name FROM students where last_name = 'Benichou' AND first_name = 'Marc'
-- SELECT first_name, last_name FROM students where first_name LIKE '%a%'
-- SELECT first_name, last_name FROM students where first_name LIKE 'A%'
-- SELECT first_name, last_name FROM students where first_name LIKE '%a'
-- SELECT first_name, last_name FROM students where substring (first_name, length(first_name) - 1, 1) = 'a'
-- SELECT first_name, last_name FROM students where id IN (1, 3)

SELECT * FROM students where birth_date >= '2000-01-01'



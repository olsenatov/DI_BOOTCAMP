-- -- PART 1
-- -- #1 - #3
-- CREATE TABLE Customer (
--     id serial PRIMARY KEY,
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE CustomerProfile (
--     id serial PRIMARY KEY,
--     isLoggedIn BOOLEAN DEFAULT false,
--     customer_id INT references Customer(id) UNIQUE
-- )

-- INSERT INTO Customer (first_name, last_name)
-- VALUES
--     ( 'John', 'Doe'),
--     ( 'Jerome', 'Lalu'),
--     ( 'Lea', 'Rive');

-- INSERT INTO CustomerProfile (isLoggedIn, customer_id)
-- VALUES
--     (true, (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe')),
--     (false, (SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

-- -- #4.1
-- SELECT customer.first_name
-- FROM Customer 
-- INNER JOIN CustomerProfile ON customer.id = CustomerProfile.customer_id
-- WHERE CustomerProfile.isLoggedIn = true;

-- -- #4.2
-- SELECT customer.first_name, CustomerProfile.isLoggedIn
-- FROM Customer 
-- LEFT JOIN CustomerProfile ON customer.id = CustomerProfile.customer_id;

-- -- #4.3
-- SELECT COUNT(*) 
-- FROM Customer
-- LEFT JOIN CustomerProfile ON customer.id = CustomerProfile.customer_id
-- WHERE CustomerProfile.isLoggedIn IS NULL OR CustomerProfile.isLoggedIn = false;


-- -- Part 2
-- -- #1
-- CREATE TABLE Book (
--     book_id serial PRIMARY KEY,
--     title VARCHAR(100) NOT NULL,
--     author VARCHAR(50) NOT NULL
-- );

-- -- #2
-- INSERT INTO Book (title, author)
-- VALUES
--     ('Alice In Wonderland', 'Lewis Carroll'),
--     ('Harry Potter', 'J.K. Rowling'),
--     ('To Kill a Mockingbird', 'Harper Lee');

-- -- #3
-- CREATE TABLE Student (
--     student_id serial PRIMARY KEY,
--     name VARCHAR(50) NOT NULL UNIQUE,
--     age INT CHECK (age <= 15)
-- );

-- -- #4
-- INSERT INTO Student (name, age)
-- VALUES
--     ('John', 12),
--     ('Lera', 11),
--     ('Patrick', 10),
--     ('Bob', 14);

-- -- #5
-- CREATE TABLE Library (
--     book_fk_id INT references Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     student_fk_id INT references Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     borrowed_date DATE,
--     PRIMARY KEY (book_fk_id, student_fk_id)
-- );

-- -- #6
-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES
-- ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'John'), '2022-02-15'),

-- ((SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-03-03'),

-- ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'Lera'), '2021-05-23'),

-- ((SELECT book_id FROM Book WHERE title = 'Harry Potter'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-08-12');
-- 

-- -- #7.1
-- SELECT * from Library

-- -- #7.2
-- SELECT student.name, book.title, student.age
-- FROM Library
-- JOIN Student ON library.student_fk_id = student.student_id
-- JOIN Book ON library.book_fk_id = book.book_id;

-- -- #7.3
-- SELECT AVG(age) AS average_age
-- FROM Library 
-- JOIN Student ON library.student_fk_id = student.student_id
-- JOIN Book ON library.book_fk_id = book.book_id 
-- WHERE book.title = 'Alice in Wonderland';

-- SELECT AVG(age) AS average_age
-- FROM Student
-- JOIN library ON student.student_id = library.student_fk_id 
-- JOIN Book ON library.book_fk_id = book.book_id 
-- WHERE book.title = 'Alice in Wonderland';

-- -- don't know what happens, seems to me, that i wrote everything right, whatever I  try, it returns Null
-- -- even though in the previous exercise there're obviously 2 students reading this book - i can count AVG is 11.5 years =)

-- -- #7.4
-- DELETE FROM Student WHERE name = 'Lera';
-- -- After deleting the student from the "Student" table, any record in the "Library" table 
-- -- that had a foreign key reference to the deleted student will be deleted due to 
-- -- ON DELETE CASCADE setting in Library table defenition
-- select * from Library -- shows 3 records remaining

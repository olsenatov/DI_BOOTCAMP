-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- );

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES
-- ('Matt','Damon','08/10/1970', 5),
-- ('George','Clooney','06/05/1961', 2),
-- ('Brad', 'Pitt', '1980-04-22', 1),
-- ('Matt', 'Damon', '1982-11-22', 2),
-- ('Patrick', 'Jolie', '1980-04-22', 1),
-- ('Marc', 'Benichou', '1998-11-02',0), 
-- ('Yoan', 'Cohen', '2010-12-03',0), 
-- ('Lea',	'Benichou', '1987-07-27',0), 
-- ('Amelia', 'Dux', '1996-04-07',0), 
-- ('David', 'Grez', '2003-06-14',0), 
-- ('Omer', 'Simpson', '1980-10-03',1); 

-- SELECT AVG(number_oscars) from actors
-- SELECT first_name, last_name from actors where number_oscars = 1
-- SELECT  DISTINCT number_oscars from actors 
--  SELECT first_name, last_name, number oscars from actors 
--  GROUP BY number_oscars
 
-- SELECT * from actors where first_name in ('David', 'Morgan', 'Will')

-- SELECT number_oscars, count(number_oscars) from actors 
-- GROUP BY number_oscars

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- create table country (
-- id smallserial primary key,
-- name varchar(50) not null,
-- country_code smallint not null check(country_code < 50)
-- );
-- -- one to many

-- FOREIGN KEY(country_id) REFERENCES country(id)

-- ALTER table actors
-- add column country_id smallint;

-- ALTER table actors
-- add foreign key (country_id) references country(id);


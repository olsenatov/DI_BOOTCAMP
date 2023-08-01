-- -- ExerciseXP1
-- -- #1
-- SELECT DISTINCT(language.language_id), language.name from language
-- INNER JOIN film ON language.language_id = film.language_id

-- -- #2
-- SELECT film.title, film.description, language.name 
-- from film
-- INNER JOIN language ON film.language_id = language.language_id

-- -- #2.1 Lise said it's wrong

-- -- #2.2
-- SELECT film.title, film.description, language.name 
-- from film
-- FULL JOIN language ON film.language_id = language.language_id

-- -- #3
-- CREATE table new_film (
-- id serial Primary key,
-- name varchar(50) NOT NULL
-- );

-- INSERT INTO new_film (name)
-- VALUES
-- ('Green Mile'),
-- ('Tree of Life'),
-- ('Inception'),
-- ('Arrival');

-- -- #4 + #4.1 - #4.7
-- CREATE table customer_review (
-- review_id serial Primary key NOT NULL,
-- film_id int references new_film(id) ON DELETE CASCADE,
-- language_id int references language(language_id) ON DELETE CASCADE,
-- title varchar(50) NOT NULL,
-- score int DEFAULT 1 CHECK(score BETWEEN 1 AND 10),
-- review_text varchar,
-- last_update date,
-- name varchar(50) NOT NULL
-- );

-- -- #5
-- INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update, name)
-- VALUES
-- ((select id from new_film where name = 'Inception'), (select language_id from language where name = 'English'), 'Perfect!', 10, 'This film I will remember forever, I came out of cinema ompletely different person', '2007-11-03', 'Mark'),
-- ((select id from new_film where name = 'Green Mile'), (select language_id from language where name = 'German'), 'Gut', 8, 'Der Film ist nicht für Kinder, aber sehr gut und emotional', '2003-12-01', 'Ursula')
-- SELECT * from customer_review

-- -- #6 - the review is deleted with the film
-- DELETE FROM new_film where name = 'Inception'
-- SELECT * from customer_review


-- -- EXERCISEXP2

-- -- #1
-- UPDATE film
-- set language_id = (select language_id from language where name = 'Italian')
-- where title = 'Atlantis Cause' OR title = 'Baby Hall' OR title = 'Chitty Lock'

-- SELECT title, language_id from film where title = 'Atlantis Cause' OR title = 'Baby Hall' OR title = 'Chitty Lock'

-- -- #2
-- store_id, address_id - we need to insert into these columns of the table using subqueries like (select store_id from store where address = 'something')
-- (select address_id from address where address = 'something')

-- -- #3 - went easy
-- drop table customer_review


-- -- #4 - 183
-- SELECT Count(*) from rental where return_date is Null

-- -- #5 - checking for replacement cost
-- SELECT film.title, film.replacement_cost 
-- from inventory 
-- join film on film.film_id  = inventory.inventory_id
-- join rental on rental.inventory_id = inventory.inventory_id
-- where rental.return_date is null
-- order by film.replacement_cost DESC 
-- LIMIT 30

-- -- #6.1

-- select film.title, film.description, actor.first_name, actor.last_name
-- from film_actor
-- join film on film.film_id = film_actor.film_id
-- join actor on actor.actor_id = film_actor.actor_id
-- where actor.first_name = 'Penelope' AND actor.last_name = 'Monroe' AND film.description ILIKE '%sumo wrestler%'

-- -- #6.2
-- select film.title, film.length, film.rating, category.name
-- from film
-- join film_category on film_category.film_id = film.film_id
-- join category on film_category.category_id = category.category_id
-- WHERE name = 'Documentary' AND length < 60 AND rating = 'R'

-- -- #6.3
-- -- conditions:
-- -- film.title ?
-- -- customer.first_name = 'Matthew' customer.last_name = 'Mahan'
-- -- payment.amount > 4 !
-- -- rental.rental_date between '2005-07-28' and '2005-08-01'
-- -- rental.inventory_id -> inventory.inventory_id inventory.film_id ->film.film_id

-- select film.title, customer.first_name, customer.last_name, rental.return_date, payment.amount
-- from rental
-- join customer on customer.customer_id = rental.customer_id
-- join payment on payment.customer_id = customer.customer_id
-- join inventory on inventory.inventory_id = rental.inventory_id
-- join film on film.film_id = inventory.film_id
-- where customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND rental.return_date between '2005-07-28' and '2005-08-01' AND payment.amount > 4
 -- -- somehow can't make it show up only 1 film, shows 3 in numerous copies, don't understand the logic of how it happens
 
-- -- #6.4
-- SELECT title, replacement_cost, description
-- from film
-- join inventory on inventory.film_id = film.film_id
-- join rental on rental.inventory_id = inventory.inventory_id
-- join customer on customer.customer_id = rental.customer_id
-- where title ILIKE '%boat%' OR description ILIKE '%boat%' AND customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
-- ORDER BY replacement_cost DESC
-- LIMIT 1
-- -- don't know, if the limit is the right thing to use here, as if LIMIT 2, the second fild is also rather expencive to replace
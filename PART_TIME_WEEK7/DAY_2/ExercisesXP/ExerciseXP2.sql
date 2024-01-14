-- SELECT * from customer -- 1

-- SELECT first_name || ' ' || last_name AS full_name FROM customer -- 2

-- SELECT DISTINCT create_date from customer -- 3

-- SELECT * from customer ORDER BY first_name DESC -- 4

-- SELECT film_id, title, description, release_year, rental_rate from film ORDER BY rental_rate ASC -- 5

-- SELECT address, phone from address where district = 'Texas' -- 6

-- SELECT * from film where film_id = 15 OR film_id = 150 -- 7

-- SELECT film_id, title, description, length, rental_rate from film where title = 'Dozen Lion'-- 8 favourite movie to check  - Shawshank Redemption - none, actually in the list - Dozen Lion - gives its details

-- SELECT film_id, title, description, length, rental_rate from film where title LIKE 'Sh%' -- 9

-- SELECT * from film 
-- ORDER BY rental_rate ASC
-- LIMIT 10   -- 10

-- SELECT * from film 
-- ORDER BY rental_rate ASC 
-- FETCH FIRST 10 ROWS ONLY
-- OFFSET 10 -- 11

-- SELECT customer.first_name, customer.last_name, payment.payment_date, payment.amount
-- from customer
-- INNER JOIN payment ON customer.customer_id = payment.customer_id 
-- Order by payment_id -- 12

-- SELECT film.film_id, film.title, film.rental_rate, inventory.inventory_id
-- FROM film 
-- LEFT JOIN inventory ON film.film_id = inventory.film_id
-- WHERE inventory.inventory_id is null -- 13

-- SELECT city.city, country.country from city 
-- INNER JOIN country on 
-- city.country_id = country.country_id -- 14

-- SELECT customer.first_name, customer.last_name, payment.payment_date, payment.amount, staff_id
-- from customer
-- INNER JOIN payment ON customer.customer_id = payment.customer_id 
-- Order by staff_id -- 15


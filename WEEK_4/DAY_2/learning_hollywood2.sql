-- insert into country (name, country_code)
-- values
-- ('USA', 40),
-- ('France', 33),
-- ('UK', 20);

-- ONE TO MANY 

-- actors --> country

-- UPDATE actors set country_id = 1 where first_name = 'Matt'

-- SELECT id from country where name = 'USA';

-- UPDATE actors set country_id = (SELECT id from country where name = 'USA') where first_name = 'George'

-- UPDATE actors set country_id = (SELECT id from country where name = 'France') where last_name in ('Benichou', 'Grez', 'Dux')
-- UPDATE actors set country_id = (SELECT id from country where name = 'UK') where last_name in ('Jolie', 'Pitt', 'Cohen', 'Simpson')

-- select actors.first_name, actors.last_name, country.name
-- from actors
-- join country
-- on actors.country_id = country.id
-- where actors.first_name != 'Matt'
-- order by actors.last_name
-- ;

-- MANY TO MANY

-- create table movie (
-- id serial primary key,
-- title varchar(50) not null,
-- country_id smallint references country(id)
-- 	);

-- insert into movie (title, country_id)
-- values
-- ('Good Will Hunting', (select id from country where name = 'USA')),
-- ('Jason Bourne', (select id from country where name = 'USA')),
-- ('Oceans 8', (select id from country where name = 'UK')),
-- ('Oceans Twelve', (select id from country where name = 'UK'));

-- create table actors_movies (
-- id serial primary key,
-- actor_id int references actors(actor_id),
-- movie_id smallint references movie(id)
-- 	);

-- insert into actors_movies (actor_id, movie_id) values
-- ((select actor_id from actors where first_name = 'Matt'), (select id from movie where title = 'Good Will Hunting')),
-- ((select actor_id from actors where first_name = 'Matt'), (select id from movie where title = 'Jason Bourne')),
-- ((select actor_id from actors where first_name = 'Matt'), (select id from movie where title = 'Oceans 8')),
-- ((select actor_id from actors where first_name = 'George'), (select id from movie where title = 'Oceans 8'));

-- create table producers (
-- id serial primary key,
-- country_id smallint references country(id),
-- producer_name varchar,
-- producer_surname varchar
-- );

-- Insert into producers (country_id, producer_name, producer_surname)
-- values
-- ((select id from country where name = 'USA'), 'Lawrence', 'Bender'),
-- ((select id from country where name = 'UK'), 'Steven', 'Soderbergh'),
-- ((select id from country where name = 'USA'), 'Paul', 'Greengrass')

-- create table movies_producers (
-- id serial primary key,
-- producer_id int references producers(id),
-- movie_id smallint references movie(id)
-- 	);
	
-- insert into movies_producers (producer_id, movie_id) values
-- ((select id from producers where producer_name = 'Lawrence'), (select id from movie where title = 'Good Will Hunting')),
-- ((select id from producers where producer_name = 'Paul'), (select id from movie where title = 'Jason Bourne')),
-- ((select id from producers where producer_name = 'Steven'), (select id from movie where title = 'Oceans 8')),
-- ((select id from producers where producer_name = 'Steven'), (select id from movie where title = 'Oceans Twelve'));


-- movie <-> movies_producers (connected)
-- producers <-> movies_producers (connected)

select movie.title, producers.producer_name, producers.producer_surname
from movie
INNER JOIN movies_producers on movie.id = movies_producers.movie_id
INNER JOIN producers on producers.id = movies_producers.producer_id
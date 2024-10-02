-- DQL: Data Query Language
-- SELECT is the SQL query statement

-- retrieve the full content of the movie table
SELECT *
FROM imdb.movie;

-- retrieve the movies that are produced in '2010'
-- show id, official_title and length in the query result
SELECT id, official_title, length
FROM imdb.movie
WHERE year = '2010';

-- retrieve the movies of 2010 with duration grater than one hour
SELECT id, official_title, length
FROM imdb.movie
WHERE year = '2010' and length > 60;

-- supported logical operators are: AND, OR, NOT
-- A AND B means that both A, B must be true
-- A OR B means that at least A or B must be true
-- NOT A means that the negation of A must be true

-- get the movies where the year is between 2000 and 2010 or the duration is between 60 and 120 minutes
-- use brackets to dpecify the precedence of evaluation among and/or operators
select id, official_title, length, year
FROM imdb.movie
WHERE (year >= '2000' and year <= '2010') or (length >= 60 and length <= 120);
-- the IN operator can be used to enumerate the list of values to consider
-- IN returns true if the attribute value is equal to one of the value in the list
--  WHERE year IN ('200', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010') or (length >= 60 and length <= 120);
-- BETWEEN is an alternative operator to condier an interval of values 
-- WHERE year between '2000' and '2010' or length between 60 and 120;

-- get the movies with title "the man who knew too much"
select *
from imdb.movie
where official_title = 'the man who knew too much';

-- use lower function to reduce a string to lowercase
-- upper function is available for the opposite (convert to uppercase)
select *
from imdb.movie
where lower(official_title) = 'the man who knew too much';

-- retrieve the movies about murder
-- LIKE operator
-- wildcards of like:
-- %: this wildcard represents any string of any length
-- _: this wildcard represents a string of exactly one character
select *
from imdb.movie
where lower(official_title) like '%murder%';

-- get the movies that are not produced in 2010
SELECT id, official_title, year
FROM imdb.movie
WHERE year <> '2010';

-- get the movies where the length or the year are specified (not null)

-- what happens to a movie without values on year with this query?
-- null is not a values and it is not considered in any comparison
SELECT id, official_title, year
FROM imdb.movie
WHERE year <> '2010';

-- get the movies without value on year
SELECT id, official_title, year
FROM imdb.movie
WHERE year is null;

-- get the movies with value on year
SELECT id, official_title, year
FROM imdb.movie
WHERE year is not null;

-- consider this operation
insert into imdb.movie(id, official_title, year, length) values ('383838', '', '2010', 67);
insert into imdb.movie(id, official_title, year, length) values ('438474', '    ', '2010', 67);
-- possible errors:
-- id duplication

-- get the movies with empty/blank values in title
-- TRIM drops heading and trailing blanks in a string
SELECT *
FROM imdb.movie
WHERE trim(official_title) = '';

-- get the persons that are alive
select id as "id code", given_name as "person name", birth_date "date of birth"
from imdb.person
where "death_date" is null;

-- get the name of persons with birth_date after 1970 and sort the result by birth_date (ascending order) and given_name (descending order) where birth_date is the same
select id, given_name, birth_date
from imdb.person
where birth_date >= '1971-01-01'
-- order by birth_date ASC, given_name DESC
-- alternative syntax:
order by 3, 2 DESC;

-- join operation
-- allow to link records in different tables
-- get the title of movies produced in 90' (1990-1999) that are Thrillers
select *
from imdb.movie, imdb.genre
where movie.id = genre.movie and movie.year between '1990' and '1999' and lower(genre.genre) = 'thriller';

-- alternative syntax
select *
from imdb.movie inner join imdb.genre on movie.id = genre.movie
where movie.year between '1990' and '1999' and lower(genre.genre) = 'thriller';

-- get the title of movies that are thrillers

-- this is the so called cartesian product
select *
from imdb.movie, imdb.genre;

-- this is the the join between movie and genre
-- join condition: movie.id = genre.movie
select id, official_title
from imdb.movie, imdb.genre
where movie.id = genre.movie and genre.genre = 'Thriller';

-- alternative syntax
select id, official_title
from imdb.movie inner join imdb.genre on movie.id = genre.movie
where genre.genre = 'Thriller';

-- focus on the notion of INNER join
-- inner join means that movies (e.g., 0076737) that have no links in table genre are excluded from the result of the join
select *
from imdb.movie inner join imdb.genre on movie.id = genre.movie;

-- get the title of movies with score grater than 8 on a scale of 10
-- DISTINCT eliminates duplicate results from the query
-- select id, official_title, score / scale as "scaled score"
select distinct id, official_title, score/scale as "scaled score"
from imdb.movie, imdb.rating
where movie.id = rating.movie and score > 8 and scale = 10
order by 2 desc;

-- insert one more rating for the movie 0468569
insert into imdb.rating(check_date, source, movie, scale, votes, score) values ('2024-10-02', 'SM', '0468569', 10, 1, 8.4);

-- get only id and official title of movies with rating over 8 on 10
-- use distinct to remove possible duplications
select distinct id, official_title
from imdb.movie, imdb.rating
where movie.id = rating.movie and score > 8 and scale = 10
order by 2 desc;

-- get the movie title and the name of actors and characters involved in movies of 2010 or 2011. Report only actors where the name of the character is specified (not null)
-- primary key of crew: movie, person, p_role
-- is distinct needed? is it possible to have duplicates in the result of this query? no
select distinct movie.id as movie_id, official_title, person.id as person_id, given_name, "character"
from imdb.crew inner join imdb.movie on movie.id = movie inner join imdb.person on crew.person = person.id
where year between '2010' and '2011' and p_role = 'actor' and character is not null;

-- get the countries where thriller movies are produced
select distinct country
from imdb.produced inner join imdb.genre on produced.movie = genre.movie
where genre = 'Thriller';

-- get the code of movies that are produced in USA and FRA: both countries
-- the query asks fro two records of produced: one record about fra, another record about usa, and both about the same movie
-- this is not a correct solution: always empty result
select *
from imdb.produced
where country = 'USA' and country = 'FRA';

-- this is not a correct solution: a movie produced only in fra or in usa is returned in the result
select *
from imdb.produced
where country = 'USA' or country = 'FRA';

-- this is equivalent to the previous one: not a correct solution
select *
from imdb.produced
where country in( 'USA', 'FRA');

-- this is a correct solution
select *
from imdb.produced p_usa inner join imdb.produced p_fra on p_usa.movie = p_fra.movie
where p_usa.country = 'USA' and p_fra.country = 'FRA';


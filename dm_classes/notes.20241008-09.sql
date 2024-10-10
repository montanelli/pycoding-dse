-- get the code of movies that are produced in USA and FRA: both countries
-- the query asks fro two records of produced: one record about fra, another record about usa, and both about the same movie
-- this is a solution based on self-join of the table produced
select *
from imdb.produced p_usa inner join imdb.produced p_fra on p_usa.movie = p_fra.movie
where p_usa.country = 'USA' and p_fra.country = 'FRA';

-- alternative solution based on set operation
-- intersect is a set operation that returns the records that belong to both the queries bound by the intersection
-- constraints: i) the queries to combine must have the same number of attributes in the projection (select), and ii) each attribute in projection must be compatible on domain (data type) with the attribute in the other query in the same position
SELECT movie
from imdb.produced
where country = 'USA'
INTERSECT
SELECT movie
from imdb.produced
where country = 'FRA';

-- same solution with the movie title in the result: join needed
SELECT movie, official_title
from imdb.produced inner join imdb.movie on movie.id = produced.movie
where country = 'USA'
INTERSECT
SELECT movie, official_title
from imdb.produced inner join imdb.movie on movie.id = produced.movie
where country = 'FRA';

-- it is important to keep the key of the movies in the select, otherwise it is possible that different movies with same title produce a false positive in the results
-- in the following example, My Movie is returned by the following query because the movie code is missing in select
-- My Movie is related to different movie codes, and should not be included in result since the two movies are not produced in BOTH USA and FRA
SELECT official_title
from imdb.produced inner join imdb.movie on movie.id = produced.movie
where country = 'USA'
INTERSECT
SELECT official_title
from imdb.produced inner join imdb.movie on movie.id = produced.movie
where country = 'FRA';
-- example
produced
movie  | country
001         USA
002         FRA

movie
id  |  title
001     My Movie       2024
002     My Movie       1936

-- union operation
-- return movies that are produced in at least one country among USA and FRA
-- are movies from both returned? yes
-- are movies from both returned twice? no
-- use UNION ALL to return the records in the intersect twice
SELECT movie, official_title
from imdb.produced inner join imdb.movie on movie.id = produced.movie
where country = 'USA'
UNION
SELECT movie, official_title
from imdb.produced inner join imdb.movie on movie.id = produced.movie
where country = 'FRA';

-- this can be written as:
-- without distinct it is equivalent to UNION ALL
SELECT DISTINCT movie, official_title
from imdb.produced inner join imdb.movie on movie.id = produced.movie
where country = 'USA' or country = 'FRA';

-- return the movies that are produced only in USA
SELECT movie, official_title
from imdb.produced inner join imdb.movie on movie.id = produced.movie
where country = 'USA'
EXCEPT
SELECT movie, official_title
from imdb.produced inner join imdb.movie on movie.id = produced.movie
where country <> 'USA';

-- return the movies that are BOTH thriller and horror
SELECT movie
from imdb.genre
where genre = 'Thriller'
INTERSECT
SELECT movie
from imdb.genre
where genre = 'Horror';

-- alternative solution based on the notion of nested query (subquery)
SELECT movie
from imdb.genre
where genre = 'Thriller' and movie in (
    SELECT movie
    from imdb.genre
    where genre = 'Horror'
);

-- return persons that are born and died in the same country
-- solution 1
select person, country
from imdb.location
where d_role = 'B'
INTERSECT
select person, country
from imdb.location
where d_role = 'D';

-- solution 2
select birth.person, birth.country
from imdb.location birth inner join imdb.location death on birth.person = death.person
where birth.country = death.country and birth.d_role = 'B' and death.d_role = 'D';

-- how to check if solution 1 and solution 2 are equivalent
-- exercise: check with set operations

-- other kinds of join
-- consider this join
select *
from imdb.movie inner join imdb.produced ON movie.id = produced.movie;

-- is it possible that a movie is missing in the result of the previous query? yes, when the movie does not have any relation with the records in produced

-- to include movies that are not present in produced (spurious records), use an external/lateral join
-- in this case we use a left join: it is the result of inner + the spurious records of the table on the left side of the join (spurious means records without any link with records with the table on the right
select *
from imdb.movie left join imdb.produced ON movie.id = produced.movie;

-- return the movies without genre
select id
from imdb.movie
where id not in (
    select distinct movie
    from imdb.genre
);

-- alternative
select id
from imdb.movie
except
select movie
from imdb.genre;

-- alternative with left join
select movie.id
from imdb.movie left join imdb.genre on movie.id = genre.movie
where genre.movie is null;

-- this is equivalent to the following
-- right join means that you add the spurious records in the table on the right of the join operation in addtion to the result of the inner join
select movie.id
from imdb.genre right join imdb.movie on movie.id = genre.movie
where genre.movie is null;

-- as a further join operation, we have the full join that means left + right join

-- return the movies that are not rated higher than 8 on 10
-- movies that are never rated over 8 on 10
-- this is not the correct solution since records are considered one by one and the condition asked by the query is about the entire recordset of any movie
select movie.id, movie.official_title, rating.score / rating.scale
from imdb.movie left join imdb.rating on movie.id = rating.movie
where rating.score / rating.scale <= 0.8;

-- correct solution
-- what about the movies without any rating? they should be included
-- rating.movie is null is the condition to include spurious records from movie in the result
select movie.id, movie.official_title
from imdb.movie left join imdb.rating on movie.id = rating.movie
where rating.score / rating.scale <= 0.8 or rating.movie is null
except
select movie.id, movie.official_title
from imdb.movie left join imdb.rating on movie.id = rating.movie
where rating.score / rating.scale > 0.8

movie.id official_title   | rating.movie  rating.scale  rating.score
001         My Movie            001         10                 7
002         My Fav Movie        NULL        NULL                NULL

-- return the movies that are not Thriller
-- what about the movies without genre? they should be included in the result
select movie
from imdb.genre right join imdb.movie on movie.id = genre.movie
where genre <> 'Thriller' or genre.movie is null
except
select movie
from imdb.genre
where genre = 'Thriller';

-- this is ok as well
select id
from imdb.movie
except
select movie
from imdb.genre
where genre = 'Thriller';

-- example
genre.genre genre.movie   |  movie.id
Thriller        001             001
NULL            NULL            002


-- aggregations and aggregate functions
-- MAX, MIN, AVG, SUM, COUNT

-- return the movie with the highest/lowest value of length
select max(length), min(length)
from imdb.movie;

-- return the movie with the highest/lowest value of length considering movies in 2010
select max(length), min(length)
from imdb.movie
where year = '2010'

-- what is the average length of movies in the 90' years
select avg(length)
from imdb.movie
where year between '1990' and '1999';

-- return the overall duration of movies in 2010
select sum(length) as "minutes of show", sum(length)/60 as "hours of show"
from imdb.movie
where year ='2010';

-- count the number of movies in 2010
select count(*)
from imdb.movie
where year = '2010';

-- count the number of persons that are dead
select count(*)
from imdb.person
where death_date is not null;

-- this is equivalent to the previous one
-- count over attribute excludes null values
select count(death_date)
from imdb.person;

-- return the number of persons with unique given_name
-- add distinct to the count operator
select count(distinct given_name), count(*), count(given_name)
from imdb.person

-- for each year, return the max duration
select year, max(length)
from imdb.movie
group by year;

-- return the number of persons working in each movie
select movie,  count(*), count(person), count(distinct person)
from imdb.crew
group by movie;

-- return the number of actors working in each movie
select movie,  count(*), count(person), count(distinct person)
from imdb.crew
where p_role = 'actor'
group by movie;

-- return the average rating for each movie
-- sort result by average in descending order
-- when group by is specified, only attributes in the group by can be projected in the select clause
-- to return the movie title, the join with movie table is needed
select movie, official_title, avg(score/scale)
from imdb.rating inner join imdb.movie on movie.id = rating.movie
group by movie, official_title
order by 3 desc;

-- for each movie, count the involved persons by role
-- sort result by movie
select movie, p_role, count(person)
from imdb.crew
group by movie, p_role
order by 1;

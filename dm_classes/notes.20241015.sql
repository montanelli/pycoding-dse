-- for each movie, count the involved persons by role
-- sort result by movie
select movie, p_role, count(person)
from imdb.crew
group by movie, p_role
order by 1;

-- for each genre, count the number of movies
select genre, count(*), count(movie), count(distinct movie)
from imdb.genre
group by genre.genre;

-- return the countries where more than 10 movies are produced
select country, count(*)
from imdb.produced
group by country
having count(*) > 10;

-- return the countries where more than 10 horror movies are produced
select country, count(produced.movie)
from imdb.produced inner join imdb.genre on produced.movie = genre.movie
where genre = 'Horror'
group by country
having count(*) > 10;

-- return the number of persons born in each country
-- insert a country in the result also when zero persons are born there
-- we need an external join to include spurious countries (countries without born persons)
-- the condition on d_role = 'B' must be contextual to the join (so in from clause), otherwise the effect of external join is canceled and spurious records are eliminated from the result (and countries without born persons are excluded)
select iso3, name, count(*), count(person)
from imdb.country left join imdb.location on country.iso3 = location.country and d_role = 'B'
group by country.iso3, name;

-- return the countries where no person is born (preliminary to solve the preious query)
-- return the countries in the country table that are not belonging to the set of countries in the location table with d_role = 'B'
select iso3
from imdb.country
except
select country
from imdb.location
where d_role = 'B';

-- alternative solution 
select *
from imdb.country left join imdb.location on country.iso3 = location.country and d_role = 'B'
where location.country is null;

-- for each person, count the number of actor presences into movies
select id, given_name, count(crew.person)
from imdb.person left join imdb.crew on person.id = crew.person and p_role = 'actor'
group by id, given_name;

-- alternative
-- cte (common table expression)
-- cte are useful to decompose a complex query in to steps
-- https://www.postgresql.org/docs/current/queries-with.html
-- solve first this problem: find the link between persons and movies
-- then, count the records for each person
with actors as (
select *
from imdb.crew
where p_role = 'actor')
select person.id, given_name, count(actors.person)
from imdb.person left join actors on person.id = actors.person
group by person.id, given_name;

-- find the horror movies that are distributed in Italy and count the number of actors for each of them
-- first, find horror movies
-- then find those distributed in italy
-- then count the actors
with horror_movies as (
    select movie
    from imdb.genre
    where genre = 'Horror'
), horror_italy_movies as (
select released.movie
from imdb.released inner join horror_movies ON released.movie = horror_movies.movie
where country = 'ITA'
)
select crew.movie, count(*)
from imdb.crew inner join horror_italy_movies on crew.movie = horror_italy_movies.movie
where p_role = 'actor'
group by crew.movie;

-- find the movie with the highest/top number of actors
-- first: find the number of actors for each moview
-- then, find the max value on the counters
-- finally, return the movie that has the max value

-- this solution is not correct: we return all the counts, not only the top one
-- we must select only movies with top number of actors (we can have more than one movie with the top value and they must be all returned)
select movie, count(*)
from imdb.crew
where p_role = 'actor'
group by movie
order by 2 desc;

-- this solution is totally wrong: we cannot calculate an aggregate function over another aggregate function
select max(count(*))
from imdb.crew
group by movie;

-- correct solution:
with movie_counts as (
    select movie, count(*) as m_count
    from imdb.crew
    where p_role = 'actor'
    group by movie
), top_count as (
    select max(m_count) as m_top
    from movie_counts
)
select movie_count.*
from movie_counts inner join top_count on m_count = m_top;

-- alternative solution without cte
select movie, count(*) as m_count
from imdb.crew
where p_role = 'actor'
group by movie
having count(*) >= all (
    select count(*) 
    from imdb.crew
    where p_role = 'actor'
    group by movie
);
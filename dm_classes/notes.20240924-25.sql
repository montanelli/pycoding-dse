-- SQL-DDL (data definition language)
-- commands of SQL for creating database structures such as tables
-- examples of table creation in the imdb database
create table imdb.person (
id varchar(10) not null primary key,
bio        text,
birth_date date,
death_date date,
given_name varchar(100) not null
);

create table imdb.movie (
id              varchar(10)  not null primary key,
official_title  varchar(200) not null,
budget          numeric(12,2),
year            char(4),
length          integer check (length > 0),
plot            text
);

-- two different behaviors on foreign keys (fk) for crew.person (cascade) and crew.movie (no action, the default not required to be specified)
-- imdb.person_role is a custom-defined domain/datatype (see below, you can view the specification on datagrip in object types in the imdb database)
create table imdb.crew (
person      varchar(10) not null references person(id) 
    ON UPDATE CASCADE ON DELETE CASCADE,
movie       varchar(10) not null references movie(id) 
    ON UPDATE NO ACTION ON DELETE NO ACTION,
p_role      imdb.person_role not null,
"character" varchar(200),
primary key (person, movie, p_role)
);

create domain imdb.person_role as varchar(10) check (value in ('director', 'writer', 'actor', 'producer'));

-- foreign key crew.person referencing person.id means that:
-- 1. a record in table person exists where the id value corresponds to the crew.person value
-- 2. one and only one record exists in person with the property in 1

-- example of record insert in the crew table
insert into imdb.crew(person, movie, p_role, character) values ('123456', '4758998', 'actor', 'John');
-- example of record insert in the person table
insert into imdb.person(id, given_name) values ('345532', 'Stefano Montanelli');

-- assume that the person.id value in the insert is unique
-- is there a problem with the table crew due to the foreign key on crew.person -> person.id? no

-- examples of record update in the person table
update imdb.person set id = '4534344' where id = '484844';
-- problems?
-- possible duplication of primary key
-- possible violation of foreign key constraint when a referencing record is present in the crew table on the 484844 value
-- no problem is raised if the deleted value (484844) is not referenced in crew

update imdb.person set death_date = now() where id = '484844';

update imdb.person set death_date = now() where given_name = 'Leonardo DiCaprio';

update imdb.person set given_name = 'Antonio DiCaprio' where given_name = 'Leonardo DiCaprio';

-- example of record update in the crew table
update imdb.crew set person = '747885' where movie = '4342323';
-- we are setting up the same person value for a possible large number of crew records about the specified movie
-- possible violation of primary key of crew
-- possible violation of foreign key constraint on person.id

update imdb.crew set movie = person where person = '324353';

-- by default the behavior of the DBMS is that you cannot do operations that violate foreign keys: NO ACTION
-- alternative behavior: the update is propagated to the referenced record: CASCADE

-- assume to have CASCADE on the FK crew.person -> person.id
update imdb.person set id = '345643' where id = '0000138';
-- cascade means that records in other tables with a fk referencing person.id are updated accordingly

-- example of query (we will work on more examples of queries in next classes)
-- I'm looking for records with Leonardo DiCaprio as a given name
SELECT *
FROM imdb.person
WHERE given_name = 'Leonardo DiCaprio';

select *
from imdb.person
where id = '345643';

select *
from imdb.crew
where person = '345643';

-- further examples of update
update imdb.crew set person = '847457' where person = '345643';

-- example of referential integrity with the fk crew.movie (NO ACTION)
update imdb.movie set id = 'ABCD' where id = '235232';

-- example of referential integrity with the fk crew.person (CASCADE)
update imdb.person set id = '748484' where id = '0000138';

-- examples with delete operations considering CASCADE on crew.person and NO ACTION on crew.movie
DELETE FROM imdb.person where id = '234422'; -- the deletion of the record in the movie is always performed. The deletion of records in crew where person has the value '234422' is performed as well due to cascade
DELETE FROM imdb.movie where id = '232422'; -- this is done only if no records of crew contain the value '232422' on crew.movie, otherwise the delete is stopped and an error is raised due to no action

--- more examples with the rating table
create table imdb.rating (
check_date date not null,
source varchar(200) not null,
movie varchar(10)  not null references imdb.movie(id)
    on update cascade on delete cascade,
scale numeric not null,
votes integer not null,
score decimal not null,
primary key (check_date, source, movie),
check ((score >= 0) AND (score <= scale))
);

-- is it possible that the "Corriere della Sera" (a source) rates the movie "Interstellar" (id= 352322) twice? yes (if the value of check_date is different)

update imdb.movie set length = 134 where official_title = 'Interstellar';
-- how many records involved? 0-1-many? potentially many
-- any problem with the update? no
update imdb.movie set id = 'ABCD' where official_title = 'Interstellar';
-- if more than one record has title Interstellar, we have a primary key violation in table movie
-- if the value 'ABCD' already exists in movie, than an error is raised and the update is rejected
-- if exactly one record is found with title Interstellar and ABCD is not used in movie, then everything ok due to CASCADE: possible records in rating that refer to Interstellar are switched to ABCD
delete from imdb.movie where budget > 1000000;
-- potentially, many record can be selected for deletion
-- the command is successfully executed: the possible record in rating that refer to Interstellar are deleted as well (due to CASCADE)
delete from imdb.movie where id = '2354242';
-- 0-1 records involved
-- considering only rating table: the command is successfully executed: the possible record in rating that refer to 2354242 are deleted as well (due to CASCADE)
-- if we consider also the table crew (where the fk crew.movie has NO ACTION) and records are found that refer to 2354242, then the deletion is rejected (nothing is done also in rating)
update imdb.rating set score = score * 1.1 where score < 7;
-- potentially many records involved
-- it is possible that the check score < scale is violated. In this case, what happens? we rollback to the status before the execution of the command
update imdb.rating set movie = '124143' where movie = '532555';
-- we can violate the primary key if a record already exists with movie=124143 and source, check_date with same value of the updated record
-- example:
movie   check_date   source
532555  2020-12-05   Corriere della Sera
124143  2020-12-05   Corriere della Sera
-- the value 124143 must exists in movie.id, otherwise: error
delete from imdb.rating where source = 'Corriere della Sera';
-- problems? no 






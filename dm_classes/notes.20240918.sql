-- In SQL, DDL stands for Data Definition Language

-- SQL-DDL allows to define the structure/schema of tables and related constraints

create table person (
id varchar(10) not null primary key,
bio        text,
birth_date date,
death_date date,
given_name varchar(100) not null
);

create table movie (
id  varchar(10)  not null primary key,
official_title varchar(200) not null,
budget numeric(12, 2),
year char(4) not null,
length integer check (length > 0),
plot text,
unique(official_title, year)
);

create table crew (
person varchar(10) not null references person(id),
movie varchar(10) not null references movie(id),
p_role imdb.person_role not null,
character varchar(200),
primary key (person, movie, p_role)
);

create table genre (
movie varchar(10) not null references movie(id),
genre varchar(20) not null,
primary key(movie, genre)
);

Identification in relationasl databases:
- superkey: any combination of attributes that enforces identification of instances (not possible to have same value on the superkey attributes in two different records of the table)
- key: a minimal superkey 
- primary key: a key without null values. In each table you have one and only one primary key  

Example with table movie(id, official_title, year, budget, length, plot)
superkeys (and K-eys):
- id (K)
- official_title, year (K)
- official_title, length (K)
- official_title, budget (K) 
- official_title, year, length 
- id, official_title 
- id, plot 
- plot, year (K)
- id, official_title, year, budget, length, plot


table genre(movie, genre)
superkeys:
- movie, genre (K) 

table crew(movie, person, p_role, character)
superkeys:
- person, movie, p_role, character (K)
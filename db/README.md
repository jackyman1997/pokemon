# Setting up local MySQL server using HomeBrew
Read [this](https://thoughtbot.com/blog/starting-and-stopping-background-services-with-homebrew). 

## Prep: 
- install `brew`  
- install a SQL 'thing' (like `MySQL WorkBench`, ...)  

## 1. install `brew services` via brew (one-time action)
```
brew tap homebrew/services
```

## 2. install `mysql` via `brew` (one-time action)
```
brew install mysql
```

## 3. start a local `mysql` server
In here, `<name of the service> = mysql`.
```
brew services start <name of the service>
```
or 
```
brew services restart <name of the service>
```
Extra, to check what services are running: 
```
brew services list
```
To stop a service: 
```
brew services stop <name of the service>
```
And, if `mysql` is no long exist but u still want to stop the service: 
```
brew services cleanup
```

## 4. checkout MySQL Workbench to see if the local database is 'connect-able'
it should automatically pop up on the welcoming page

## 5. create database and table using sql in MySQL Workbench
create database: 
``` SQL
-- drop db if it is created before, ensuring good for the next line, can comment this line
DROP DATABASE IF EXISTS MyPokemon;  
-- create db
CREATE DATABASE MyPokemon;
```
create table: 
``` SQL
-- check if the db we r working on exists
USE MyPokemon;

CREATE TABLE pokemon(
    id INT NOT NULL AUTO_INCREMENT, 
    pokedex_id INT NOT NULL, 
    pokemon_name VARCHAR(255) NOT NULL, 
	type_1 VARCHAR(255) NOT NULL,
    type_2 VARCHAR(255) NULL,
    HP INT NOT NULL, 
    Attack INT NOT NULL, 
    Defense	INT NOT NULL, 
    Special_Attack INT NOT NULL, 
    Special_Defense	INT NOT NULL, 
    Speed INT NOT NULL, 
    PRIMARY KEY (id)
);
```

## 6. try insert some data
insert test pokemon: 
``` SQL
INSERT INTO pokemon (pokedex_id, pokemon_name, type_1, type_2, HP, Attack, Defense, Special_Attack, Special_Defense, Speed)
VALUES (0, 'test pokemon', 'fire', Null, 69, 69, 69, 69, 69, 69)

-- or
INSERT INTO pokemon
VALUES (default, 1, 'test pokemon 2', 'water', Null, 666, 666, 666, 666, 666, 666)
```
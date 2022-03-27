-- create database
DROP DATABASE IF EXISTS MY_POKEMON; 
CREATE DATABASE MY_POKEMON; 
DROP DATABASE IF EXISTS RAW_POKEMON; 
CREATE DATABASE RAW_POKEMON; 


-- create tables
USE RAW_POKEMON; 

CREATE TABLE Pokemons(
    id INT NOT NULL AUTO_INCREMENT, 
    pokedex_id INT NOT NULL, 
    pokemon_name VARCHAR(255) NOT NULL, 
    hp INT NOT NULL, 
    attack INT NOT NULL, 
    defense	INT NOT NULL, 
    special_attack INT NOT NULL, 
    special_defense	INT NOT NULL, 
    speed INT NOT NULL, 
	type1 VARCHAR(255) NOT NULL, 
    type2 VARCHAR(255) NULL, 
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
    PRIMARY KEY (id), 
    CONSTRAINT pokemon_id UNIQUE (id, pokedex_id)
);

CREATE TABLE Battles(
    id INT NOT NULL AUTO_INCREMENT, 
    pokemon1 VARCHAR(255) NOT NULL, 
    pokemon2 VARCHAR(255) NOT NULL, 
    outcome INT,  -- if 0, pokemon1 wins, 1 then pokemon2 wins, else are invalid results
    log_url VARCHAR(255) NOT NULL, 
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
    PRIMARY KEY (id) 
);

CREATE TABLE Types_map(
    id INT NOT NULL AUTO_INCREMENT, 
    type_names VARCHAR(255) NOT NULL, 
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
    PRIMARY KEY (id)
);

CREATE TABLE Alias_map(
    id INT NOT NULL AUTO_INCREMENT, 
    name1 VARCHAR(255) NOT NULL, 
    name2 VARCHAR(255) NOT NULL, 
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
    PRIMARY KEY (id) 
);


-- create normalised tables
USE MY_POKEMON; 

CREATE TABLE Types_map(
    id INT NOT NULL AUTO_INCREMENT, 
    type_names VARCHAR(255) NOT NULL, 
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
    PRIMARY KEY (id)
);

CREATE TABLE Pokemons(
    id INT NOT NULL AUTO_INCREMENT, 
    pokedex_id INT NOT NULL, 
    pokemon_name VARCHAR(255) NOT NULL, 
    hp INT NOT NULL, 
    attack INT NOT NULL, 
    defense	INT NOT NULL, 
    special_attack INT NOT NULL, 
    special_defense	INT NOT NULL, 
    speed INT NOT NULL, 
	type1_id INT NOT NULL, 
    type2_id INT NULL, 
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
    PRIMARY KEY (id), 
    FOREIGN KEY (type1_id) REFERENCES MY_POKEMON.Types_map(id), 
    FOREIGN KEY (type2_id) REFERENCES MY_POKEMON.Types_map(id), 
    CONSTRAINT pokemon_id UNIQUE (id, pokedex_id)
);

CREATE TABLE Battles(
    id INT NOT NULL AUTO_INCREMENT, 
    pokemon1_id INT NOT NULL, 
    pokemon2_id INT NOT NULL, 
    outcome INT,  -- if 0, pokemon1 wins, 1 then pokemon2 wins, else are invalid results
    log_url VARCHAR(255) NOT NULL, 
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
    PRIMARY KEY (id), 
    FOREIGN KEY (pokemon1_id) REFERENCES MY_POKEMON.Pokemons(id), 
    FOREIGN KEY (pokemon2_id) REFERENCES MY_POKEMON.Pokemons(id)
);
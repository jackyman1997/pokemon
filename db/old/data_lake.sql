-- act as a data lake
DROP DATABASE IF EXISTS RAW_POKEMON; 
CREATE DATABASE RAW_POKEMON; 

USE RAW_POKEMON;

-- types.json
CREATE TABLE Types(
    id INT NOT NULL AUTO_INCREMENT,
    type_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
); 

-- alias.json
CREATE TABLE Alias(
    id INT NOT NULL AUTO_INCREMENT,
    name1 VARCHAR(255) NOT NULL, 
    name2 VARCHAR(255) NOT NULL, 
    PRIMARY KEY (id)
);

-- match.json
CREATE TABLE Matches(
    id INT NOT NULL AUTO_INCREMENT, 
    pokemon1 VARCHAR(255) NOT NULL, 
    pokemon2 VARCHAR(255) NOT NULL, 
    pokemon1_win BOOLEAN NOT NULL, 
    url VARCHAR(255) NOT NULL, 
    PRIMARY KEY (id)
);

-- data.xlsx
CREATE TABLE Pokemon(
    id INT NOT NULL AUTO_INCREMENT, 
    pokedex_id INT NOT NULL, 
    pokemon_name VARCHAR(255) NOT NULL, 
    type_1 VARCHAR(255) NOT NULL, 
    type_2 VARCHAR(255) NULL, 
    hp INT NOT NULL, 
    attack INT NOT NULL, 
    defense	INT NOT NULL, 
    special_attack INT NOT NULL, 
    special_defense	INT NOT NULL, 
    speed INT NOT NULL, 
    PRIMARY KEY (id)
);

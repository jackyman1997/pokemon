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

CREATE TABLE battle(
    id INT NOT NULL AUTO_INCREMENT, 
    pokemon1 VARCHAR(255) NOT NULL, 
    pokemon2 VARCHAR(255) NOT NULL, 
    pokemon1_win BOOL BOOLEAN NOT NULL, 
    url VARCHAR(255) NOT NULL, 
    PRIMARY KEY (id)
);

-- deal with this later, as form_change = same pokedex_id but different stats or types
-- CREATE TABLE stats(
--     id INT NOT NULL AUTO_INCREMENT, 
--     pokedex_id INT NOT NULL, 
--     HP INT NOT NULL, 
--     Attack INT NOT NULL, 
--     Defense	INT NOT NULL, 
--     Special Attack INT NOT NULL, 
--     Special Defense	INT NOT NULL, 
--     Speed INT NOT NULL, 
--     PRIMARY KEY (id), 
--     FOREIGN KEY (pokedex_id) REFERENCES pokemon(pokedex_id)
-- );

-- CREATE TABLE types(
--     id INT NOT NULL AUTO_INCREMENT, 
--     pokedex_id INT NOT NULL, 
--     type_1 VARCHAR(255) NOT NULL,
--     type_2 VARCHAR(255) NULL,
--     PRIMARY KEY (id), 
--     FOREIGN KEY (pokedex_id) REFERENCES pokemon(pokedex_id)
-- );

-- CREATE TABLE form_change(
--     id INT NOT NULL AUTO_INCREMENT, 
--     pokedex_id INT NOT NULL, 
--     pokemon_name VARCHAR(255) NOT NULL, 
--     PRIMARY KEY (id), 
--     FOREIGN KEY (pokedex_id) REFERENCES pokemon(pokedex_id)
-- );




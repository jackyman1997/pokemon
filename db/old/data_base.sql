-- for all normalised data, transformed from raw data
DROP DATABASE IF EXISTS MY_POKEMON; 
CREATE DATABASE MY_POKEMON; 

USE MY_POKEMON;

CREATE TABLE pokemon(
    id INT NOT NULL AUTO_INCREMENT, 
    pokedex_id INT NOT NULL, 
    pokemon_name VARCHAR(255) NOT NULL, 
    HP INT NOT NULL, 
    Attack INT NOT NULL, 
    Defense	INT NOT NULL, 
    Special_Attack INT NOT NULL, 
    Special_Defense	INT NOT NULL, 
    Speed INT NOT NULL, 
    PRIMARY KEY (id), 
    CONSTRAINT pokemon_id UNIQUE (id, pokedex_id)  -- ???, surrogate vs business key
);

-- Types
CREATE TABLE Types
AS (
	SELECT 
		t1.id,
	-- 	t1.pokedex_id,
	--  t1.pokemon_name,
	-- 	t1.type_1,
	-- 	t2.type_2, 
		t1.type_id_1, 
		t2.type_id_2
	FROM (
		SELECT 
			RAW_POKEMON.pokemon.id AS id, 
	-- 		RAW_POKEMON.pokemon.pokedex_id,
	-- 		RAW_POKEMON.pokemon.pokemon_name,
			RAW_POKEMON.Types.id AS type_id_1, 
			RAW_POKEMON.pokemon.type_1
		FROM RAW_POKEMON.pokemon
		LEFT JOIN RAW_POKEMON.Types 
		ON RAW_POKEMON.Types.type_names = RAW_POKEMON.pokemon.type_1
	) AS t1
	JOIN (
		SELECT 
			RAW_POKEMON.pokemon.id AS id, 
	-- 		RAW_POKEMON.pokemon.pokedex_id,
	-- 		RAW_POKEMON.pokemon.pokemon_name,
			RAW_POKEMON.Types.id AS type_id_2, 
			RAW_POKEMON.pokemon.type_2
		FROM RAW_POKEMON.pokemon
		LEFT JOIN RAW_POKEMON.Types 
		ON RAW_POKEMON.Types.type_names = RAW_POKEMON.pokemon.type_2
	) AS t2
	ON t1.id = t2.id
)

CREATE TABLE battle(
    id INT NOT NULL AUTO_INCREMENT, 
    pokemon1_id INT NOT NULL, 
    pokemon2_id INT NOT NULL, 
    pokemon1_win BOOLEAN NOT NULL, 
    url VARCHAR(255) NOT NULL, 
    PRIMARY KEY (id),
    FOREIGN KEY (pokemon1_id) REFERENCES pokemon(id), 
    FOREIGN KEY (pokemon2_id) REFERENCES pokemon(id)
);

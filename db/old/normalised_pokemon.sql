CREATE TABLE IF NOT EXISTS ttt (
	id INT NOT NULL AUTO_INCREMENT, 
    pokedex_id INT NOT NULL, 
    pokemon_name VARCHAR(255),
    type_id_1 INT NOT NULL, 
    type_id_2 INT NULL,
    hp INT NOT NULL, 
    attack INT NOT NULL, 
    defense INT NOT NULL, 
    special_attack INT NOT NULL, 
    special_defense INT NOT NULL, 
    speed INT NOT NULL, 
    PRIMARY KEY (id) 
-- 	FOREIGN KEY (type_id_1, type_id_2) REFERENCES RAW_POKEMON.Types(id) -- this causes error 3978
) 


AS (
	SELECT 
		RAW_POKEMON.Pokemon.id, 
		RAW_POKEMON.Pokemon.pokedex_id, 
		RAW_POKEMON.Pokemon.pokemon_name,
		type_table.type_id_1, 
		type_table.type_id_2,
		RAW_POKEMON.Pokemon.hp, 
		RAW_POKEMON.Pokemon.attack,
		RAW_POKEMON.Pokemon.defense, 
		RAW_POKEMON.Pokemon.special_attack,
		RAW_POKEMON.Pokemon.special_defense, 
		RAW_POKEMON.Pokemon.speed
	FROM RAW_POKEMON.Pokemon
	JOIN (
		SELECT 
			t1.id,
			-- t1.pokedex_id,
			-- t1.pokemon_name,
			-- t1.type_1,
			-- t2.type_2, 
			t1.type_id_1, 
			t2.type_id_2
		FROM (
			SELECT 
				RAW_POKEMON.pokemon.id AS id, 
				-- RAW_POKEMON.pokemon.pokedex_id,
				-- RAW_POKEMON.pokemon.pokemon_name,
				RAW_POKEMON.Types.id AS type_id_1, 
				RAW_POKEMON.pokemon.type_1
			FROM RAW_POKEMON.pokemon
			LEFT JOIN RAW_POKEMON.Types 
			ON RAW_POKEMON.Types.type_names = RAW_POKEMON.pokemon.type_1
		) AS t1
		JOIN (
			SELECT 
				RAW_POKEMON.pokemon.id AS id, 
				-- RAW_POKEMON.pokemon.pokedex_id,
				-- RAW_POKEMON.pokemon.pokemon_name,
				RAW_POKEMON.Types.id AS type_id_2, 
				RAW_POKEMON.pokemon.type_2
			FROM RAW_POKEMON.pokemon
			LEFT JOIN RAW_POKEMON.Types 
			ON RAW_POKEMON.Types.type_names = RAW_POKEMON.pokemon.type_2
		) AS t2
		ON t1.id = t2.id
	) AS type_table
	ON RAW_POKEMON.Pokemon.id = type_table.id
) 
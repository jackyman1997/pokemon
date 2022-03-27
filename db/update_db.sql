-- update Types_map
INSERT INTO MY_POKEMON.Types_map(
	id, 
	type_names
)
SELECT 
    id, 
    type_names 
FROM RAW_POKEMON.Types_map AS src
ON DUPLICATE KEY UPDATE
    MY_POKEMON.Types_map.id = src.id,
    MY_POKEMON.Types_map.type_names = src.type_names,
    MY_POKEMON.Types_map.modified_date = CURRENT_TIMESTAMP();


-- update pokemon with mapping types_name to type_id
INSERT INTO MY_POKEMON.Pokemons(  
	id,   
    pokedex_id,   
    pokemon_name,   
    hp,   
    attack,   
    defense,   
    special_attack,   
    special_defense,   
    speed,   
    type1_id,   
    type2_id 
) 
SELECT * FROM ( 
	SELECT    
		p.id,    
        p.pokedex_id,    
        p.pokemon_name,    
        p.hp,    
        p.attack,    
        p.defense,    
        p.special_attack,    
        p.special_defense,    
        p.speed,    
        t1.id as type1_id,    
        t2.id as type2_id  
	FROM RAW_POKEMON.Pokemons p  
    JOIN MY_POKEMON.Types_map t1  -- join/inner join here since type1 is a must
    ON p.type1 = t1.type_names  
    LEFT JOIN MY_POKEMON.Types_map t2  -- type2 can be NULL
    ON p.type2 = t2.type_names
) AS src
ON DUPLICATE KEY UPDATE
	MY_POKEMON.Pokemons.id = src.id, 
	MY_POKEMON.Pokemons.pokedex_id = src.pokedex_id, 
	MY_POKEMON.Pokemons.pokemon_name = src.pokemon_name, 
	MY_POKEMON.Pokemons.hp = src.hp, 
	MY_POKEMON.Pokemons.attack = src.attack, 
	MY_POKEMON.Pokemons.defense = src.defense, 
	MY_POKEMON.Pokemons.special_attack = src.special_attack, 
	MY_POKEMON.Pokemons.special_defense = src.special_defense, 
	MY_POKEMON.Pokemons.speed = src.speed, 
	MY_POKEMON.Pokemons.type1_id = src.type1_id, 
	MY_POKEMON.Pokemons.type2_id = src.type2_id,
    MY_POKEMON.Pokemons.modified_date = CURRENT_TIMESTAMP();


-- update battles
INSERT INTO MY_POKEMON.Battles(  
    pokemon1_id, pokemon2_id, outcome, log_url
) 
SELECT 
    src.pokemon1_id, 
    src.pokemon2_id, 
    src.outcome,
    src.log_url
FROM ( 
	SELECT 
		a1.id pokemon1_id, 
		a2.id pokemon2_id, 
		b.outcome outcome,
		b.log_url log_url
	FROM RAW_POKEMON.Battles b
	JOIN RAW_POKEMON.pokemons a1
	ON b.pokemon1 = a1.pokemon_name
	JOIN RAW_POKEMON.pokemons a2
	ON b.pokemon2 = a2.pokemon_name
) AS src
ON DUPLICATE KEY UPDATE 
    MY_POKEMON.Battles.pokemon1_id = src.pokemon1_id, 
    MY_POKEMON.Battles.pokemon2_id = src.pokemon2_id, 
    MY_POKEMON.Battles.outcome = src.outcome,
    MY_POKEMON.Battles.log_url = src.log_url, 
    MY_POKEMON.Battles.modified_date = CURRENT_TIMESTAMP();

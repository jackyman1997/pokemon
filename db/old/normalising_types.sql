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
		RAW_POKEMON.pokemon.pokedex_id,
		RAW_POKEMON.pokemon.pokemon_name,
		RAW_POKEMON.Types.id AS type_id_1, 
		RAW_POKEMON.pokemon.type_1
	FROM RAW_POKEMON.pokemon
	LEFT JOIN RAW_POKEMON.Types 
	ON RAW_POKEMON.Types.type_names = RAW_POKEMON.pokemon.type_1
) AS t1
JOIN (
	SELECT 
		RAW_POKEMON.pokemon.id AS id, 
		RAW_POKEMON.pokemon.pokedex_id,
		RAW_POKEMON.pokemon.pokemon_name,
		RAW_POKEMON.Types.id AS type_id_2, 
		RAW_POKEMON.pokemon.type_2
	FROM RAW_POKEMON.pokemon
	LEFT JOIN RAW_POKEMON.Types 
	ON RAW_POKEMON.Types.type_names = RAW_POKEMON.pokemon.type_2
) AS t2
ON t1.id = t2.id
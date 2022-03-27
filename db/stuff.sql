SELECT t1.pokemon_id, w1+w2 wins, tot1+tot2 total, (w1+w2)/(tot1+tot2) win_rates
FROM (
	SELECT pokemon1 pokemon_id, sum(outcome) as w1, count(*) as tot1 FROM RAW_POKEMON.Battles
	GROUP BY pokemon1
) AS t1
LEFT JOIN (
	SELECT pokemon2 pokemon_id, count(*)-sum(outcome) as w2, count(*) as tot2 FROM RAW_POKEMON.Battles
	GROUP BY pokemon2
) AS t2
ON t1.pokemon_id = t2.pokemon_id; 

CREATE TABLE everything AS
SELECT
	id, pokedex_id, pokemon_name, hp, attack, defense, special_attack, special_defense, speed, type1_id, type2_id, wins, total, win_rates
FROM pokemons_merge_types
LEFT JOIN (
	SELECT t1.pokemon_id pokemon_id, w1+w2 wins, tot1+tot2 total, (w1+w2)/(tot1+tot2) win_rates
	FROM (
		SELECT pokemon1 pokemon_id, sum(outcome) as w1, count(*) as tot1 FROM RAW_POKEMON.Battles
		GROUP BY pokemon1
	) AS t1
	LEFT JOIN (
		SELECT pokemon2 pokemon_id, count(*)-sum(outcome) as w2, count(*) as tot2 FROM RAW_POKEMON.Battles
		GROUP BY pokemon2
	) AS t2
	ON t1.pokemon_id = t2.pokemon_id
) AS src
ON pokemons_merge_types.id = src.pokemon_id; 

SELECT t1.type_id type_id, Types_map.type_names, w1+w2 wins
FROM (
	SELECT type1_id type_id, sum(wins) as w1 FROM everything
	GROUP BY type1_id
) AS t1
LEFT JOIN (
	SELECT type2_id type_id, sum(wins) as w2 FROM everything
	GROUP BY type2_id
) AS t2
ON t1.type_id = t2.type_id
LEFT JOIN RAW_POKEMON.Types_map
ON t1.type_id = Types_map.id
ORDER BY wins DESC; 


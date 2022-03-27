UPDATE RAW_POKEMON.Battles t1
INNER JOIN RAW_POKEMON.Alias_map t2
ON t1.pokemon1 = t2.name2
SET t1.pokemon1 = t2.name1
WHERE t1.id > 0; 

UPDATE RAW_POKEMON.Battles t1
INNER JOIN RAW_POKEMON.Alias_map t2
ON t1.pokemon2 = t2.name2
SET t1.pokemon2 = t2.name1
WHERE t1.id > 0; 

UPDATE RAW_POKEMON.Battles t1
INNER JOIN RAW_POKEMON.Pokemons t2
ON t1.pokemon1 = t2.pokemon_name
SET t1.pokemon1 = t2.id
WHERE t1.id > 0; 

UPDATE RAW_POKEMON.Battles t1
INNER JOIN RAW_POKEMON.Pokemons t2
ON t1.pokemon2 = t2.pokemon_name
SET t1.pokemon2 = t2.id
WHERE t1.id > 0
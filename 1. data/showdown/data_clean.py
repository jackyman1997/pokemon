import requests
import json

# got pokemondb dex
with open('baseStats.json', 'r') as f:
    db = json.load(f)

# get all names
names = [row['Name'].lower() for row in db]

# alias and fanmade 
with open('alias.json', 'r') as f:
    alias_names = json.load(f)

with open('nonofficial_pokemon.json', 'r') as f:
    fanmade_names = json.load(f)

# raw
with open('raw_match_data.json', 'r') as f:
    raw_match = json.load(f)

not_found = []
no_result = []
ok = []
N = len(raw_match)
for idx, match in enumerate(raw_match): 
    if match['pokemon1'] == '-1': 
        not_found.append(match)
    elif match['pokemon1 wins'] == -1 and (match['pokemon1'] != '-1' and match['pokemon2'] != '-1'): 
        no_result.append(match)
    else:
        ok.append(match)
    print(f'{idx+1}/{N} done', end='\r')

print(f'\nok: {len(ok)}\nno pokemon: {len(not_found)}\nno results: {len(no_result)}')

with open('match_no_pks.json', 'w') as f: 
    f.write(json.dumps(not_found, indent=4))

with open('match_no_result.json', 'w') as f: 
    f.write(json.dumps(no_result, indent=4))

with open('match_data.json', 'w') as f: 
    f.write(json.dumps(ok, indent=4))
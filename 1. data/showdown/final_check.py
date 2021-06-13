import requests
import json

# got pokemondb dex
with open('baseStats.json', 'r') as f:
    db = json.load(f)

# get all names
names = [row['Name'].lower() for row in db]

# raw
with open('match_ok.json', 'r') as f:
    data = json.load(f)

N = len(data)
ok = 0
wrong = 0
for idx, item in enumerate(data): 
    pk1 = item['pokemon1']
    pk2 = item['pokemon2']

    if pk1 in names and pk2 in names: 
        ok += 1
    else:
        wrong += 1
    print(f'{idx+1}/{N} done', end='\r')

print(f'\nok: {ok}\nwrong_name: {wrong}')
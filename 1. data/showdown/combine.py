import requests
import json
import pandas as pd

# got pokemondb dex
with open('baseStats.json', 'r') as f:
    db = json.load(f)

for idx, item in enumerate(db): # lower cases
    item['Name'] = item['Name'].lower()
    item['number of battles'] = item.get('number of battles', 0)
    item['number of wins'] = item.get('number of wins', 0)

with open('number_of_battle_raw.json', 'r') as f:
    number_of_battle_raw = json.load(f)

N = len(number_of_battle_raw)
for idx, key_name in enumerate(number_of_battle_raw):

    for item in db:
        if item['Name'] == key_name: 
            item['number of battles'] = number_of_battle_raw[key_name]

    print(f'{idx+1}/{N} done', end='\r')

with open('win_rate_raw.json', 'r') as f:
    win_rate_raw = json.load(f)

M = len(win_rate_raw)
for idx, key_name in enumerate(win_rate_raw):

    for item in db:
        if item['Name'] == key_name: 
            item['number of wins'] = win_rate_raw[key_name]

    print(f'{idx+1}/{M} done', end='\r')

with open('try.json', 'w') as f:
     f.write( json.dumps(db, indent=4) )
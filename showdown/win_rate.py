import requests
import json
import pandas as pd

# got pokemondb dex
with open('baseStats.json', 'r') as f:
    db = json.load(f)

# raw
with open('match_ok.json', 'r') as f:
    data = json.load(f)

N = len(data)
win_rate_raw = {}
number_of_battle_raw = {}
for idx, item in enumerate(data): 

    number_of_battle_raw[item['pokemon1']] = number_of_battle_raw.get(item['pokemon1'], 0) + 1
    number_of_battle_raw[item['pokemon2']] = number_of_battle_raw.get(item['pokemon2'], 0) + 1

    if item['pokemon1 wins'] == 1: 
        win_rate_raw[item['pokemon1']] = win_rate_raw.get(item['pokemon1'], 0) + 1
    if item['pokemon1 wins'] == 0: 
        win_rate_raw[item['pokemon2']] = win_rate_raw.get(item['pokemon2'], 0) + 1

    print(f'{idx+1}/{N} done', end='\r')

with open('win_rate_raw.json', 'w') as f:
    f.write( json.dumps(win_rate_raw, indent=4) )

with open('number_of_battle_raw.json', 'w') as f:
    f.write( json.dumps(number_of_battle_raw, indent=4) )

cnt = 0 
for k in number_of_battle_raw: 
    cnt += number_of_battle_raw[k]

print(cnt)
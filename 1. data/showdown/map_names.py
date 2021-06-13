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
with open('match_data.json', 'r') as f:
    data = json.load(f)

N = len(data)

fanmade = []
wrong_name = []
ok = []

for idx, item in enumerate(data): 
    pk1 = item['pokemon1']
    pk2 = item['pokemon2']

    if pk1 in names and pk2 in names: 
        ok.append(item)
    
    else:
        if pk1 not in names: 
            try: 
                pk1 = alias_names[pk1]
            except: 
                continue

        if pk2 not in names: 
            try: 
                pk2 = alias_names[pk2]
            except: 
                continue

        if pk1 in names and pk2 in names: 
            item['pokemon1'] = pk1
            item['pokemon2'] = pk2
            ok.append(item)
        elif pk1 in fanmade_names.keys() or pk2 in fanmade_names.keys(): 
            fanmade.append(item)
        else:
            wrong_name.append(item)
    
        print(f'{idx+1}/{N} done', end='\r')

print(f'\nok: {len(ok)}\nfanmade: {len(fanmade)}\nwrong_name: {len(wrong_name)}')

with open('match_ok.json', 'w') as f: 
    f.write(json.dumps(ok, indent=4))

with open('match_fanmade.json', 'w') as f: 
    f.write(json.dumps(fanmade, indent=4))

with open('match_wrong_name.json', 'w') as f: 
    f.write(json.dumps(wrong_name, indent=4))
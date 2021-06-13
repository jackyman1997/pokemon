import requests
import json

with open('./data/check_name.json') as f:
    check_name = json.load(f)

with open('baseStats.json', 'r') as f:
    db = json.load(f)
names = [row['Name'].lower() for row in db]

def extract_pokemons2(pks: list) -> list: 
    new = []
    for p in pks:
        terms = p.split('|')
        pkm = [term for term in terms if 'p1a' not in term and 'p2a' not in term and '/' not in term]
        pkm = ''.join(pkm)
        if ',' in pkm:
            pkm = pkm[:pkm.index(',')]
        new.append(pkm.lower())

    return new

find_alias = {}
M = len(check_name)
for idx, item in enumerate(check_name): 
    pks = extract_pokemons2(item['line'])
    for pk in pks:
        if pk not in names: 
            find_alias[pk] = find_alias.get(pk, 0) + 1
    print(f'{idx+1}/{M} done')

with open('./data/find_alias.json', 'w') as f:
    f.write( json.dumps(find_alias, indent=4) )
import requests
import json

with open('./data/check_match2.json') as f:
    check_match2 = json.load(f)

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

def extract_pokemons1(lines: str) -> list: 
    what_pokemons = [line for line in lines.split('\n') if 'switch' in line and ('p1a: ' in line or 'p2a: ' in line)]
    # player 1
    try:
        start = what_pokemons[0].index('p1a')
        pk1 = what_pokemons[0][start:]
    except:
        pk1 = -1
    # player 2
    try:
        start = what_pokemons[1].index('p2a')
        pk2 = what_pokemons[1][start:]
    except:
        pk2 = -1
    # combine and check
    pks = [pk1, pk2]
    if -1 in pks: 
        return -1
    else:
        return pks

M = len(check_match2)
find_alias2 = {}
for idx, item in enumerate(check_match2): 
    log = requests.get(item['url']).text
    pks = extract_pokemons1(log)
    new = extract_pokemons2(pks)
    for pk in new:
        if pk not in names: 
            find_alias2[pk] = find_alias2.get(pk, 0) + 1
    print(f'{idx+1}/{M} done')

with open('./data/find_alias2.json', 'w') as f:
    f.write( json.dumps(find_alias2, indent=4) )
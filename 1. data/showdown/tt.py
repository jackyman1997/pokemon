import requests
import json

with open('1v1_links.json', 'r') as f:
    data = json.load(f)

with open('baseStats.json', 'r') as f:
    db = json.load(f)

names = [row['Name'].lower() for row in db]

def find_loser(lines: str):     
    who_lose = [line for line in lines.split('\n') if 'faint' in line]
    if who_lose == []:
        return -1
    else:
        who_lose = ''.join(who_lose) # convert back to str
        if 'p1a' in who_lose: # if player1 loses, then label 0
            return 0
        elif 'p2a' in who_lose: # if player2 loses, which means player1 wins, then label 1
            return 1
        else: 
            return -1

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

def extract_pokemons2(pks: list) -> list: 
    new = []
    for p in pks:
        terms = p.split('|')
        pkm = [term for term in terms if 'p1a' not in term and 'p2a' not in term and '/' not in term]
        pkm = ''.join(pkm)
        if ',' in pkm:
            pkm = pkm[:pkm.index(',')]
        new.append(pkm.lower())
    print(new)
    return new

useless = []
check_name = []
check_match = []
ok_links = []
N = len(data)
for idx, url in enumerate(data): 
    url += '.log'
    log = requests.get(url).text
    match = {}
    if find_loser(log) != -1:
        if extract_pokemons1(log) != -1:
            full_line = extract_pokemons1(log)
            # for checking db
            for_check = extract_pokemons2(full_line)

            checking = [1 if p in names else 0 for p in for_check]

            if sum(checking) == 2:
                match['pokemon 1'] = for_check[0]
                match['pokemon 2'] = for_check[1]
                match['pokemon 1 wins'] = find_loser(log)
                match['url'] = url
                ok_links.append(match)
            else: 
                match['line'] = full_line
                match['url'] = url
                check_name.append(match)
        else: 
            match['url'] = url
            check_match.append(match)
    else:
        useless.append(url)
    print(f'{idx+1}/{N} done', end='\r')

with open('./data/check_name.json', 'w') as f:
    f.write(json.dumps(check_name, indent=4))

with open('./data/useless.json', 'w') as f:
    f.write(json.dumps(useless, indent=4))

with open('./data/check_match.json', 'w') as f:
    f.write(json.dumps(check_match, indent=4))

with open('./data/ok_links.json', 'w') as f:
    f.write(json.dumps(ok_links, indent=4))

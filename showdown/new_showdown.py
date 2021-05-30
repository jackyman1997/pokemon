import requests
import json

# got links
with open('1v1_links.json', 'r') as f:
    data = json.load(f)

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

# functions 
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
    return new

N = len(data)
raw_match_results = []
raw_match_results_lines = []
for idx, url in enumerate(data): 

    url += '.log'
    log = requests.get(url).text

    # save every match in {}
    match = {}
    match_line = ''

    player1_win = find_loser(log)

    pks_raw_line = extract_pokemons1(log)

    try: 
        pks_list = extract_pokemons2(pks_raw_line)
    except: 
        pks_list = ['-1', '-1']
    
    match['pokemon1'] = pks_list[0]
    match['pokemon2'] = pks_list[1]
    match['pokemon1 wins'] = player1_win
    match['url'] = url
    raw_match_results.append(match)

    match_line = pks_list[0] + ' || ' + pks_list[1] + ' || ' + str(player1_win) + ' || ' + url
    raw_match_results_lines.append(match_line)

    print(f'{idx+1}/{N} done', end='\r')

with open('raw_match_data.json', 'w') as f:
    f.write( json.dumps(raw_match_results, indent=4) )

with open('raw_match_data_line.json', 'w') as f:
    f.write( json.dumps(raw_match_results_lines, indent=4) )
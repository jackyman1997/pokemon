import json
import requests

with open('./data/check_match.json', 'r') as f:
    data = json.load(f)

check_match2 = []
N = len(data)
for idx, line in enumerate(data): 
    lines = requests.get(line['url']).text
    who_lose = [line for line in lines.split('\n') if 'faint' in line]
    what_pokemons = [line for line in lines.split('\n') if 'switch' in line and ('p1a: ' in line or 'p2a: ' in line)]
    
    who_lose = ''.join(who_lose)
    what_pokemons = ''.join(what_pokemons)

    get_in = {'faint': who_lose, 'pks': what_pokemons, 'url': line['url']}
    check_match2.append(get_in)

    print(f'{idx+1}/{N} done', end='\r')


with open('./data/check_match2.json', 'w') as f:
    f.write(json.dumps(check_match2, indent=4))
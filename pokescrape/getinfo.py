import json

with open('./pokedex_links.json', 'r') as f:
    links = json.load(f.read())
print(len(links))
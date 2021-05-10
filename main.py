# libs 
import numpy as np
import pandas as pd
import json

# import my scripts 
from pokemondb.scrape_pokemondb import Pokemon_baseStats
from showdown.scrape_showdown import Pokemon_winRate

# scaping part, I m not running them as they can take upto 2 hrs to finish
Pokemon_baseStats()
# Pokemon_winRate()

# all data required should be in the same directory
# base stats
with open('baseStats.json', 'r') as f:
    pokemonBS = pd.DataFrame( json.load(f) )
    # add 2 more columns for number of battles and number of wins 
    pokemonBS['Number of battles'] = [np.nan] * len(pokemonBS)
    pokemonBS['Number of wins'] = [np.nan] * len(pokemonBS)
# win rate data
with open('wins.json', 'r') as f:
    pokemonWins = json.load(f)

# a simple loop to combine those by matching the pokemon names 
for pokemon_name in pokemonWins: 
    try: # as some of the names in `wins` is not a recognised pokemon (fan-made)
        pokemonBS.loc[ pokemonBS['Name']==pokemon_name, 'Number of battles' ] = len(pokemonWins[pokemon_name])
        pokemonBS.loc[ pokemonBS['Name']==pokemon_name, 'Number of wins' ] = sum(pokemonWins[pokemon_name])
    except: 
        continue

# finally derive the win rates 
pokemonBS['Win rates'] = pokemonBS['Number of wins'] / pokemonBS['Number of battles']

# export to excel 
pokemonBS.to_excel('data.xlsx')
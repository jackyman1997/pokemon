# Pokemon project
I am trying to build an AI-related project on pokemon. Ultimately, a bot that can play pokemon battle and create its own team would be my final target. This requires so much work but let's start small, getting data for pokemons, building simple AI models, then dive deeper. Wish me luck. 

# Why?
I love pokemon, wouldn't it be fun to apply some AI on this game. Just like computers can play chess, I believe they can also enjoy pokemon.  

# Starts small
Gathering pokemon data is the first step. Data from each Pokemon and their match data are mainly what I want.  
Later on a simple regression on win rate again their base-stats can be done, and slow adding in more features (such as types, weaknesses, learned moves, carried item, IVs, EVs, natures ...).  
A pokemon identifier that figure out which pokemon it is from a picture would be a fun practice. Also, the new game `Pokémon Snap` is out. Time to test.  
(ADD MORE...)  
And yes, don't know how many years later, AI learns to play pokemon.

# Pokemon data scraping
Just to scraping data about pokemon first, starting from base-stats and match data from <a href='https://pokemonshowdown.com/'>pokemonshowdown</a>. These will allow me to work out whether there is a relationship between base-stats and winning battles. I will gradually add more data in to see if the model improves.  
Mainly I want myself to get familiarised with what online data about pokemon that I can use and extract. 

# TODO 
- Some of the pokemon names on <a href='https://pokemonshowdown.com/'>pokemonshowdown</a> are not matched to <a href='https://pokemondb.net/'>pokemon db</a> or other api. Need to find a way to generalise them, especially from those with multiple forms.  
- <a href='https://pokemonshowdown.com/'>pokemonshowdown</a> 1v1 data is insufficient  
- Team match data, how to obtain win rate for that?  
- IVs, EVs, natures and other factors that are critical to a pokemon battle, are not added yet.  
- (...)

# useful links 
<a href='https://victoryroadvgc.com/2020/12/08/players-cup-ii-na-results/'>vgc data</a>  
<a href='https://www.pikalytics.com/pokedex/ss'>Pikalytics</a>  
<a href='https://pokemonshowdown.com/'>pokemonshowdown</a>  
try to understand what real and raw data are, can ask the forum people or github owner  
replay may contain data about win rate, and records are save as .txt and .json  
<a href='https://www.pokemon.com/us/pokedex/'>pokedex</a>  
<a href='https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon'>wiki</a>  
<a href='https://bulbapedia.bulbagarden.net/wiki/Stat'>wiki 2</a>  
<a href='https://pokeapi.co/'>pokeapi</a>  
<a href='https://pokemondb.net/'>pokemon db</a>  

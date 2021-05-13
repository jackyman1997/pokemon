# Pokémon project
I am trying to build an AI-related project on Pokémon. Ultimately, a bot that can play Pokémon battle and create its own team would be my final target. This requires so much work but let's start small, getting data for Pokémons, building simple AI models, then dive deeper. Wish me luck. 

# Why?
I love Pokémon, wouldn't it be fun to apply some AI on this game? Just like computers can play chess, I believe they can also enjoy playing Pokémon.  

# Starts small
Gathering Pokémon data is the first step. Data from each Pokémon and their match data are mainly what I want.  
Later on a simple regression on win rate against their base-stats can be done, and slow adding in more features (such as types, weaknesses, learned moves, carried item, IVs, EVs, natures ...).  
A Pokémon identifier that figure out which Pokémon it is from a picture would be a fun practice. Also, the new game `Pokémon Snap` is out. Time to test.  

(ADD MORE...)  
And yes, don't know how many years later, AI learns to play Pokémon.

# 1. Pokémon data scraping for win rate analysis
Just to scraping data about Pokémon first, starting from base-stats from <a href='https://pokemondb.net/'>Pokémon db</a>  and match data from <a href='https://pokemonshowdown.com/'>Pokémonshowdown</a>. These will allow me to work out whether there is a relationship between base-stats and winning battles. I will gradually add more data in to see if the model improves.  
Mainly I want myself to get familiarised with what online data about Pokémon that I can use and extract.  
- most used move/item/Pokémon can also be good attributes for analysing win rate

## why though?
- Higher base stats, better they are
- may answer why are some Pokémon so famous? 
- May be I can figure a generalised strategy for battle 
- A complete data set about each Pokémon is needed for building the Pokémon battle AI
Then Winning analysis is required 

## Data I got now
1. data of each 'specie' of Pokémon, like Base Stats, they are well organised so can be store in a table easily, so data warehouse is a better advance choice  
2. for the links of replays and wins of each Pokémon, they are kinda "first-come-first-in" types of data, which can be quite choatic, so data lake for storage would be better    
3. icons is going into data lake  
4. there are some more data I need to scrape, such as item/move used during battle, even more images of the same 'specie' of Pokémon for later Pokémon identifier  

# TODO 
- Some of the Pokémon names on <a href='https://pokemonshowdown.com/'>Pokémonshowdown</a> are not matched to <a href='https://pokemondb.net/'>Pokémon db</a> or other api. Need to find a way to generalise them, especially from those with multiple forms  
- <a href='https://pokemonshowdown.com/'>Pokémonshowdown</a> 1v1 data is insufficient for some Pokémons (ie no battle data/1 battle only/ban Pokémons)  
- Team match data, how to obtain win rate for that?  (NLP may help reading on those battle.log files)  
- IVs, EVs, natures, abilities and other factors that are critical to a Pokémon battle, are not added yet. (IVs, EVs are natures may not be needed as some of them are randomly assigned by game or have a preset value figured out by exiperienced Pokémon trainers)  
- some more data about the battle, such as number of turns, number of battles that Pokémon has play first, number of times of 'super effective' move played, number of 'support' move used ...  
- a move set database, and which Pokémon can learn them
- abilities database
- items carries/used during battle
- parallelised (?) requests to speed up those 11K links of battle logs requests  
- (...)

# useful links 
<a href='https://victoryroadvgc.com/2020/12/08/players-cup-ii-na-results/'>vgc data</a>  
<a href='https://www.pikalytics.com/pokedex/ss'>Pikalytics</a>  
<a href='https://pokemonshowdown.com/'>Pokémonshowdown</a>  
<a href='https://www.pokemon.com/us/pokedex/'>Pokédex</a>  
<a href='https://pokemonshowdown.com/'>pokemonshowdown</a>  
<a href='https://www.pokemon.com/us/pokedex/'>pokedex</a>  
<a href='https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon'>wiki</a>  
<a href='https://bulbapedia.bulbagarden.net/wiki/Stat'>wiki 2</a>  
<a href='https://pokeapi.co/'>Pokéapi</a>  
<a href='https://pokemondb.net/'>Pokémon db</a>  

# links 
<a href='https://victoryroadvgc.com/2020/12/08/players-cup-ii-na-results/'>vgc data</a>  
<a href='https://www.pokemon.com/us/pokedex/'>pokedex</a>  
<a href='https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon'>wiki</a>
<a href='https://pokeapi.co/'>pokeapi</a>

# what i done
- got a list of pokemon and urls from <a href='https://www.pokemon.com/us/pokedex/'>pokedex</a>  

# TO DO
- try obtain images and use <a href='https://pokeapi.co/'>pokeapi</a> to get more details on each pokemon 
- something about vgc data

# ideas  
currently I don't have a solid direction on ho to apply ai onto this kind of dataset, maybe i can use vgc data to do some sort of prediction. 

# details  
6 stats:  
- HP
- ATK
- DEF
- SP. ATK
- Sp. DEF
- SPD

stats of a pokemon are affected by the followings:  
- base stats (BS)
- IVs 
- EVs
- nature 
- levels (LV) 

For HP:  
<a href="https://www.codecogs.com/eqnedit.php?latex=\text{HP}&space;=&space;\frac{(2&space;\text{BS}&space;&plus;&space;\text{IV}&space;&plus;&space;\frac{EV}{4}))&space;\times&space;\text{LV}}{100}&space;&plus;&space;10&space;&plus;&space;\text{LV}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\text{HP}&space;=&space;\frac{(2&space;\text{BS}&space;&plus;&space;\text{IV}&space;&plus;&space;\frac{EV}{4}))&space;\times&space;\text{LV}}{100}&space;&plus;&space;10&space;&plus;&space;\text{LV}" title="\text{HP} = \frac{(2 \text{BS} + \text{IV} + \frac{EV}{4})) \times \text{LV}}{100} + 10 + \text{LV}" /></a>  
![\text{HP} = \frac{(2 \text{BS} + \text{IV} + \frac{EV}{4})) \times \text{LV}}{100} + 10 + \text{LV}]  
Other stats:  
$ \text{Others} = \big( \frac{(2 \text{BS} + \text{IV} + \frac{EV}{4})) \times \text{LV}}{100} + 5 \big) \times \text{nature} $  
All fraction are rounded to integer (floor function)
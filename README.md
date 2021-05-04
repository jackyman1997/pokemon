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
<img src="https://render.githubusercontent.com/render/math?math=%5Ctext%7BHP%7D%20%3D%20%5Cfrac%7B(2%20%5Ctext%7BBS%7D%20%2B%20%5Ctext%7BIV%7D%20%2B%20%5Cfrac%7BEV%7D%7B4%7D))%20%5Ctimes%20%5Ctext%7BLV%7D%7D%7B100%7D%20%2B%2010%20%2B%20%5Ctext%7BLV%7D">  
![\text{HP} = \frac{(2 \text{BS} + \text{IV} + \frac{EV}{4})) \times \text{LV}}{100} + 10 + \text{LV}]  
Other stats:  
<img src="https://render.githubusercontent.com/render/math?math=%5Ctext%7BOthers%7D%20%3D%20%5Cbig(%20%5Cfrac%7B(2%20%5Ctext%7BBS%7D%20%2B%20%5Ctext%7BIV%7D%20%2B%20%5Cfrac%7BEV%7D%7B4%7D))%20%5Ctimes%20%5Ctext%7BLV%7D%7D%7B100%7D%20%2B%205%20%5Cbig)%20%5Ctimes%20%5Ctext%7Bnature%7D">  
All fraction are rounded to integer (floor function)
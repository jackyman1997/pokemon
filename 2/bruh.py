import requests 
import json 
import time
from selenium import webdriver 
import chromedriver_autoinstaller # https://pypi.org/project/chromedriver-autoinstaller/

url = 'https://pokemondb.net/pokedex/all'

# auto install chromedriver
chromedriver_autoinstaller.install()

# set options for chromedriver
options = webdriver.ChromeOptions()
# sth about handshake and SSL, no ideas, copied from my old projects
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
# maximise windows
options.add_argument("--start-maximized")
# set path to chromedriver.exe
chromedriver_path = '../chromedriver.exe'

# start
driver = webdriver.Chrome(options=options)
driver.get(url)
print('open')
time.sleep(5)
print('have slept')

# find element 
table = driver.find_element_by_tag_name('tbody')

print(table.find_element_by_tag_name('tr').text.split())

# loop to get all pokemons
pokemons = []
rows = table.find_elements_by_tag_name('tr')
for idx, row in enumerate(rows): 
    details = row.text.split()
    pokemon = {}
    pokemon['Id'] = int(details[0])
    pokemon['Name'] = details[1]
    pokemon['TotalBS'] = details[-7]
    pokemon['HP'] = details[-6]
    pokemon['Attack'] = details[-5]
    pokemon['Defense'] = details[-4]
    pokemon['Special Attack'] = details[-3]
    pokemon['Special Defense'] = details[-2]
    pokemon['Speed'] = details[-1]

    pokemons.append(pokemon)

# give json
with open('baseStats.json', 'w') as f:
    f.write(json.dumps(pokemons, indent=4))

driver.close() 
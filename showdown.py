import requests
import json
import time
from selenium import webdriver 
import chromedriver_autoinstaller # https://pypi.org/project/chromedriver-autoinstaller/

url = 'https://pokemonshowdown.com/ladder/gen81v1'

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


table = driver.find_elements_by_tag_name('td')

players = []
for row in table: 
    try: 
        player_name = row.find_element_by_class_name('subtle')
    except: 
        continue
    players.append(player_name.text)

# close
driver.close()

with open('1v1_players.json', 'w') as f:
    f.write( json.dumps(players, indent=4) )
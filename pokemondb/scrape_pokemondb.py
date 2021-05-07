import json 
import time
from selenium import webdriver 
import chromedriver_autoinstaller # https://pypi.org/project/chromedriver-autoinstaller/

class Pokemon_baseStats(): 
    def __init__(self): 
        # webdriver setup
        chromedriver_autoinstaller.install() # auto install chromedriver
        # set options for chromedriver
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors-spki-list') # sth about handshake and SSL, no ideas, copied from my old projects
        self.options.add_argument('--ignore-ssl-errors')
        self.options.add_argument("--start-maximized") # maximise windows
        # set path to chromedriver.exe
        # self.chromedriver_path = '../chromedriver.exe'
        # webdriver start
        self.driver = webdriver.Chrome(options=self.options)
        # json naming 
        self.name_baseStats = 'baseStats.json'
        # runnning 
        self.find_baseStats()

    def find_baseStats(self): 
        url_baseStats = 'https://pokemondb.net/pokedex/all'
        self.driver.get(url_baseStats)
        time.sleep(5)
        # scrape base Stats
        table = self.driver.find_element_by_tag_name('tbody')
        rows = table.find_elements_by_tag_name('tr')
        pokemons = []
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
        # close webdriver
        self.driver.close()
        # save in json
        with open(self.name_baseStats, 'w') as f:
            f.write( json.dumps(pokemons, indent=4) )

# for testing
if __name__ == '__main__': 
    Pokemon_baseStats()
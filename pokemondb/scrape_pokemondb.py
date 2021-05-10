import json 
import time
from selenium import webdriver 
import chromedriver_autoinstaller # https://pypi.org/project/chromedriver-autoinstaller/
import requests
import os

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
        '''
        main scraper script for pokemondb.net
        '''
        # webdriver open
        url_baseStats = 'https://pokemondb.net/pokedex/all'
        self.driver.get(url_baseStats)
        time.sleep(5)
        # get elements for scrape base Stats
        table = self.driver.find_element_by_tag_name('tbody')
        rows = table.find_elements_by_tag_name('tr')
        # loop over the list of webelements (<tr>)
        pokemons = []
        for idx, row in enumerate(rows):
            # use dictionary for each pokemon
            pokemon = {}
            # get text  
            details = row.text.split()
            # pokemon ID
            pokemon['Id'] = int(details[0])
            # pokemon name
            try: # some pokemon may have special names 
                special_name = row.find_element_by_class_name('text-muted').text
                if details[1] in special_name: 
                    pokemon['Name'] = special_name
                else:    
                    pokemon['Name'] = details[1] + '-' + row.find_element_by_class_name('text-muted').text
            except:
                pokemon['Name'] = details[1]
            # pokemon icon
            icon_name = str(pokemon['Id']) + '. ' + pokemon['Name'] # this is for the image file name
            try: # shit happens here, those bastards used different attribute names to link the icons 
                icon_url = row.find_element_by_tag_name('img').get_attribute('src')
            except:
                icon_url = row.find_elements_by_tag_name('span')[1].get_attribute('data-src')
            pokemon['Icon'] = self.dl_img(url=icon_url, name_of_the_img=icon_name) # now we download
            # pokemon type(s)
            pokemon['Type(s)'] = [types.text.split('\n') for types in row.find_elements_by_class_name('cell-icon')][0] # the last [0] is to flatten the list (.split() crates another list within)
            # now all the base stats 
            pokemon['TotalBS'] = details[-7]
            pokemon['HP'] = details[-6]
            pokemon['Attack'] = details[-5]
            pokemon['Defense'] = details[-4]
            pokemon['Special Attack'] = details[-3]
            pokemon['Special Defense'] = details[-2]
            pokemon['Speed'] = details[-1]
            # save in list
            pokemons.append(pokemon)
            # some how many have been done
            print(f'{idx}/{len(rows)} done', end="\r")
        # close webdriver
        self.driver.close()
        # to json
        with open(self.name_baseStats, 'w') as f:
            f.write( json.dumps(pokemons, indent=4) )

    def dl_img(self, url: str, name_of_the_img: str) -> str:
        '''
        just for downloading image and return the directory to the image
        '''
        # need to create an folder to save them 
        folder_name = './pokemon_icons/'
        if not os.path.exists(folder_name): # check if folder exist
            os.makedirs(folder_name) # if not then make one
        # naming and check for window naming rules TODO 
        img_dir = folder_name + name_of_the_img + '.png'
        img_dir = img_dir.replace(':', '')
        # using requests
        with open(img_dir, 'wb+') as pic:
            pic.write( requests.get(url).content )
        return img_dir

    def gimmi_type(self, pokemon_type: int or str) -> str or int:
        '''
        convert type (word) to type (number), and vice versa \n
        for later use
        '''
        self.type_set = {
            'normal': 0, 
            'fire': 1, 
            'water': 2, 
            'electric': 3, 
            'grass': 4, 
            'ice': 5, 
            'fighting': 6, 
            'poison': 7, 
            'ground': 8, 
            'flying': 9, 
            'psychic': 10, 
            'bug': 11, 
            'rock': 12, 
            'ghost': 13, 
            'dragon': 14, 
            'dark': 15, 
            'steel': 16,
            'fairy': 17 
        } 
        if type( pokemon_type ) is str: 
            try: 
                gimmi = self.type_set[pokemon_type.lower()]
            except:
                gimmi = 'this is an imaginary type, not existed in pokemons` world'
        elif type( pokemon_type ) is int: 
            self.type_set_reversed = dict((v,k) for k,v in self.type_set.items()) # reverse keys and values
            try: 
                gimmi = self.type_set_reversed[pokemon_type]
            except: 
                gimmi = 'bro ur number. gimmi int and [0,17]'
        else:
            gimmi = 'I dunno what went wrong but sth is wrong'
        return gimmi

# for testing
if __name__ == '__main__': 
    Pokemon_baseStats()
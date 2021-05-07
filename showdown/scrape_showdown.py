import json 
import time
from selenium import webdriver 
import chromedriver_autoinstaller # https://pypi.org/project/chromedriver-autoinstaller/

url = 'https://pokemonshowdown.com/ladder/gen81v1'
url_1v1_user_table = 'https://pokemonshowdown.com/ladder/gen81v1'

class Pokemon_winRate(): 
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
        self.name_usernames = '1v1_usernames.json'
        # runnning 
        self.find_1v1_usernames()

    def find_1v1_usernames(self): 
        url_1v1_user_table = 'https://pokemonshowdown.com/ladder/gen81v1'
        self.driver.get(url_1v1_user_table)
        time.sleep(5)
        # scrape usernames
        table = self.driver.find_elements_by_tag_name('td')
        players = []
        for row in table: 
            try: 
                player_name = row.find_element_by_class_name('subtle')
            except: 
                continue
            players.append(player_name.text)
        # close webdriver
        self.driver.close()
        # save in json
        with open(self.name_usernames, 'w') as f:
            f.write( json.dumps(players, indent=4) )

# for testing
if __name__ == '__main__': 
    Pokemon_winRate()

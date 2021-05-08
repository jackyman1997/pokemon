import json 
import time
from selenium import webdriver 
import chromedriver_autoinstaller # https://pypi.org/project/chromedriver-autoinstaller/
import requests

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
        # json naming and variables naming 
        self.name_usernames = '1v1_usernames.json'
        self.players = []
        self.name_links = '1v1_links.json'
        self.links = []
        # runnning 
        # self.get_links()
        with open(self.name_links, 'r') as f:
            urls = json.load(f)
        prep_for_win_rate = []
        for url in urls:
            extract_battle_data = self.get_battle_log(url=url)
            prep_for_win_rate.append(extract_battle_data)
        # save
        with open('faint.json', 'w+') as f: 
            f.write( json.dumps(prep_for_win_rate, indent=4) )

    def find_1v1_usernames(self): 
        url_1v1_user_table = 'https://pokemonshowdown.com/ladder/gen81v1'
        # webdriver start
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(url_1v1_user_table)
        time.sleep(5)
        # scrape usernames
        table = self.driver.find_elements_by_tag_name('td')
        for row in table: 
            try: 
                player_name = row.find_element_by_class_name('subtle')
            except: 
                continue
            self.players.append(player_name.text)
        # close webdriver
        self.driver.close()
        # save in json
        with open(self.name_usernames, 'w') as f:
            f.write( json.dumps(self.players, indent=4) )

    def old_get_1v1_links(self): 
        url_search_user = 'https://replay.pokemonshowdown.com/'
        key_words = 'gen81v1'
        # webdriver start
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(url_search_user)
        time.sleep(3)
        # import usernames json or just loop with presaved list of player names
        for name in self.players: 
            # locate elements 
            usernameSearchButton = self.driver.find_element_by_tag_name('button') # the first button is the username Search button
            usernameInput = self.driver.find_element_by_tag_name('input') # the input space is the username Search input space
            usernameInput.clear() # make sure it is empty
            usernameInput.send_keys(name) # send text
            time.sleep(3)
            usernameSearchButton.click() # click search 
            time.sleep(3)
            # now u find all the links 
            list_obj = self.driver.find_element_by_class_name('linklist') # this class name only appears once 
            links_obj = list_obj.find_elements_by_tag_name('li') # they save all links in a list format
            # loop that 
            for link_obj in links_obj:
                try:  
                    link = link_obj.find_element_by_tag_name('a').get_attribute('href')
                    if key_words in link: 
                        self.links.append(link)
                except:
                    continue
        # close webdriver
        self.driver.close()
        # save in json
        with open(self.name_links, 'w') as f:
            f.write( json.dumps(self.link, indent=4) )

    def get_links(self, key_words='gen81v1', max_links=1000): 
        url_search_user = 'https://replay.pokemonshowdown.com/'
        # webdriver start
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(url_search_user)
        time.sleep(3)
        # locate elements 
        format_textbox = self.driver.find_element_by_xpath('/html/body/div[2]/div/form[2]/p/label/input')
        format_search_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/form[2]/p/button')
        # input keys 
        format_textbox.send_keys(key_words) 
        time.sleep(1)
        # click search
        format_search_button.click()
        time.sleep(1)
        # while loop to get links 
        while True:
            # find the more button  
            try: 
                more_button = self.driver.find_element_by_name('moreResults')
                print('more button found')
            except: 
                print('more button not found')
                break
            # find the number of links 
            try: 
                table = self.driver.find_element_by_class_name('linklist')
                links_obj = table.find_elements_by_tag_name('li')
                print('more links found')
                print(len(links_obj))
            except: 
                print('table/links not found')
                break
            # check number of links the webpage has
            if len(links_obj) >= max_links: 
                for link_obj in links_obj: 
                    link = link_obj.find_element_by_tag_name('a').get_attribute('href')
                    self.links.append(link)
                break
            else: # if not, then click more
                more_button.click()
                time.sleep(3)
        # close webdriver
        self.driver.close()
        # save in json
        with open(self.name_links, 'w') as f:
            f.write( json.dumps(self.links, indent=4) )

    def get_battle_log(self, url: str):
        # log in json form in showdown 
        url = url + '.json'
        print(url)
        # try request
        try: 
            battle_data = requests.get(url)  
        except:
            print(f'{url}, link not found')
            return f'{url}, link not found'
        # check response
        if battle_data.status_code == 200: 
            try: 
                # convert into json
                battle_data_dict = json.loads(battle_data.text)
                # get info from log
                battle_log = battle_data_dict['log']
                # find p1_pokemon and p2_pokemon
                p1_index_start = battle_log.find('p1a')
                p2_index_start = battle_log.find('p2a')
                p1_index_end = p1_index_start + battle_log[p1_index_start:].find('\n')
                p2_index_end = p2_index_start + battle_log[p2_index_start:].find('\n')
                p1_info = battle_log[p1_index_start:p1_index_end].split('|')[1]
                p2_info = battle_log[p2_index_start:p2_index_end].split('|')[1]
                if ',' in p1_info:
                    p1_pokemon = p1_info.split(',')[0]
                else:
                    p1_pokemon = p1_info
                if ',' in p2_info:
                    p2_pokemon = p2_info.split(',')[0]
                else:
                    p2_pokemon = p1_info
                # faint
                faint_index_start = battle_log.find('faint')
                faint_index_end = faint_index_start + battle_log[faint_index_start:].find(':')
                which_player_faint = battle_log[faint_index_start:faint_index_end].split('|')[1]
                # save in dict
                battle = {}
                battle['p1a'] = battle.get('p1a', p1_pokemon)
                battle['p2a'] = battle.get('p2a', p2_pokemon)
                battle['faint'] = battle.get('faint', battle[which_player_faint])
                print(battle)
                return battle
            except:
                print(json.loads(battle_data.text)['log'])
                return f"{url}, index fucked, check dict['log']"
        else:
            print(f"{url}, link no response")
            return f"{url}, link no response"

# for testing
if __name__ == '__main__': 
    Pokemon_winRate()

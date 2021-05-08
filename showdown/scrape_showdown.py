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
        # 1v1 keywords
        term_1v1 = ['Challenge Cup 1v1', '1v1', 'gen8cap1v1', 'gen81v1', 'gen71v1', 'gen61v1', 'gen51v1', 'gen41v1', 'gen31v1', 'gen21v1', 'gen11v1']
        for word in term_1v1: 
            self.get_links(key_words=word, max_links=10000)
            print(len(self.links))
        # save in json
        with open(self.name_links, 'w') as f:
            f.write( json.dumps(self.links) )
        # load links json for win counts 
        with open(self.name_links, 'r') as f:
            urls = json.load(f)
        self.prep_for_win_rate = []
        for i, url in enumerate(urls):
            self.prep_for_win_rate.append(self.get_battle_log(url=url))
            print(f'{i}/{len(urls)} done', end="\r")
        # save
        with open('faint.json', 'w+') as f: 
            f.write( json.dumps(self.prep_for_win_rate, indent=4) )
        # calculate win 
        self.wins = {}
        self.count_wins()
        # calculate win rates
        self.winrate = {}
        self.compute_winrate()

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

    def get_links(self, key_words, max_links=10000): 
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
        max_reach = False 
        while not max_reach:
            # find the more button  
            try: 
                more_button = self.driver.find_element_by_name('moreResults')
            except: 
                print('more button not found')
                max_reach = True
            # find the number of links 
            try: 
                table = self.driver.find_element_by_class_name('linklist')
                links_obj = table.find_elements_by_tag_name('li')
                print(f'{len(links_obj)} more links found', end="\r")
            except: 
                print('table/links not found')
                break
            # check number of links the webpage has
            if len(links_obj) >= max_links or max_reach: 
                for link_obj in links_obj: 
                    try: 
                        link = link_obj.find_element_by_tag_name('a').get_attribute('href')
                        self.links.append(link)
                    except:
                        continue
                break
            else: # if not, then click more
                more_button.click()
                time.sleep(3)
        # close webdriver
        self.driver.close()

    def get_battle_log(self, url: str):
        # log in json form in showdown 
        url = url + '.log'
        # try request
        try: 
            battle_data = requests.get(url)  
        except:
            print(f'{url}, link not found')
            pass
        # check response
        if battle_data.status_code == 200: 
            # convert into json
            # battle_data_dict = json.loads(battle_data.text)
            # get info from log
            battle_log = battle_data.text
            # find p1_pokemon and p2_pokemon
            try: # some of the battles are abandoned since start
                player_pokemons = [a for a in battle_log.split('\n') if 'switch' in a]
                player1_pokemon = player_pokemons[0].split('|')[-2].split(',')[0]
                player2_pokemon = player_pokemons[1].split('|')[-2].split(',')[0]
                pokemons = [player1_pokemon, player2_pokemon]
            except: 
                print(f'{url}, match not started')
                pass
            # winning/which faint
            try: # some of the battles are abandoned
                which_faint = [a for a in battle_log.split('\n') if 'faint' in a]
                faint_player = which_faint[0].split('|')[-1].split(':')[0]
                if '1' in faint_player: 
                    win_pokemon, faint_pokemon = pokemons[1], pokemons[0]
                elif '2' in faint_player: 
                    win_pokemon, faint_pokemon = pokemons[0], pokemons[1]
                else:
                    win_pokemon, faint_pokemon = 'nan', 'nan'
            except: 
                faint_pokemon = 'nan'
                win_pokemon = 'nan'
            # save as dictionary
            try: 
                battle = {
                    'pokemon': player1_pokemon, 
                    'against': player2_pokemon, 
                    'wins': win_pokemon, 
                    'lose': faint_pokemon
                    }
                return battle
            except:
                print(f'{url}, sth went wrong')
                pass
        else:
            print(f"{url}, link no response")
            pass

    def count_wins(self): 
        self.data_clean_win_rate = [i for i in self.prep_for_win_rate if i != None and i['wins'] != 'nan']
        # loop
        for i in self.data_clean_win_rate:
            if i['wins'] != 'nan':
                try: 
                    self.wins[i['wins']] = self.wins.get(i['wins'], []) + [1]
                    self.wins[i['lose']] = self.wins.get(i['wins'], []) + [0]
                except:
                    continue 
        # to json
        with open('wins.json', 'w+') as f:
            f.write( json.dumps(self.wins, indent=4) )

    def compute_winrate(self): 
        for i in self.wins:
            self.winrate[i] = sum(self.wins[i])/len(self.wins[i])
        # to json
        with open('winrate.json', 'w+') as f:
            f.write( json.dumps(self.winrate, indent=4) )

# for testing
if __name__ == '__main__': 
    Pokemon_winRate()

import json 
import time
from selenium import webdriver 
import chromedriver_autoinstaller # https://pypi.org/project/chromedriver-autoinstaller/
import requests

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
        # the main loop on scraping links for replays of matches 
        for word in term_1v1: 
            self.get_links(key_words=word, max_links=10000)
            print(len(self.links))
        # save in json
        with open(self.name_links, 'w') as f:
            f.write( json.dumps(self.links) )
        # load the links json back for win counts 
        with open(self.name_links, 'r') as f:
            urls = json.load(f)
        # requests battle log from http://....log
        self.prep_for_win_rate = []
        for i, url in enumerate(urls):
            self.prep_for_win_rate.append(self.get_battle_log(url=url))
            print(f'{i+1}/{len(urls)} done', end="\r") # show how much has been done
        with open('faint.json', 'w+') as f: # save as json
            f.write( json.dumps(self.prep_for_win_rate, indent=4) )
        # calculate win 
        self.wins = {} # calculate win 
        self.count_wins()
        # self.winrate = {} # calculate win rates, not needed here, will do when merge to the main table
        # self.compute_winrate()

    def find_1v1_usernames(self): 
        '''
        an old method used for finding 1v1 players \n
        not needed for now
        '''
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
        '''
        an old method used for finding replay links from each 1v1 player \n
        not needed for now
        '''
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
        '''
        main scraper script for replay.pokemonshowdown.com
        '''
        # webpage link
        url_search_user = 'https://replay.pokemonshowdown.com/'
        # webdriver start
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(url_search_user)
        time.sleep(3)
        # locate elements, here is for the search bar
        format_textbox = self.driver.find_element_by_xpath('/html/body/div[2]/div/form[2]/p/label/input')
        format_search_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/form[2]/p/button')
        # input keys into the search bar
        format_textbox.send_keys(key_words) 
        time.sleep(1)
        # click search
        format_search_button.click()
        time.sleep(1)
        # while loop to get links 
        max_reach = False # a bool to check if the `moreResults` button still appears 
        while not max_reach:
            try: # find the more button  
                more_button = self.driver.find_element_by_name('moreResults')
            except: 
                print('more button not found')
                max_reach = True
            try: # find the links to replays 
                table = self.driver.find_element_by_class_name('linklist')
                links_obj = table.find_elements_by_tag_name('li')
                print(f'on keyword "{key_words}", {len(links_obj)} more links found', end="\r") # just to tell u how much has been done
            except: 
                print('table/links not found')
                break
            # check number of links the webpage has, if more than the `max_links` then stop
            if len(links_obj) >= max_links or max_reach: 
                for link_obj in links_obj: # if stop then start saving those links 
                    try: 
                        link = link_obj.find_element_by_tag_name('a').get_attribute('href')
                        self.links.append(link)
                    except:
                        continue
                break
            else: # if not, then click `moreResults` button
                more_button.click()
                time.sleep(3)
        # close webdriver
        self.driver.close()

    def get_battle_log(self, url: str):
        '''
        replay is saved as a log file \n
        requests.get(them) and extract info from plain text
        ''' 
        url = url + '.log' # log or json form in showdown
        try: # try request
            battle_data = requests.get(url)  
        except:
            print(f'{url}, link not found')
            pass
        if battle_data.status_code == 200: # check response
            battle_log = battle_data.text # get info from log, if json then `battle_data_dict = json.loads(battle_data.text)`
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
                which_faint = [a for a in battle_log.split('\n') if 'faint' in a] # try finding which row of text contains the word 'faint'
                faint_player = which_faint[0].split('|')[-1].split(':')[0] # this wiill give either `p1a` or `p2a`
                # simple logic assigning 
                if '1' in faint_player: 
                    win_pokemon, faint_pokemon = pokemons[1], pokemons[0]
                elif '2' in faint_player: 
                    win_pokemon, faint_pokemon = pokemons[0], pokemons[1]
                else: # if no p1a or p2a, the game is abandoned/never started 
                    win_pokemon, faint_pokemon = 'nan', 'nan'
            except: # or some other error I can`t generalise 
                win_pokemon, faint_pokemon = 'nan', 'nan'
            # save as dictionary with cautious 
            try: 
                battle = {
                    'pokemon': player1_pokemon, 
                    'against': player2_pokemon, 
                    'win': win_pokemon, 
                    'loss': faint_pokemon
                    }
                return battle
            except:
                print(f'{url}, sth went wrong')
                pass
        else:
            print(f"{url}, link no response")
            pass

    def count_wins(self): 
        '''
        just to count number of wins each pokemon has \n
        list of battle log should be in this format: \n
        [{'pokemon': player1_pokemon, \n
         'against': player2_pokemon, \n
         'win': win_pokemon, \n
         'loss': faint_pokemon}, {}, ...] \n 
        '''
        # list comprehension kicking out None or win='nan' elements 
        self.data_clean_win_rate = [i for i in self.prep_for_win_rate if i != None and i['win'] != 'nan']
        # loop for counting wins
        for i in self.data_clean_win_rate:
            if i['win'] != 'nan': # just another check to ensure
                try: # dictionary counting wins by pokemon name in list, 1: win, 0: loss
                    self.wins[i['win']] = self.wins.get(i['win'], []) + [1]
                    self.wins[i['loss']] = self.wins.get(i['win'], []) + [0]
                except:
                    continue 
        # to json
        with open('wins.json', 'w+') as f:
            f.write( json.dumps(self.wins, indent=4) )

    def compute_winrate(self): 
        '''
        just to calculate (number of wins) / (number of matches) 
        '''
        for i in self.wins:
            self.winrate[i] = sum(self.wins[i])/len(self.wins[i])
        # to json
        with open('winrate.json', 'w+') as f:
            f.write( json.dumps(self.winrate, indent=4) )

# for testing
if __name__ == '__main__': 
    Pokemon_winRate()

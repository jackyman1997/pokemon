from selenium import webdriver
import chromedriver_autoinstaller # https://pypi.org/project/chromedriver-autoinstaller/
from selenium.webdriver import ActionChains # to perform click
import time
import json
# import requests
# import os

# url
url = 'https://www.pokemon.com/us/pokedex/'

# auto install chromedriver
# chromedriver_autoinstaller.install()

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
driver = webdriver.Chrome(chromedriver_path, options=options)
driver.get(url)
print('open')
time.sleep(5)
print('have slept')

# scroll forever
no_of_pokemons = 898
while True:
    # try clicking the 'load more' button, if no 'load more' button, then scroll
    try: 
        load_more = driver.find_element_by_xpath('/html/body/div[4]/section[5]/div[2]/a/span')
        ActionChains(driver).click(load_more).perform()
        print('clicked load more')
        time.sleep(2)
    except:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        pass
    # find main element
    main_element = driver.find_element_by_xpath('/html/body/div[4]/section[5]/ul')
    # check len
    pokemons = main_element.find_elements_by_class_name('animating')
    # stop condition 
    if len(pokemons) >= no_of_pokemons:
        print('reached')
        links = {}
        for idx, i in enumerate(pokemons): 
            link = i.find_element_by_tag_name('a').get_attribute('href')
            links[idx+1] = link
        print('append links done')
        break

# output this as json 
with open('pokedex_links.json', 'w+') as f:
    f.write(json.dumps(links, indent=4))
    print('output to json')

# close
driver.close()

# just to check if 898 is the last pokemon
# driver = webdriver.Chrome(chromedriver_path, options=options)
# driver.get(links[-1])
# time.sleep(5)
# driver.close()

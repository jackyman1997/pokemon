import os
import json

def get_data(): 
    folder_path = "./data/"
    basestat_filename = folder_path + "baseStats.json"
    match_filename = folder_path + "match_ok.json"

    with open(folder_path+basestat_filename, 'r') as f: 
import json
import pandas as pd

with open('try.json', 'r') as f:
    data = pd.read_json(f)

data.to_excel('table.xlsx')
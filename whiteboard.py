# WHITEBOARD.PY
'''
'parameters': ['temp', 'precip', 'wind', 'windGust', 'waves', 'windWaves', 'swell1', 'swell2', 'hclouds', 'mclouds', 'lclouds'],
    'levels': ['surface'],
    'key': keys.windy_ApiKey,
    
    'windGust', 'waves', 'windWaves', 'swell1', 'swell2', 'hclouds', 'mclouds', 'lclouds'
 '''   

import requests
import os

# Test basic request
url = 'https://api.windy.com/api/point-forecast/v2'
api_key = 'kyYZ8FTpKtoatC5fqEiiNNiBh1CIY4zW'



r = requests.get(url, api_key)


headers = {
    "lat": '44.50130',
    "lon": '-88.06220',
    "model": 'gfs',
    'parameters': ['temp'],
    'levels': ['surface'],
    'key': "kyYZ8FTpKtoatC5fqEiiNNiBh1CIY4zW",
}


'''
json.loads(r)
csv_file = open('windy_api_pull.csv', 'w')

csv_writer = csv.writer(csv_file)
'''
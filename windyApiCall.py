"""
This is the documentation as it should have been from the Windy.com point-forecast documentation
https://api.wind.com/point-forecast/docs

These notes taken on 2022-09-29 @ 12:39 hours.
This comes from the community forum, g.martins on 2021-04-23 @ 15:19
https://community.windy.com/topic/15423/api-requests-in-python/3

data = {"lat": -39.809,
        "lon": -16.787,
        "model": "gfs",
        "parameters": ["wind"],
        "key": "abcd1234"
        }
header = {"Content-Type" :"application/json"}
s= requests.post("https://api.windy.com/api/point-forecast/v2", json = data, headers = header)
print(s.text)
"""
import requests
import pandas as pd
import json
from tabulate import tabulate
import csv
#import lxml
#import grequests
import datetime
from pprint import pprint

from pandas.io.json import json_normalize

# Read the Manual https://api.windy.com/point-forecast/docs
# Import modules and API Key
url = 'https://api.windy.com/api/point-forecast/v2'
#payload = dict(key1='kyYZ8FTpKtoatC5fqEiiNNiBh1CIY4zW')
# Build a class to make the REST API calls
# Test basic request
data = {
    "lat": 44.50130,
    "lon": -88.06220,
    "model": "gfs",
    "parameters": ["temp", "wind"],
    "levels": ["surface"],
    "key": "kyYZ8FTpKtoatC5fqEiiNNiBh1CIY4zW",
}
header = {"Content-Type" :"application/json"}

## Uncommend these last two rows to do a data pull
r = requests.post(url, json = data, headers = header)
data = r.json()

del data['units']
del data['warning']
#



dump = json.dumps(data)
for key in json.loads(dump):
        print(key)
print("Line 60")


dtg = pd.json_normalize(data, record_path = ['ts']); dtg.rename(columns = {0: 'dtg'}, inplace = True); #print(dtg)

temp = pd.json_normalize(data, record_path = ['temp-surface']); temp.rename(columns = {0: 'temp'}, inplace = True); #print(temp)
wind_speed_we = pd.json_normalize(data, record_path = ['wind_u-surface']); wind_speed_we.rename(columns = {0: 'wind_w-surface'}, inplace = True); #print(wind_speed_we) # wind speed blowing from W to E; neg num from E to W
wind_speed_sn = pd.json_normalize(data, record_path = ['wind_v-surface']); wind_speed_sn.rename(columns = {0: 'wind_s-surface'}, inplace = True); #print(wind_speed_sn) # wind speed blowing from S to N; neg num from N to S


data = {'dtg': dtg,
        'temp': temp,
        'wind_speed_we': wind_speed_we,
        'wind_speed_sn': wind_speed_sn
       }

df = pd.concat(data,
                axis = 1);

print('line 75')
df.columns = ['timestamp', 'surfaceTemp', 'westEastWind', 'southNorthWind']

print(df.keys())
df['timestamp'] = pd.to_datetime(df['timestamp'], format = '%Y%m%d %H:%M:%S', utc = True)
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
print("Line 77")
df.info(verbose=True)

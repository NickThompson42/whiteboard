## python script to merge data sets

import pandas as pd
import numpy as np

# Maritime Traffic data
blackLion = pd.read_csv('C:/Users/NicholasThompson/pythonProjects/dataCleaning/threeBucket/mt_natuna_20220919T135650_maritimeTraffic_sample.csv')
#print(blackLion.head())

blackLion_subset = blackLion[["MMSI","LAT","LON","SPEED","HEADING","TIMESTAMP"]]
blackLion_subset.columns = ["mmsi", "latitude", "longitude", "speed", "heading", "timestamp"]
blackLion_subset['dataSource'] = 'maritimeTraffic'


for col in blackLion_subset.columns:
    print(col)

print("\n")

blackLion_subset.head()

print("\n")

"""
# Spire data
redLion = pd.read_csv('C:/Users/NicholasThompson/pythonProjects/dataCleaning/threeBucket/bquxjob_474ef954_1837a61a5a3_spire-sample.csv')
#print(redLion.head())
redLion_subset = redLion[["MMSI","Latitude","Longitude","Speed","Heading","MovementDateTime"]]
redLion_subset.columns = ["mmsi", "latitude", "longitude", "speed", "heading", "timestamp"]
redLion_subset['dataSource'] = 'spire'

for col in redLion_subset.columns:
    print(col)

print("\n")


# orbComm data
blueLion = pd.read_csv('C:/Users/NicholasThompson/pythonProjects/dataCleaning/threeBucket/bquxjob_42451d86_1837a6b583a_orbComm-stream_sample.csv')
blueLion_subset = blueLion[["mmsi","lat","lon","speed","heading","datetime_UTC"]]
blueLion_subset.columns = ["mmsi", "latitude", "longitude", "speed", "heading", "timestamp"]
blueLion_subset['dataSource'] = 'orbComm'

for col in blueLion_subset.columns:
    print(col)

#print(blueLion.head())


## Preapare BeastKingGoLion for time series normalization

"""

"""
Maritime Traffic {
MMSI, 

--*--IMO, SHIP_ID--*--, 

LAT, LON, SPEED, HEADING, 

--*--COURSE, STATUS--*--, 

TIMESTAMP, 

--*--SHIPNAME, SHIPTYPE, CALLSIGN, FLAG, LENGTH, WIDTH, GRT, DWT, DRAUGHT, YEAR_BUILT, TYPE_NAME, AIS_TYPE_SUMMARY, DESTINATION, ETA--*--

} --> NEW:  {MMSI, LAT, LON, SPEED, HEADING, TIMESTAMP}

Spire {MMSI, Latitude, Longitude, Speed, Heading, _*_ProcessedDate_*_, MovementDateTime} --> NEW: {MMSI, Latitude, Longitude, Speed, Heading, MovementDateTime}
orbComm {mmsi, lat, lon, speed, heading, course, timestamp, datetime_UTC} --> NEW: {mmsi, lat, lon, speed, heading, course, datetime_UTC}
 """



import os
import pandas as pd
import geopandas as gpd
from google.cloud import bigquery

# python -m pip install --upgrade pip
# pip install --upgrade google-cloud
# pip install --upgrade google-cloud-bigquery
# pip install --upgrade google-cloud-storage

from datetime import *
# #C:\Users\MatthewFlure\Documents\RoyceGeo\keen-autumn-333723-828d28598288.json
# CRED = input()
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CRED

gdf = gpd.read_file(input("input Geo File: "))
pulldays = input("Please specify the number of days you would like to pull for (MAX == 365): ")
if int(pulldays) > 365:
    pulldays = "365"
extents = gdf.geometry.bounds
extents = [extents.loc[i, :].values.flatten().tolist() for i in list(range(len(extents)))]
loc = ["POINT ("+str(round((i[0]+i[2])/2,8))+" "+str(round((i[1]+i[3])/2,8))+")" for i in extents]

dfs = []
for ext, cp in zip(extents, loc):
    client = bigquery.Client()
    QUERY = (
        "SELECT * FROM `keen-autumn-333723.ais.ais-spire` WHERE (datetime_utc BETWEEN TIMESTAMP(\""+str(datetime.now() - timedelta(days = int(pulldays)))[:10]+"\") AND TIMESTAMP(\""+str(datetime.now())[:10]+"\")) AND (lon BETWEEN "+str(ext[0])+" AND "+str(ext[2])+") AND (lat BETWEEN "+str(ext[1])+" AND "+str(ext[3])+")")
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish
    mmsi = []
    lat = []
    lon = []
    course = []
    speed = []
    dtglist = []
    for row in rows:
        mmsi.append(row.mmsi)
        lat.append(row.lat)
        lon.append(row.lon)
        course.append(row.course)
        speed.append(row.speed)
        dtglist.append(row.datetime_UTC)
    resultsdf = pd.DataFrame()
    resultsdf["mmsi"] = mmsi
    resultsdf["lat"] = lat
    resultsdf["lon"] = lon
    resultsdf["course"] = course
    resultsdf["speed"] = speed
    resultsdf["datetime_utc"] = dtglist
    resultsdf["datetime_utc"] = resultsdf["datetime_utc"].astype(str)
    resultsdf["datetime_utc"] = resultsdf["datetime_utc"].str[:19]
    resultsdf["datetime_utc"] = pd.to_datetime(resultsdf["datetime_utc"])
    resultsdf = resultsdf.sort_values(by = "datetime_utc", ascending = False).reset_index(drop = True)
    resultsdf["aoi_cp"] = cp
    print(str(len(resultsdf))+" Hits")
    dfs.append(resultsdf)
resultsdf = pd.concat(dfs)
resultsdf.to_csv(str(datetime.now())[:19].replace(" ","T").replace("-","").replace(":","")+"_"+pulldays+"D_spirBQ.csv",index = False)
print("Results Saved to: "+str(datetime.now())[:19].replace(" ","T").replace("-","").replace(":","")+"_"+pulldays+"D_spireBQ.csv")
resultsdf
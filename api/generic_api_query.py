import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon, Point, box
from google.cloud import bigquery
from google.oauth2 import service_account
from datetime import datetime, timedelta

def credentials(file):
    """
    Get credentials for BigQuery

    Args:
        file : str
            Path to credentials json
    Return:
        credentials
            Account credentials to authenticate for BigQuery
    """
    credentials = service_account.Credentials.from_service_account_file(file)
    
    return credentials

def query_client(credentials, project_id):
    """
    Get the client for BigQuery
    
    Args:
        credentials : 
            BigQuery auth credentials
    Return:
        client
            BigQuery client
    """
    
    client = bigquery.Client(credentials=credentials,project=credentials.project_id)
    
    return client

def query_table(client, table_id, query):
    """
    Query a BigQuery table

    Args:
        client : 
            BigQuery client
        table_id : str
            Name of the table to query
        query : str
            SQL query to make to BigQuery
    Return:
        results
            Results of the query
    """
    client.get_table(table_id)
    
    results = client.query(query)
    
    return results

def bigquery_df(results):
    """
    Args:

    Return
        df
            Pandas DataFrame containing data from BigQuery table
    """
    df = results.to_dataframe()

    return df

def bigquery_points_gdf(df, path=None):
    """
    Converts DataFrame from BigQuery to a GeoDataFrame
    """
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat), crs="EPSG:4326")
    
    if path:
        gdf.to_file(path, driver='GeoJSON')
    return gdf

"""TODO: Function to read in Polygon AOI (or make one with list of points) to use for spatial filtering after reading data from BQ"""

if __name__ == '__main__':
    creds_file = 'keen-autumn-333723-ed9fcfc755d3.json'
    project_id = "keen-autumn-333723"
    table_id = "adtech.venntel_data"

    # query = """ SELECT * FROM `keen-autumn-333723.adtech.venntel_data` ORDER BY <field> ASC LIMIT 10 """
    now = datetime.now()
    tdelt = timedelta(days = 30)
    then = (now - tdelt)
    query = f"SELECT * FROM `keen-autumn-333723.ais.orbcomm_stream` WHERE (datetime_UTC BETWEEN TIMESTAMP('{then}') AND TIMESTAMP('{now}')) AND (lon BETWEEN 109.70359835 AND 120.04987867) and (lat BETWEEN 14.07911217 AND 19.30910003)"


    creds = credentials(creds_file)
    client = query_client(creds, project_id)
    results = query_table(client, table_id, query)

    df = bigquery_df(results)

    gdf = bigquery_points_gdf(df)
    print(gdf.iloc[0])
    print(gdf.head())
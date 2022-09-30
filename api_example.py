{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7d2b9695",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import csv\n",
    "import io\n",
    "import urllib.parse\n",
    "import pandas as pd\n",
    "import geopandas as gpd\n",
    "import time as timer\n",
    "from datetime import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eeadbd76",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://services.marinetraffic.com/api/exportvessels/55ae8a2b9c8a8854ae191addb3eb6c2bd96b5fcb%20%20%20%20?v=8\"\n",
    "timespan=2880\n",
    "try:\n",
    "    timespan = \"&timespan=\"+str(int(timespan))\n",
    "except:\n",
    "    timespan = \"&timespan=\"+str(int(round(timespan,0)))\n",
    "MAXLAT=6.2\n",
    "MAXLAT = \"&MAXLAT=\"+str(float(MAXLAT))\n",
    "MINLON=125.0\n",
    "MINLON = \"&MINLON=\"+str(float(MINLON))\n",
    "MAXLON=125.6\n",
    "MAXLON = \"&MAXLON=\"+str(float(MAXLON))\n",
    "MINLAT=5.3\n",
    "MINLAT = \"&MINLAT=\"+str(float(MINLAT))\n",
    "end = \"&protocol=csv&msgtype=extended\"\n",
    "print(url + timespan + MAXLAT + MINLON + MAXLON + MINLAT + end)\n",
    "while(True):\n",
    "    dtstr = str(datetime.utcnow())[:19].replace(\" \",\"T\").replace(\"-\",\"\").replace(\":\",\"\")\n",
    "    try:\n",
    "        with requests.Session() as s:\n",
    "            download = s.get(url + timespan + MAXLAT + MINLON + MAXLON + MINLAT + end)\n",
    "            decoded_content = download.content.decode('utf-8')\n",
    "            df = pd.read_csv(io.StringIO(decoded_content))\n",
    "            df.columns = df.columns.str.replace(' ','')\n",
    "#             cr = csv.reader(decoded_content.splitlines(), delimiter=',')\n",
    "#             my_list = list(cr)\n",
    "#             headers = my_list.pop(0)\n",
    "#             headers = [x.replace(\" \",\"\") for x in headers]\n",
    "#             df = pd.DataFrame(my_list, columns=headers)\n",
    "            df[\"TIMESTAMP\"] = [pd.to_datetime(d) for d in list(df[\"TIMESTAMP\"])]\n",
    "            del df[\"DSRC\"]\n",
    "            del df[\"UTC_SECONDS\"]\n",
    "            del df[\"ROT\"]\n",
    "            print(len(df))\n",
    "    except Exception as e:\n",
    "        print(e)\n",
    "    df.to_csv(\"mt_santos_balut_\"+dtstr+\".csv\", index = False)\n",
    "    print(\"sleeping for 1 Hour\")\n",
    "    timer.sleep(3600)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b1f01b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv(\"mt_n_scs_1426Z.csv\", index = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0542c05",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

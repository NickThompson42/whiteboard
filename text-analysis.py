# Import libraries
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.now()

# URL where the pdfs are located
url = "https://ahec.armywarcollege.edu/CENTCOM-IRAQ-papers/"

# Folder location
folder_location = r"/Users/nthompson/Downloads"
if not os.path.exists(folder_location):os.mkdir("/Users/nthompson/Downloads")

# Requests URL and get response object
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')

"""
# Find all hyperlinks present on webpage
links = soup.find_all('a')

i = 0
"""

print("All complete before the `for` loop. Time now: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


# From all links check for pdf link and
# if present download file
for link in soup.select("a[href$='.pdf']"):
    # Name the pdf files using the last portion of each link which are unique
    filename = os.path.join(folder_location, link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url, link['href'])).content)

   
print("All PDF files downloaded")
print("import successful at ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
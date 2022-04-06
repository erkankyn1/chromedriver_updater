import requests
from lxml import html
import os

# Go to chromedriver main page. 
page = requests.get('https://chromedriver.chromium.org/')
# Get all page content
tree = html.fromstring(page.content)
#This will take "Latest stable release:" row.
page_response = tree.xpath('/html/body/div[1]/div/div[2]/div[3]/div[1]/section[2]/div[2]/div/div/div/div/div/div/div/div/ul[1]/li[2]/p/span[2]/a')
# Get ChromeDriver 10x.xxx.xxx.xx Text
latest_download_link=page_response[0].text
# Split text for get latest version number.
latest_download_link=latest_download_link.split(" ")[1]
# Download zip file for Linux 64
download_zip=requests.get("https://chromedriver.storage.googleapis.com/"+latest_download_link+"/chromedriver_linux64.zip")
# Save the zip file to your local folder. This part is important. Run this project on your local folder for don't stuck at permissions. 
open("chromedriver_linux64.zip","wb").write(download_zip.content)
# Unzip should be installed on your distro. sudo apt install unzip or sudo yum install unzip. 
os.system("unzip chromedriver_linux64.zip && rm chromedriver_linux64.zip")

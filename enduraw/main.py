import requests
from bs4 import BeautifulSoup

# URL de la page à scraper
url = 'https://findmymarathon.com/weather-detail.php?zname=New%20York%20City%20Marathon&year=#google_vignette'  

request_text = requests.get(url).content
page = BeautifulSoup(request_text, "lxml")
print(page)

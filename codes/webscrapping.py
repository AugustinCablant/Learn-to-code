import urllib
import bs4
import pandas
from urllib import request

# page wikipedia de la Ligue 1 de football, millésime 2019-2020 
url_ligue_1 = "https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2019-2020"
request_text = request.urlopen(url_ligue_1).read()
print(type(request_text))
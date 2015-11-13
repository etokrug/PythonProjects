from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup as bs

SUPPRESS = "lxml"
html = urlopen("http://www.pythonscraping.com")
bsObj = bs(html, SUPPRESS)
imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
urlretrieve(imageLocation, "logo.jpg")
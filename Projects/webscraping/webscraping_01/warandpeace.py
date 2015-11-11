from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import *

SUPPRESS_BS4_WARNING = "lxml"
SITE = "http://www.pythonscraping.com/pages/warandpeace.html"
html = urlopen(SITE)
bsObj = bs(html, SUPPRESS_BS4_WARNING)

allText = bsObj.findAll(class_ = "text")

print(allText)

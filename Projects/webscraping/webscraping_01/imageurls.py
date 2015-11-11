from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

SUPPRESS_BS4_WARNING = "lxml"
SITE = "http://www.pythonscraping.com/pages/page3.html"

html = urlopen(SITE)
bsObj = bs(html, SUPPRESS_BS4_WARNING)

images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})

for image in images:
    print(image["src"])
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse, urljoin
import re
import datetime
import random


SUPPRESS_BS4_WARNING = "lxml"
SITE = "http://en.wikipedia.org/"


random.seed(datetime.datetime.now())
def getLinks(article, articleUrl):
    nextURL = urljoin(article, articleUrl)
    html = urlopen(nextURL)
    bsObj = bs(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks(SITE, "/wiki/Kevin_Bacon")

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(SITE, newArticle)






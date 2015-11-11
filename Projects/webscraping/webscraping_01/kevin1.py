from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse, urljoin
import re
import datetime
import random


SUPPRESS_BS4_WARNING = "lxml"
SITE = "http://en.wikipedia.org/"


pages = set()
def getLinks(article, pageUrl):
    global pages
    nextURL = urljoin(article, pageUrl)
    html = urlopen(nextURL)
    bsObj = bs(html)
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError as e:
        print("This page is missing something ain't no thang though...")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #it's a new page
                newPage = link.attrs['href']
                print("------------\n"+newPage)
                pages.add(newPage)
                getLinks(article, newPage)

getLinks(SITE, "/wiki/Kevin_Bacon")

#links = getLinks(SITE, "/wiki/Kevin_Bacon")

"""
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(SITE, newArticle)
"""





from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import *

TEST_SITE = "http://pythonscraping.com/pages/page1.html"
#TEST_SITE = "https://pythonscrapingthisurldoesnotexist.com"
SUPPRESS_BS4_WARNING = "lxml"

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), SUPPRESS_BS4_WARNING)
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle(TEST_SITE)
if title == None:
    print("Title could not be found")
else:
    print(title)

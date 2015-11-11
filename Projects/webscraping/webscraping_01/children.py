from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


SUPPRESS_BS4_WARNING = "lxml"
SITE = "http://www.pythonscraping.com/pages/page3.html"

html = urlopen(SITE)
bsObj = bs(html, SUPPRESS_BS4_WARNING)

for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)

print("\n*****\n")

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
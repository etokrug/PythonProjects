from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs
import re
import random

SUPPRESS_BS_WARNING = 'lxml'
#retrieves all internal links on a page

def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    #finds all links beginning with "/"
    for link in bsObj.findAll("a", href=re.compile("^(\/|.*(http(s).*:\/\/"+includeUrl+")).*")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# Retrieves list of all external links on page
def getExternalLinks(bsObj, url):
    excludeUrl = getDomain(url)
    externalLinks = []
    #finds all links with http/www not containing current URL
    for link in bsObj.findAll("a", href=re.compile("^(http)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None and len(link.attrs['href']) != 0:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getDomain(address):
    return urlparse(address).netloc


def followExternalOnly(bsObj, url):
    externalLinks = getExternalLinks(bsObj, url)
    if len(externalLinks) == 0:
        print("Only internal links here. Try another site")
        internalLinks = getInternalLinks(bsObj, getDomain(url))
        randInternalLink = "http://"+getDomain(url)
        randInternalLink += internalLinks[random.randint(0, len(internalLinks)-1)]
        bsObj = bs(urlopen(randInternalLink), SUPPRESS_BS_WARNING)
        #try again
        followExternalOnly(bsObj, randInternalLink)
    else:
        randomExternal = externalLinks[random.randint(0, len(externalLinks)-1)]
        try:
            nextBsObj = bs(urlopen(randomExternal), SUPPRESS_BS_WARNING)
            print(randomExternal)
            #next page
            followExternalOnly(nextBsObj, randomExternal)
        except HTTPError:
            #try that thang again
            print("Encountered error at "+randomExternal+"! Trying different link.")
            followExternalOnly(bsObj, url)


url = "http://oreilly.com"
#url = "https://www.chromeexperiments.com/globe"
bsObj = bs(urlopen(url), SUPPRESS_BS_WARNING)

followExternalOnly(bsObj, url)
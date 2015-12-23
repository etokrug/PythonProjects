from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import *


testURL = 'http://www.indeed.com/viewjob?jk=d1ba3eb7270f66c4&qd=UrHrZ0Syz3jzOwVwUtxb2aHPy7AUBv6jW-gHawIJGQjzkkU-mtAn7DHAo3RQmMZrkyi7lrPYw6OB4vyKaPQi2zZTlzevP07V0jp5tVM8d5Q2ZvgWAyxRKUrJwfvtF5pCHqeiOfrcDO4wvLXfvaxkxg&atk=1a75ks4sob0djaim&utm_source=publisher&utm_medium=organic_listings&utm_campaign=affiliate'
SUPPRESS_BS4_WARNING = "lxml"


def getJobSummary(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), SUPPRESS_BS4_WARNING)
        summary = bsObj.find("span", {"id":"job_summary"}).get_text()
    except AttributeError as e:
        return None

    return summary

getJobSummary(testURL)
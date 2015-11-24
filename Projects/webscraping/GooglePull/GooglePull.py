from bs4 import BeautifulSoup
from urllib.request import urlopen
import json


def getResults(qString, counter = 0, index = 0):
    counter += 1
    if index > 0:
        start = '&start=%d' % index
    else: start = ''

    key = 'AIzaSyAZGjG38gajQG8Cvr3orfPoqMwnPVjJOy8'
    cseid = '014013134609030703942:ic0zbyqoame'
    url = 'https://www.googleapis.com/customsearch/v1?key={0}&cx={1}&q={2}{3}'\
        .format(key, cseid, qString, start)

    response = urlopen(url).read().decode('utf-8')
    responseJson = json.loads(response)

    index = responseJson.get("queries").get("nextPage")[0].get("startIndex")

    items = responseJson.get("items")

    print(responseJson.get("queries"))
    for i in range(0, len(items)):
        print(items[i].get("formattedUrl"))

    if counter > 5:
        return 0
    else:
        getResults(qString, counter, index)


getResults('test')
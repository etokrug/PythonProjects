from urllib.request import urlopen
import json
from bs4 import BeautifulSoup
from urllib.error import *
import pymysql as p
from datetime import datetime
import sys


conn = p.connect(host='local.dev', user='ScrapingUser', passwd='HappyTime', db='JobSearches', charset='utf8')
cur = conn.cursor()


def getResults(qString, location, index=1, counter=0):
    mainUrl = "http://api.indeed.com/ads/apisearch?"
    publisher = "5400817528818021"
    dataFormat = "json"
    scrubbedLocation = google_url_escaping(location)
    scrubbedQuery = google_url_escaping(qString)
    queryUrl = "{0}publisher={1}&q={2}&l={3}&start={4}&format={5}&v=2".format(
        mainUrl, publisher, scrubbedQuery, scrubbedLocation, index, dataFormat)
    print(queryUrl)
    response = urlopen(queryUrl).read().decode('utf-8')
    responseJson = json.loads(response)

    newIndex = responseJson.get("end")
    total = responseJson.get("totalResults")

    if newIndex >= total:
        print("newIndex: {0} >= total: {1}".format(newIndex, total))
        return 0
    elif counter >= total:
        print("counter: {0} >= total: {1}".format(counter, total))
        return 0
    elif counter >= 990:
        print("Counter: {0} >= 990 - artificial limit reached".format(counter))
        return 0
    else:
        results = responseJson.get("results")
        for i in range(0, len(results)):
            # toPrint = "{0}.) {1}\n{2}".format(index+i, results[i].get("jobtitle"), results[i].get("url"))
            storeJob(qString, results[i], counter)
            counter += 1
            # print(toPrint)
        getResults(qString, location, newIndex, counter)
        return counter


def getJobSummary(url):
    SUPPRESS_BS4_WARNING = "lxml"
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), SUPPRESS_BS4_WARNING)
        summary = bsObj.find("span", {"id":"job_summary"}).get_text()
    except AttributeError as e:
        return ''
    return summary


def google_url_escaping(value):
    returnValue = ""
    for l in value:
        if l in "$-_.+\'!*\"();/?:@=&|,":
            returnValue += ("%" + hex(ord(l))[2:])
        elif l == " ":
            returnValue += '+'
        else:
            returnValue += l
    return returnValue


def storeJob(terms, jsonObj, counter):
    title = ''
    counter += 1
    try:
        search_terms = sqlPrepare(terms)
        title = sqlPrepare(jsonObj.get("jobtitle"))
        company = sqlPrepare(jsonObj.get("company"))
        snippet = sqlPrepare(jsonObj.get("snippet"))
        location = sqlPrepare(jsonObj.get("formattedLocation"))
        # "date" : "Fri, 18 Dec 2015 14:52:19 GMT"
        posting_date = sqlPrepare(datetime.strptime(jsonObj.get("date"), "%a, %d %b %Y %H:%M:%S %Z"))
        indeed_url = sqlPrepare(jsonObj.get("url"))
        job_expired_at_search = jsonObj.get("expired")
        summary = sqlPrepare(getJobSummary(jsonObj.get("url")))
        search_date = sqlPrepare(datetime.now())

        queryString = "INSERT INTO Jobs (search_terms, title, company, snippet, location, posting_date, " \
                      "indeed_url, job_expired_at_search, summary, search_date) " \
                      "VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9});"\
            .format(search_terms, title, company, snippet, location, posting_date, indeed_url,
                    job_expired_at_search, summary, search_date)
        try:
            cur.execute(queryString)
            cur.connection.commit()
        except p.ProgrammingError as e:
            print(e.__traceback__, e.args)
    except:
        print("Unexpected Error: ", sys.exc_info()[0])
        print("Error Dropped Insert")
    finally:
        if title != '':
            print("{0}.) {1}".format(counter, title))



def sqlPrepare(insertObj):
    returnString = str(insertObj)
    returnString = returnString.replace("'", "\\'")
    returnString = returnString.replace("’", "\\'")
    return "'" + returnString + "'"

try:
    q = "junior developer"
    loc = "Portland, OR"
    getResults(q, loc)
finally:
    cur.close()
    conn.close()

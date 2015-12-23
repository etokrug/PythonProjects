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
    # This is the main URL for the indeed.com API Call
    mainUrl = "http://api.indeed.com/ads/apisearch?"
    # This is the key you get when you register with them for API Calls
    publisher = "5400817528818021"
    # Specify data format in JSON because their default is XML (Gross)
    dataFormat = "json"
    # This switches the special chars in the location and query itself to hex chars
    scrubbedLocation = google_url_escaping(location)
    scrubbedQuery = google_url_escaping(qString)
    queryUrl = "{0}publisher={1}&q={2}&l={3}&start={4}&format={5}&v=2".format(
        mainUrl, publisher, scrubbedQuery, scrubbedLocation, index, dataFormat)
    print(queryUrl) # printing for testing
    # Call out to the URL and return the JSON object
    response = urlopen(queryUrl).read().decode('utf-8')
    responseJson = json.loads(response)
    # Grab the next index from the JSON so you know where the next URL should point (paging)
    newIndex = responseJson.get("end")
    # Get the total results for comparison
    total = responseJson.get("totalResults")

    # This can be refactored but I wanted to account for some weird cases quickly
    if newIndex >= total:
        print("newIndex: {0} >= total: {1}".format(newIndex, total))
        return 0
    elif counter >= total:
        print("Counter: {0} >= total: {1}".format(counter, total))
        return 0
    elif counter >= 990:
        # I think the API gets finicky around 1000 returned jobs.
        # Need further testing/research to confirm but I slapped a limit on it just in case.
        print("Counter: {0} >= 990 - artificial limit reached".format(counter))
        return 0
    else:
        # Return the results block from the JSON Obj
        results = responseJson.get("results")
        # Loop through each object in the JSON results obj and store it in the DB
        for i in range(0, len(results)):
            storeJob(qString, results[i], counter)
            # Increase the object counter
            counter += 1
        # Recursively call the getResults function passing the counter in
        getResults(qString, location, newIndex, counter)
        # Return back using counter
        return counter


# Use this to scrape the summary from the Indeed job page.
# I'd break it down but the HTML is not uniform and would be more annoying to parse than it's worth.
def getJobSummary(url):
    # Normally a global var I use to suppress BeautifulSoup's weird warning about using lxml.
    SUPPRESS_BS4_WARNING = "lxml"
    try:
        # Get html object to use in bsObj
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        # Get the bsObj and search it for the job summary indicated by the id job_summary in a span
        bsObj = BeautifulSoup(html.read(), SUPPRESS_BS4_WARNING)
        summary = bsObj.find("span", {"id":"job_summary"}).get_text()
    except AttributeError as e:
        # Instead of returning None return a null string to be plugged
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
    # Need to research specific exceptions I want to handle here
    except:
        print("Unexpected Error: ", sys.exc_info()[0])
        print("Error Dropped Insert")
    finally:
        if title != '':
            print("{0}.) {1}".format(counter, title))


# There are more eloquent ways to do this but needed to get it done
def sqlPrepare(insertObj):
    returnString = str(insertObj)
    returnString = returnString.replace("'", "\\'")
    return "'" + returnString + "'"

try:
    q = "Python Developer"
    loc = "Portland, OR"
    getResults(q, loc)
finally:
    cur.close()
    conn.close()

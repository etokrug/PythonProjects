# GCS Google Custom Search URL Builder
# Currently only a few fields are used in the DB due to resource and knowledge constraints
# More can be added later from the template below
# Current GCS JSON Params: https://developers.google.com/custom-search/json-api/v1/reference/cse/list
# Current GCS REST Params: https://developers.google.com/custom-search/json-api/v1/using_rest
"""
JSON Template:
"template":
    "https://www.googleapis.com/customsearch/v1?
    q={searchTerms}
    &num={count?}
    &start={startIndex?}
    &lr={language?}
    &safe={safe?}
    &cx={cx?}
    &cref={cref?}
    &sort={sort?}
    &filter={filter?}
    &gl={gl?}
    &cr={cr?}
    &googlehost={googleHost?}
    &c2coff={disableCnTwTranslation?}
    &hq={hq?}&hl={hl?}
    &siteSearch={siteSearch?}
    &siteSearchFilter={siteSearchFilter?}
    &exactTerms={exactTerms?}
    &excludeTerms={excludeTerms?}
    &linkSite={linkSite?}
    &orTerms={orTerms?}
    &relatedSite={relatedSite?}
    &dateRestrict={dateRestrict?}
    &lowRange={lowRange?}
    &highRange={highRange?}
    &searchType={searchType}
    &fileType={fileType?}
    &rights={rights?}
    &imgSize={imgSize?}
    &imgType={imgType?}
    &imgColorType={imgColorType?}
    &imgDominantColor={imgDominantColor?}
    &alt=json"
"""

from urllib.request import urlopen
from FindNews.Grab import GCSEnums
import json


class GCSUrlBuilder:
    def __init__(self):
        # TODO: Evaluate using Enum.name for dict keys
        # IMPORTANT: These component keys MUST match their google template counterparts!!!
        self.urlComponents = {
            'mainUrl': "https://www.googleapis.com/customsearch/v1?"
            , 'q': None
            , 'start': None # This is for the start index of the search, not the save()
            # TODO: For Enums: https://developers.google.com/custom-search/docs/xml_results_appendices
            , 'lr': None # TODO: language enum
            , 'cr': None # TODO: country enum # TODO: Add Country To Model
            , 'gl': None # TODO: Enum here - Pushes preferred countries results up.
            , 'googlehost': None # TODO: Enum here
            # TODO: Pull these fields from DB:
            # Search engine - CSE ID
            , 'cx': None # TODO: Pull this from DB - Custom Search ID
            # API Key - your apps API Key
            , 'key': None # TODO: Pull this from DB - API Key
            , 'exactTerms': None
            , 'excludeTerms': None
        }














# Builder Variables



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
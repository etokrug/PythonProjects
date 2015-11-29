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
import json


class GCSUrlBuilder:
    def __init__(self):
        # IMPORTANT: These component keys MUST match their google template counterparts!!!
        self.mainUrl = "https://www.googleapis.com/customsearch/v1?"
        self.urlComponents = {
            'q': None
            , 'start': None # This is for the start index of the search, not the save()
            # TODO: For Enums: https://developers.google.com/custom-search/docs/xml_results_appendices
            # lr: Restricts the search to documents written in a particular language
            , 'lr': None # TODO: language enum
            # cr: Restricts search results to documents originating in a particular country.
            , 'cr': None # TODO: country enum # TODO: Add Country To Model
            # gl: Geolocation of end user. Refers to google_gl in model
            , 'gl': None # TODO: Enum here - Pushes preferred countries results up.
            , 'googlehost': None # TODO: Enum here
            # TODO: Pull these fields from DB:
            # SearchEngines in model: search_api
            , 'cx': None # TODO: Pull this from DB - Custom Search ID
            # API Key - api_key in model
            , 'key': None # TODO: Pull this from DB - API Key
            , 'exactTerms': None
            , 'excludeTerms': None
            , 'dateRestrict': None
            , 'alt': 'json'
            ,
        }

    # TODO: Make sure you account for escape characters in final return
    def return_url(self):
        returnString = self.mainUrl
        for k, v in self.urlComponents.items():
            if v is not None:
                returnString += ('&' + k + "=" + self.google_url_escaping(v))
        return returnString

    def google_url_escaping(self, value):
        returnValue = ""
        for l in value:
            if l in "$-_.+\'!*\"();/?:@=&|":
                returnValue += ("%" + hex(ord(l))[2:])
            else:
                returnValue += l
        returnValue.replace(" ", "+")
        return returnValue


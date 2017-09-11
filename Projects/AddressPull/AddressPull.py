from censusgeocode import CensusGeocode
import csv
import json
import time
import requests


class YaelsGeoz:
    def __init__(self, objid, x, y):
        self.x = x
        self.y = y
        self.objid = objid

        success = False
        barrier = 10
        try:
            while not success:
                try:
                    self.geo = CensusGeocode().coordinates(x, y)

                    self.result_str = self.geo.__str__().replace("'", '"')
                    self.result = json.loads(self.geo.__str__().replace("'", '"'))
                    self.census_tract = self.result[0]['Census Tracts'][0]['BASENAME']
                    success = True
                except KeyError as e:
                    if barrier > 0:
                        print("Error: {0}. Retrying in 2 seconds.".format(e))
                        time.sleep(2)
                        barrier -= 1
                    else:
                        success = True
                        print("Hard Error: {0} - failed too many times".format(e, barrier))
                        self.geo = None
                        self.result = None
                        self.census_tract = None
        except Exception as e:
            print("Hard Error: {0} - Type: {1}".format(e, type(e)))
            self.geo = None
            self.result = None
            self.census_tract = None

    def __str__(self):
        return "{0},{1},{2},{3}".format(self.x, self.y, self.objid, self.census_tract)

    def as_list(self):
        return [self.x, self.y, self.objid, self.census_tract]


class FullAddress:
    def __init__(self, street, city=None, state=None, zipcode=None):
        if city and state:
            self.city_n_stateboi = True
        elif zipcode:
            self.city_n_stateboi = False
        else:
            raise ValueError("Datboi, you gotta have either a zipcode OR a city AND state")
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.base_url = 'https://geocoding.geo.census.gov/geocoder/geographies/address'
        self.format = 'json'
        self.benchmark = 4
        self.vintage = 4
        self.census_tract = None

        if self.city_n_stateboi:
            payload = {'format': self.format, 'street': self.street, 'state': self.state, 'city': self.city,
                       'benchmark': self.benchmark, 'vintage': self.vintage}
        else:
            payload = {'format': self.format, 'street': self.street, 'zip': self.zipcode, 'benchmark': self.benchmark,
                       'vintage': self.vintage}

        success = False
        barrier = 10
        try:
            self.result = requests.get(self.base_url, params=payload).json()
            if self.city_n_stateboi:
                self.zipcode = self.result['result']['addressMatches'][0]['addressComponents']['zip']
            else:
                self.state = self.result['result']['addressMatches'][0]['addressComponents']['state']
                self.city = self.result['result']['addressMatches'][0]['addressComponents']['city']
            self.census_tract = self.result['result']['addressMatches'][0]['geographies']['Census Tracts'][0]['BASENAME']
        except (KeyError, IndexError) as e:
            if barrier > 0:
                print("Error: {0}. Retrying in 2 seconds.".format(e))
                time.sleep(2)
                barrier -= 1
            else:
                success = True
                print("Hard Error: {0} - failed too many times".format(e, barrier))
                self.geo = None
                self.result = None
                self.census_tract = None

    def __str__(self):
        return "{0},{1},{2},{3}{4}".format(self.street, self.city, self.state, self.zipcode, self.census_tract)

    def as_list(self):
        return [self.street, self.city, self.state, self.zipcode, self.census_tract]


def census_tract_run(infile, outfile):
    geoz = []
    count = 1
    with open(infile) as csvfile:
        reader = csv.DictReader(csvfile)
        with open(outfile, 'w') as newfile:
            wr = csv.writer(newfile, quoting=csv.QUOTE_ALL)
            for row in reader:
                # print(row['X'], row['Y'], row['OBJECTID'])
                new_geo = YaelsGeoz(row['X'], row['Y'], row['OBJECTID'])
                geoz.append(new_geo)
                wr.writerow(new_geo.as_list())
                print("{0}.) {1}".format(count, new_geo.__str__()))
                count += 1


def full_address_run(infile, outfile):
    geoz = []
    count = 1
    with open(infile) as csvfile:
        reader = csv.DictReader(csvfile)
        with open(outfile, 'w') as newfile:
            wr = csv.writer(newfile, quoting=csv.QUOTE_ALL)
            for row in reader:
                new_geo = FullAddress(street=row['street'], city=row['city'], state=row['state'])
                geoz.append(new_geo)
                wr.writerow(new_geo.as_list())
                print("{0}.) {1}".format(count, new_geo.__str__()))
                count += 1
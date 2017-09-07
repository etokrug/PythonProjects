from censusgeocode import CensusGeocode
import csv
import json
import time


class YaelsGeoz:
    def __init__(self, x, y, objid):
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

geoz = []
count = 1
with open('property_workup.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with open('output.csv', 'w') as newfile:
        wr = csv.writer(newfile, quoting=csv.QUOTE_ALL)
        for row in reader:
            # print(row['X'], row['Y'], row['OBJECTID'])
            new_geo = YaelsGeoz(row['X'], row['Y'], row['OBJECTID'])
            geoz.append(new_geo)
            wr.writerow(new_geo.as_list())
            print("{0}.) {1}".format(count, new_geo.__str__()))
            count += 1


# for geo in geoz:
#     print(geo)
# cg = CensusGeocode()
#
# result = cg.coordinates(x=-122.6549022, y=45.53956005)
# f = open('info.json', "w")
# f.write(result.__str__())
# f.close()

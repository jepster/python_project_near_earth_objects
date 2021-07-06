import json


with open('data/cad.json') as infile:
    jsonContent = json.load(infile)

    for item in jsonContent['data']:
        found_name = False
        found_date_start = False
        for i in item:
            if type(i) == str and '2002 PB' == i:
                found_name = True
            if type(i) == str and '2000-Jan-01' in i:
                found_date_start = True
            if found_name and found_date_start:
                debug = 1


# this program reads in data from a csv file and outputs each line as a list
# author: gerry callaghan

import csv # to read in csv files
import requests # to download the file from the web
import json # to handle JSON data

FILENAME = 'data.csv'
DATADIR = "../data/"
FULLPATH = DATADIR + FILENAME   

'''
#to determine path is correct
#print(FULLPATH)
'''

'''
#to determine the class
with open(FULLPATH, 'rt') as fp:
    reader = csv.reader(fp, delimiter=",",quoting=csv.QUOTE_NONNUMERIC)
    P
    for line in reader:
        print(f"{type(line)}")
'''    

'''
# to determine that i can remove the header
with open(FULLPATH, 'rt') as fp:
    reader = csv.reader(fp, delimiter=",",quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    for line in reader:
        #print(f"{(line)}")
        if not linecount: # first line is the header
            print(f" {(line)} \n---------")
        else:
            print(f"{(line)}")

        linecount += 1
'''

'''
# now to count the ages
with open(FULLPATH, 'rt') as fp:
    reader = csv.reader(fp, delimiter=",",quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    linecount = 0
    for line in reader:
            if not linecount: # first line is the header  
                print(f" {(line)} \n---------") 
            else:   
                total += int(line[1]) # second column is the age & note that as must make them integers before adding
                # though in my case, by using QUOTE_NONNUMERIC above, they are already floats
            linecount += 1
    print(f"\nThe total age is {total} from {linecount - 1} entries")
'''

'''
# now to ccalculate the average age
with open(FULLPATH, 'rt') as fp:
    reader = csv.reader(fp, delimiter=",",quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    linecount = 0
    for line in reader:
            if not linecount: # first line is the header  
                print(f" {(line)} \n---------") 
            else:   
                total += int(line[1]) # second column is the age & note that as must make them integers before adding
                # though in my case, by using QUOTE_NONNUMERIC above, they are already floats
            linecount += 1
    print(f"\nThe average age is {total / (linecount - 1)}")
'''

'''
# now to read in the file as a Dictionary object
with open(FULLPATH, 'rt') as fp:
    reader = csv.DictReader(fp, delimiter=",",quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    linecount = 0
    for line in reader:
        total += (line["age"]) # we can now use the age as index
       #         # don't need INT because by using QUOTE_NONNUMERIC above, they are already floats
        linecount += 1
    print(f"\nThe average age is {total / (linecount)}") # we don't need -1 here because there is no header row in the data now
'''

# how to import JSON from the internet
# above we have added the import requests to be able to import from the web

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data=response.json() # this converts the JSON to a Python dictionary
#print(f"{type(data)}") # to show that it is a dictionary
print(f"{data}") # to show data

# this makes the data more readable
with open("bank_holidays.json", 'w') as fp: # write the data to a file
    json.dump(data, fp, indent=4) # this writes the dictionary to a file in JSON format
    json_string = json.dumps(data) # this converts the dictionary to a JSON string
    print(f"{(json_string)}") # to show that it is a string

# to access specific data
# it's a dictionary of dictionaries, so we want the first object, Northern Ireland, 
# then within that, the first event, then within that, 
# the title and finally the date on which it occurs
print(f"\nThe first bank holiday in Northern Ireland is: {data['northern-ireland']['events'][0]['title']} on {data['northern-ireland']['events'][0]['date']}")

        
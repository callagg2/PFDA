import csv # to read in csv files
import requests # to download the file from the web
import json # to handle JSON data

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data=response.json() # this converts the JSON to a Python dictionary
#print(f"{type(data)}") # to show that it is a dictionary
#print(f"{data}") # to show data

# this makes the data more readable
with open("bank_holidays.json", 'w') as fp: # write the data to a file
    json.dump(data, fp, indent=4) # this writes the dictionary to a file in JSON format
    json_string = json.dumps(data) # this converts the dictionary to a JSON string
    #print(f"{(json_string)}") # to show that it is a string

# it's a dictionary of dictionaries, so we want the first object, Northern Ireland, 
# we want to print out the bank holidays that happen in Northern Ireland
# The first dictionary has the keys 'england-and-wales', 'scotland' and 'northern-ireland', we want 'northern-ireland'
# The second dictionary has the keys 'division' and 'events', we want 'events', 
# we already know the division is Northern Ireland because we selected it in the first step

print(f"The list of bank holiday in Northern Ireland is as follows:\n")

# if we just want dates
for event in data['northern-ireland']['events']: # so we loop through the list of events under 'northern-ireland'
        print(event['date']) # and print out the title and date of each event
'''
but if we want to print out the title and date of each event, we can do this:
for event in data['northern-ireland']['events']: # so we loop through the list of events under 'northern-ireland'
        print(f"{event['title']} is on {event['date']}") # and print out the title and date of each event

'''


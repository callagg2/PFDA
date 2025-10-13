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
    

print(f"The list of bank holiday in Northern Ireland is as follows:\n")
#for event in data['northern-ireland']['events']: # so we loop through the list of events under 'northern-ireland'
 #       print(f"{event['title']} is on {event['date']}") # and print out the title and date of each event

#print(f"{ ['northern-ireland']['events'][0]}") # to show the list of events:

for event in data['northern-ireland']['events']: # so we loop through the list of events under 'northern-ireland'
        print(event['date']) # and print out the title and date of each event
        #print(f"{data['northern-ireland']['events'][event]['date']}") # to show the date of the first event


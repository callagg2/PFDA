# title: Northern Ireland Holidays
# author: Gerry Callaghan
# this script pulls in a list of UK bank holidays from a URL 
# and prints out the dates of the bank holidays that happen in northern Ireland

import csv # to read in csv files
import requests # to download the file from the web
import json # to handle JSON data


url = "https://www.gov.uk/bank-holidays.json"

response = requests.get(url)

data = response.json() # this converts the JSON response file data to a Python dictionary
#print(f"{type(data)}") # to show that it is a dictionary
#print(f"{data}") # to show data

# the file Data contains a dictionary of dictionaries, so we want the first object, Northern Ireland, 
# we want to print out the bank holidays that happen in Northern Ireland
# The first dictionary has the keys 'england-and-wales', 'scotland' and 'northern-ireland', we want 'northern-ireland'
# The second dictionary has the keys 'division' and 'events', we want 'events', 
# we already know the division is Northern Ireland because we selected it in the first step

print(f"The list of bank holidays in Northern Ireland is as follows:\n")

# if we just want dates
for event in data["northern-ireland"]["events"]: # so we loop through the list of events under 'northern-ireland'
        print(f"{event["date"]}") # and print out the title and date of each event

#but if we want to print out the title and date of each event, we can do this:
print(f"\nThe list of bank holidays in Northern Ireland, along with their titles, is as follows:\n")
for event in data["northern-ireland"]["events"]: # so we loop through the list of events under 'northern-ireland'
        print(f"{event["title"]} is on: \t {event["date"]}") # and print out the title and date of each event



# Finding dates unique to Northern Ireland

# these are just my counter for the while loops for each province 
northern_ireland_day=0
england_and_wales_day = 0
scotland_day=0

# this is an empty array to which i will append the unique dates
unique_days=[]

found = False

# I'm just saying when my counter is less than the total number of elements in the array
while northern_ireland_day < len(data["northern-ireland"]["events"]):
        # I'm just saying when my counter is less than the total number of elements in the array
        while england_and_wales_day < len(data["england-and-wales"]["events"]):
                # if the value at this position in the Nortern ireland array/dictionary equals that of the English and Welsh one
                if data["northern-ireland"]["events"][northern_ireland_day]["date"] == data["england-and-wales"]["events"][england_and_wales_day]["date"]:
                        found = True
                        # to exit the inner while loop i'm setting the england and wales day to the maximum value
                        england_and_wales_day = len(data["england-and-wales"]["events"])
                else:
                        found = False
                        # this will increment the while loop to the next entry in the dictionary object for England and Wales
                        england_and_wales_day = england_and_wales_day +1 
        
        if found == False:
                while scotland_day < len(data["scotland"]["events"]):
                        if data["northern-ireland"]["events"][northern_ireland_day]["date"] == data["scotland"]["events"][scotland_day]["date"]:
                                found = True
                                # to exit the inner while loop i'm setting the scotland day to the maximum value
                                scotland_day = len(data["scotland"]["events"])
                        else:
                                found = False
                                # this will increment the while loop to the next entry in the dictionary object for Scotland        
                                scotland_day = scotland_day +1
                               
        if found == False:
                # so if this Northern Irish date was not found in either the while loops for England, Wales or Scotland add it to an array
                unique_days.append(data["northern-ireland"]["events"][northern_ireland_day]["date"])
        
        # this will increment the while loop to the next entry in the dictionary object for Northern Ireland   
        northern_ireland_day = northern_ireland_day +1
        # This resets the counter for England and Wales day
        england_and_wales_day = 0
        # This resets the counter for Scotland day
        scotland_day = 0
        # this resets the found boolean to false
        found = False   
                          
# print out all the unique dates in the unique dates array
print(f"\nThe list of unique dates to Northern Ireland are:\n {unique_days}")

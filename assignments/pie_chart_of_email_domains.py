# this program takes a pandas dataframe, and creates a piechart of all the data in one column
# author: Gerry Callaghan

# i will using pandas to manipulate my data, numpy for numerical operations, and matplotlib to create the pie chart
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

'''
# # up one levels to root and then down into data
datadir = "../data/"
people_filename = datadir + "people-100.csv"
print(f"{people_filename}")
open(people_filename)
'''
people_filename ="people-100.csv"


# this reads in the data from a csv file into a pandas dataframe
df= pd.read_csv(people_filename)
print(f"{df.head()}")

cleandf= df.fillna(value=' ')

people_df = pd.read_csv(people_filename)

people_df['domain'] = people_df['Email'].str.split('@').str[1]


print(f"{people_df['domain']}")


#unique, counts = np.unique(['domain'], return_counts=True)

# we can now put this into a pie plot
# https://www.analyticsvidhya.com/blog/2024/02/pie-chart-matplotlib/
plt.pie(people_df['domain'].value_counts(), labels=people_df['domain'].unique(), autopct='%1.1f%%')

plt.savefig("pie-chart of email domains.png")

plt.show()

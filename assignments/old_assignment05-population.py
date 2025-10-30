#this looks at calculating the weighted standard deviation of a data set

import pandas as pd
import numpy as np  

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FY006A/CSV/1.0/en"


# read in the data from the csv file
df = pd.read_csv(url)

print(f"{df.tail()}\n")


'''
# i could save the data locally and read it in from there as follows
FILENAME = "population_for_analysis.csv"
DATADIR = "./"
FULLPATH = DATADIR + FILENAME
'''

# remove some of the superfluous columns
df= df[df["Sex"]!= "Female"]
df= df[df["Sex"]!= "Male"]
print(f"{df.tail()}\n")

headers = df.columns.tolist()
print(f"{headers}\n")

drop_col_list = ["STATISTIC","Statistic Label","TLIST(A1)","CensusYear","C02199V02655","Sex","C02076V03371","C03789V04537", "UNIT"]
df.drop(columns=drop_col_list, inplace=True)
headers = df.columns.tolist()
print(f"{headers}\n")

print(f"{df.head(3)}\n")   

print(f"{df[df["Single Year of Age"] != "All ages"]}\n") 
df = df[df["Single Year of Age"] != "All ages"]
df["Single Year of Age"] = df["Single Year of Age"].str.replace("Under 1 year","0")
df["Single Year of Age"] = df["Single Year of Age"].str.replace("\D", "", regex=True)
df["Single Year of Age"] = df["Single Year of Age"].astype("Int64")
df["VALUE"] = df["VALUE"].astype("Int64")
print(f"{df.head()}\n")

print(f"{df.info()}\n")

df_analysis = pd.pivot_table(df,"VALUE", "Single Year of Age", "Administrative Counties")
print(f"{df_analysis.head(3)}\n")
#print(f"{df_analysis.info()}\n")
df_analysis.to_csv("population_for_analysis2.csv")   


headers = list(df_analysis.columns)[0:]
print(f"{headers}\n") 
#print (df[headers[0]].mean)

district = headers[0]
print(f"{district}\n")

# weighted mean
# weighted mean is sum (age * population at age) / (populations at age)

number_people = df_analysis[district].sum()
print(f"{number_people}\n")

# notice where the .sum() is place, it is outside the parentheses of Age * population
# this should work except Pandas has meade the age the index because it goes from 0 to 100
#cumulative_age = (df_analysis["Single Year of Age"]*df_analysis[district]).sum()
#print(f"{cumulative_age}\n")
#so we needed to search the internet for multiplying index by column in pandas
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mul.html
# DataFrame.mul(other, axis='columns', level=None, fill_value=None)
cumulative_age  = (df_analysis[district].mul(df_analysis.index, axis=0)).sum()
print(f"{cumulative_age}\n")

# now to get the weighted mean
weighted_mean = cumulative_age/number_people
print(f"Mean age in {district} is {weighted_mean:.1f} ")

# there is an easier way to do this using numpy
import numpy as np
weighted_mean2= np.average(df_analysis.index, weights=df_analysis[district])
print(f"Mean age in {district} using numpy is {weighted_mean2:.1f} \n")


# Weighted median

# the data is already sorted by age 
# df.sort_values('Single Year of Age', inplace=True)

# create a series called the cumulative sum, and we find the index of the middle value
cumsum = df_analysis[district].cumsum()
cutoff = df_analysis[district].sum() / 2.0
print(f" the cumulative sum is: {cumsum}\n")
print(f" the middle index is {cutoff}\n")

#see where the cumulative sum is greater than or equal to the cutoff
print(f"{df_analysis[district][cumsum >= cutoff]}\n")
# to find the index of the first value where this is true we find the index 0 of this series
print(f"{df_analysis[district][cumsum >= cutoff].index[0]}\n")
median = df_analysis[district][cumsum >= cutoff].index[0]

#median = df_analysis["Single Year of Age"][cumsum >= cutoff].iloc[0]
print(f"weighted median of {district} is {median}\n")

# Mode 
# to calculate the mode, we calcualte the meximum
# https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.idxmax.html#pandas.core.groupby.DataFrameGroupBy.idxmax

mode = df_analysis[district].idxmax()
print(f"weighted mode of {district} is {mode}\n")

# Weighted standard deviation
weighted_mean= np.average(df_analysis.index, weights=df_analysis[district])
print(f"{weighted_mean}\n")

w_variance = np.average((df_analysis.index - weighted_mean)**2, weights=df_analysis[district])
print(f"Weighted variance for {district}: {w_variance}\n")

w_stddev = np.sqrt(w_variance)
print(f"Weighted standard deviation for {district}: {w_stddev}\n")
# Preparing the population data for analysis
# The CSO data is relatively clean
# but we need to group it and remove some unnecessary columns

# author: Gerry Callaghan
# date: October 2025

import pandas as pd

FILENAME = "cso_population_by_age.csv"
DATADIR = "../data/"
FULLPATH = DATADIR + FILENAME

df = pd.read_csv(FULLPATH)

#print(f"{df.head()}\n")

drop_col_list = ["Statistic Label","CensusYear","Sex","UNIT"]
df = df.drop(columns=drop_col_list)

#df.drop(columns=drop_col_list, inplace=True)
#df.drop(columns="Statistic Label", inplace=True)
#df.drop(columns="CensusYear", inplace=True)
#df.drop(columns="Sex", inplace=True)
#df.drop(columns="UNIT", inplace=True)


# this removes the rows where age is "All ages"
df = df[df["Single Year of Age"] != "All ages"]
df["Single Year of Age"]= df["Single Year of Age"].str.replace("Under 1 year","0")
# capital D is a character, so we are using regex to remove anything that is not a digit, such as year(s)
df["Single Year of Age"]= df["Single Year of Age"].str.replace("\D", "", regex=True)
# using df.info we could see that the years column was object type, we need it to be integer type so we use
df["Single Year of Age"] = df["Single Year of Age"].astype("Int64")

df_analysis = pd.pivot_table(df,"VALUE", "Single Year of Age", "Administrative Counties")
print(f"{df_analysis.head()}\n")
print(f"{df_analysis.info()}\n")
df_analysis.to_csv("population_for_analysis.csv")
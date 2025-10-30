# Analysising population
# The CSO data is relatively clean
# but we need to group it and remove some unnecessary columns

# author: Gerry Callaghan
# date: October 2025

import pandas as pd

FILENAME = "population_for_analysis.csv"
DATADIR = "./"
FULLPATH = DATADIR + FILENAME

df = pd.read_csv(FULLPATH)

print(f"{df.head()}\n")
headers = df.columns[1:]

print(f"{headers}\n")

district = headers[0]
print(f"{df[district].describe()}\n")

print(f"{df[district]}\n")
#program reading in CSV from a URL using Pandas
# Author: Gerry Callaghan

import pandas as pd

url= "s3://noaa-gsod-pds/2020/72278023183.csv" 

df = pd.read_csv(url)   
print(df.head())  # Display the first few rows of the dataframe




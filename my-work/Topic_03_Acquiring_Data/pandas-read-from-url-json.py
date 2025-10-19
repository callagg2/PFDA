#program reading in CSV from a URL using Pandas
# Author: Gerry Callaghan

import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=wind_speed_10m,rain&past_days=3&forecast_days=1"
df = pd.read_json(url)
print(df.head())  # Display the first few rows of the dataframe


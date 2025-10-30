# Preparing the population data for analysis
# The CSO data is relatively clean
# but we need to group it and remove some unnecessary columns

# author: Gerry Callaghan
# date: October 2025

import pandas as pd

FILENAME = "cso_population_by_age.csv"
DATADIR = "../../data/"
FULLPATH = DATADIR + FILENAME

df = pd.read_csv(FULLPATH)




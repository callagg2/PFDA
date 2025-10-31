import pandas as pd
import numpy as np


x = np.array([168, 161, 167, 179, 184, 166, 198, 187, 191, 179])
print(f"The mean is: {np.mean(x)}")

print(f"The median is: {np.median(x)}")

print(f"The variance is: {np.var(x, ddof=1)}")

print(f"The standard deviation is: {np.std(x, ddof=1)}")

print(f"{np.percentile(x, [0,25,50,75,100],method="averaged_inverted_cdf")}\n")

fruit_name_list = ['apple', 'banana', 'cherry', 'dates', 'elderberry']
fruit_weight_list = [180, 120, 15, 45, 75]

my_fruit_series = pd.Series(data=fruit_weight_list,
                            index=fruit_name_list)

print(f"{my_fruit_series < 100}\n")

# create the boolean mask and assign to a variable
heavy_fruit_mask = (my_fruit_series >= 100)

# use the mask variable to index into the series
print(f"{my_fruit_series.loc[heavy_fruit_mask]}\n")

# create the boolean mask and assign to a variable
light_fruit_mask = (my_fruit_series <= 100)

# use the mask variable to index into the series
print(f"{my_fruit_series.loc[light_fruit_mask]}\n")

# an example using multiple boolean masks

# step 1: create the boolean mask and assign to a variable
light_fruit_mask = (my_fruit_series <= 20)

# step 1: create the boolean mask and assign to a variable
heavy_fruit_mask = (my_fruit_series >= 100)

# step2: use the mask variable to index into the series
# the '|' in the code below substitutes for or, we'll discuss why soon
print(f"{my_fruit_series.loc[light_fruit_mask | heavy_fruit_mask] }\n")
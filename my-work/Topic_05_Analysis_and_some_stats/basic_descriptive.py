# this script cakculates basic descriptive statistics for a dataset
# author: gerry callaghan
# date: october 2025

import pandas as pd

# a series with an even number of values
even_example_values = pd.Series([1, 2, 2, 3, 4, 5, 6, 10000])

print(f"Series Values: {even_example_values.to_list()}\n")
print(f"Series Mean: {even_example_values.mean()}\n")
print(f"Series Median: {even_example_values.median()}\n")
print(f"Series Mode: {even_example_values.mode()}\n")

# more basic analysis functions
print(f"Series Values: {even_example_values.to_list()}\n")
print(f"Series Mean: {even_example_values.mean()}\n")
print(f"Series Median: {even_example_values.median()}\n")
print(f"Series Mode: {even_example_values.mode()}\n")
print(f"Series Mode: {even_example_values.mode().to_list()}\n")
print(f"Series Min: {even_example_values.min()}\n")
print(f"Series Max: {even_example_values.max()}\n")
print(f"Series Count: {even_example_values.count()}\n")
print(f"Series Length: {len(even_example_values)}\n")
print(even_example_values.describe())


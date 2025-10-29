# import pandas
import pandas as pd

# lists of state names and populations
state_list = ['California', 'Texas', 'Florida', 'New York', 'Illinois',
              'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina', 'Michigan',
              'New Jersey', 'Virginia', 'Washington', 'Arizona', 'Massachusetts',
              'Tennessee', 'Indiana', 'Missouri', 'Maryland', 'Wisconsin',
              'Colorado', 'Minnesota', 'South Carolina', 'Alabama', 'Louisiana',
              'Kentucky', 'Oregon', 'Oklahoma', 'Connecticut', 'Utah', 'Iowa',
              'Nevada', 'Arkansas', 'Mississippi', 'Kansas', 'New Mexico',
              'Nebraska', 'West Virginia', 'Idaho', 'Hawaii', 'New Hampshire',
              'Maine', 'Montana', 'Rhode Island', 'Delaware', 'South Dakota',
              'North Dakota', 'Alaska', 'DC', 'Vermont', 'Wyoming']

population_list = [39512223, 28995881, 21477737, 19453561, 12671821, 12801989,
                   11689100, 10617423, 10488084, 9986857, 8882190, 8535519,
                   7614893, 7278717, 6949503, 6833174, 6732219, 6137428,
                   6045680, 5822434, 5758736, 5639632, 5148714, 4903185,
                   4648794, 4467673, 4217737, 3956971, 3565287, 3205958,
                   3155070, 3080156, 3017825, 2976149, 2913314, 2096829,
                   1934408, 1792147, 1787065, 1415872, 1359711, 1344212,
                   1068778, 1059361, 973764, 884659, 762062, 731545, 705749,
                   623989, 578759,]

# create a series from a list of values and a list of labels
state_series = pd.Series(data=population_list,
                         index=state_list,
                         dtype='int64')

print(f" {type(state_series)}\n")

print(f"{state_series.head()}\n")

print(f"{state_series.tail()}\n")

print(f" {state_series.values}\n")

print(f" {state_series.index}\n")

print(f" {state_series.loc['Hawaii']}\n")

print(f" {state_series.loc['Illinois':'Indiana']}\n")

print(f" {state_series.iloc[4]}\n")

print(f" {state_series.iloc[1:4]}\n")

print(f" {state_series.sort_index().head()}\n")

print(f" {state_series.sort_index().tail()}\n")

print(f" {state_series.sort_values().head()}\n")

print(f" {state_series.sort_values().tail()}\n")

total_population = state_series.sum()
print(f" Total population: {total_population}\n")

state_series_percent = round(state_series / total_population * 100,2)
print(f" {state_series_percent.head()}\n")

# a little program to find the number of large states that account
# for more than 50% of the US population

# sort the values in the series to make sure largest states are at the top
state_series_percent = state_series_percent.sort_values(ascending=False)

# create an empty list that we will add states to
state_50percent_list = []

# initialize a sum that we will add to
percent_sum = 0

# iterate through the values in the index
for state in state_series_percent.index:

  # add the current state name to the list
  state_50percent_list.append(state)

  # add the current state percent to the sum
  percent_sum = percent_sum + state_series_percent[state]

  # if the sum of the percentages exceed 50% stop the loop
  if percent_sum >= 50:
    break


print(f'The top {len(state_50percent_list)} U.S. States by population account \
for more than 50% of the U.S. population.\n')

print('These states include:\n')
for state in state_50percent_list:
  print(f'{state} with a population of {state_series[state]}.')
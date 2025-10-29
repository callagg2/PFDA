import pandas as pd

wlist = ['Los Angeles Lakers', 'Toronto Raptors', 'Golden State Warriors',
  'Golden State Warriors', 'Cleveland Cavaliers', 'Golden State Warriors',
  'San Antonio Spurs', 'Miami Heat', 'Miami Heat', 'Dallas Mavericks',
  'Los Angeles Lakers', 'Los Angeles Lakers', 'Boston Celtics',
  'San Antonio Spurs', 'Miami Heat', 'San Antonio Spurs', 'Detroit Pistons',
  'San Antonio Spurs', 'Los Angeles Lakers', 'Los Angeles Lakers',
  'Los Angeles Lakers', 'San Antonio Spurs', 'Chicago Bulls', 'Chicago Bulls',
  'Chicago Bulls', 'Houston Rockets', 'Houston Rockets', 'Chicago Bulls',
  'Chicago Bulls', 'Chicago Bulls', 'Detroit Pistons', 'Detroit Pistons',
  'Los Angeles Lakers', 'Los Angeles Lakers', 'Boston Celtics',
  'Los Angeles Lakers', 'Boston Celtics', 'Philadelphia 76ers',
  'Los Angeles Lakers', 'Boston Celtics', 'Los Angeles Lakers',
  'Seattle Supersonics', 'Washington Bullets', 'Portland Trail Blazers',
  'Boston Celtics', 'Golden State Warriors', 'Boston Celtics','New York Knicks',
  'Los Angeles Lakers', 'Milwaukee Bucks', 'New York Knicks', 'Boston Celtics',
  'Boston Celtics', 'Philadelphia 76ers', 'Boston Celtics', 'Boston Celtics',
  'Boston Celtics', 'Boston Celtics', 'Boston Celtics', 'Boston Celtics',
  'Boston Celtics', 'Boston Celtics', 'St. Louis Hawks', 'Boston Celtics',
  'Philadelphia Warriors', 'Syracuse Nationals', 'Minneapolis Lakers',
  'Minneapolis Lakers', 'Minneapolis Lakers', 'Rochester Royals',
  'Minneapolis Lakers', 'Minneapolis Lakers', 'Baltimore Bullets',
  'Philadelphia Warriors']

# construct series from list
nba_series = pd.Series(index = wlist, data = range(2020,1946,-1))

# check result
print(f"{nba_series.head()}\n")

# creating a groupby object from a series
nba_grouped = nba_series.groupby(by=nba_series.index)
print(f"{nba_grouped}\n")

print(f"{nba_grouped.head()}\n")
#print(f"{nba_grouped.tail()}\n")

# using .count with a groupby object
print(f"{nba_grouped.count()}\n")

# counting and sorting with a groupby object
print(f"{nba_grouped.count().sort_values(ascending = False).head()}\n")

# get a single group from a groupby object
print(f"{nba_grouped.get_group('Chicago Bulls')}\n")

# Each team's first win is groupby object + .min()
print(f"{nba_grouped.min()}\n")

#Which team had the longest period between their first and last championship?
# subtract min from max, THEN sort values, and view head
print(f"{(nba_grouped.max() - nba_grouped.min()).sort_values(ascending = False).head(10)}\n")

# split the index into a series of lists, grab the last element from each
team_nocity = nba_series.index.str.split(' ').str[-1]
print(f"{team_nocity}\n")

# create a series from the modified index
team_nocity_series = pd.Series(index = team_nocity, data = range(2020,1946,-1))
print(f"{team_nocity_series}\n")

# group the teams by name
team_nocity_grouped = team_nocity_series.groupby(by=team_nocity_series.index)
print(f"{team_nocity_grouped}\n")

# get the counts for the grouped object
print(f"{team_nocity_grouped.count().sort_values(ascending=False).head(10)}\n")
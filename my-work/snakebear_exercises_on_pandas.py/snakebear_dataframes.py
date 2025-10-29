# make sure you always do the import that makes pandas available
import pandas as pd

# constructing an empty Dataframe
my_df = pd.DataFrame()
print(f"{type(my_df)}\n") # checking the datatype of the result

# read the csv file, using the file name as a string, assign the result to df
urlg = "https://raw.githubusercontent.com/"
repo = "bsheese/CSDS125ExampleData/master/"
fnme = "data_albums_sales_wikipedia.csv"
#print(f"{urlg + repo + fnme}\n ")   
df = pd.read_csv(urlg + repo + fnme)
print(f"{df.head()}\n")

print(f"{df.info()}\n")

print(f"{df.head()}\n")

print(f"{df.tail()}\n")

print(f"{df.index}\n")

print(f"{df.columns}\n")

# uses the label of the artist series to set the index
df = df.set_index('artist')

# the artist series now serves as the shared index for the Dataframe
print(f"{df.head(3)}\n")
df = df.reset_index()

# setting year as the index
df = df.set_index('year')

# sort by index (year)
df = df.sort_index()

#check the result
print(f"{df.head()}\n")

# an example of updating the index labels

# copy the index into a list
year_list = df.index.to_list()
print(F"{year_list}\n") 



# create a list of decades from year_list
decade_list = []
for year in year_list:
  decade_list.append((year // 10) * 10)

print(f"{decade_list}\n") 

# convert the list into a series, and set the series name
decade_series = pd.Series(data=decade_list, name='decade')

# kick year out of the index, so we don't overwrite it
df = df.reset_index()
print(f"{df}\n")

# assign decade_series to the index
df.index = decade_series

# check the result
print(f"{df.head()}\n")


# reassign column labels to a non-capitalized form
df.columns = df.columns.str.lower()

# move decade out of the index and into the columns
df = df.reset_index()

# move year into the index
df = df.set_index('year')

# check the result
print(f"{df.head()}\n")

# an example of updating the column index
df.columns = df.columns.str.capitalize()

# check the result
print(f"{df.head()}\n")

# create a decade column
df = pd.read_csv(urlg + repo + fnme)
print(f"{df.head()}\n")
df.loc[:, 'decade'] = (df.loc[:, 'year'] //10) *10
print(f"{df.head()}\n")

# set the index to year
df = df.set_index('year')
print(f"{df.head()}\n")

# sort the dataframe by the index
df = df.sort_index()

# check the result
print(f"{df.head()}\n")


print(f"{df.loc[1971, 'artist']}\n")

print(f"{df.loc[1977:1979, 'artist':'album']}\n")


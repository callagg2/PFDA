# import pandas
import pandas as pd

# define file address
urlg = 'https://raw.githubusercontent.com/'
repo = 'bsheese/CSDS125ExampleData/master/'
fnme = 'data_book_bestsellers.csv'
url = urlg + repo + fnme

print(f"{url}\n")
# create series
df = pd.read_csv(url, names = ['i', 'book']) # ignore this for now
#df = pd.read_csv(url) # ignore this for now
print(f"{df.head()}\n")

book_series = df.iloc[1:].loc[:, 'book']
print(f"{book_series.head()}\n")

book_exclaim = book_series + "!"
print(f"{book_exclaim.head()}\n")

book_series.str.startswith("Harry").head()
print(f"{book_series.str.startswith("Harry").head()}\n")

book_series.str.endswith("Tolkien").head()
print(f"{book_series.str.endswith("Tolkien").head()}\n")

book_series.str.contains("Agatha").head()
print(f"{book_series.str.contains("Agatha").head()}\n")

book_series.str.find("Christi").head()
print(f"{book_series.str.find("Christi").head()}\n")

book_series.str.replace("Little", "Enormous").head()
print(f"{book_series.str.replace("Little", "Enormous").head()}\n")

book_series.str.split(" by ").head()
print(f"{book_series.str.split(" by ").head()}\n")

# split each string into a list, return a series of lists with two elements
# note we have a new variable here called book_series_split 
book_series_split = book_series.str.split(' by ')

# use the string accessor with indexing to get a series
# containing the first value in the new list variable book titles
book_titles = book_series_split.str[0]
print(f"{book_titles.head()}\n")

# use the string accessor with indexing to get a series
# containing the second value in the list
book_authors = book_series_split.str[1]
print(f"{book_authors.head()}\n")

#check result
print(f"{book_authors.tail()}\n")
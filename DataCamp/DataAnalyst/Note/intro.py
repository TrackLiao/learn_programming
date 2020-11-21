#!/usr/bin/env python
# coding=utf-8
# statsmodels, used in machine learning
import statsmodels as sm

# a visualization library
import seaborn as sns

# numpy, a module for performing mathematical operations on lists of data.
import numpy as np

import pandas as pd

from matplotlib import pyplot as plt

# turns a csv file into a table in python
df = pd.read_csv()
# head and info
df.head() #first 5 rows
df.info() # basic info

# select rows using logic
credit_reports[credit_report.suspect == 'Freddy Frequentist']
# turns data into a line plot
plt.plot()
#display plot in a new window
plt.show()
# get the sum of price column in dataframe "credit_records"
credit_records.price.sum()
# plot each letter and frequency column data from dataframe "ransom"
plt.plot(ransom['letter'], ransom['frequency'])
#select column with brackets and string
suspect = credit_records['suspect']
#select with a dot, column name can not contain special character
price = credit_records.price

plt.title()
plt.xlabel()
plt.ylabel()

plt.legend()
plt.plot(x, y, argument....)
# color="tomato", you can search wiki for web colors for more option
# linwidth=1 , you can change to different number, 1 is default value
# linestyle='-', other option are --, -., :
# marker='x', other option are s, o, d, *, h 

#setting a style
plt.style.use('fivethirtyeight'), # other option: ggplot, seaborn, default

plt.style.available # show avaliable style
# line plot,  good for ordered data
# scatter plot good for unorderd data, can be used for correlation
# bar chart good for comparison of categorical data, can be use to see distribution
plt.scatter(df.age, df.height)
#markder transparency
alpha=0.1 # the smaller the number, the more tranparent it is

plt.bar(df.label, df.height)
plt.ylable("something")


#horizontal bar chart, good when we have many bars
plt.barh(df.label, df.height)

#error bar
plt.bar(df.x, df.y, yerr=df.error)

# stacked bar chart
plt.bar(df.x, df.dog)
plt.bar(df.x, df.cat, bottom=df.dog)


# histograph good for visualizeing the distribution
plt.hist(gravel.mass) # take only one argument, default 10 bins
plt.hist(data, bins=nbins) # nbins is numbers of bins
plt.hist(data, range(xmin, xmax)) # focus on specific range
# normalizing histogram when two set of data has differnt sample size
# each bar porportion of the entire dataset
plt.hist(male, density=True)
plt.hist(female, density=True)


## Intermediate Python
```
This will include Visualization, Data Structure, Control Structure
```
# x axis to logarithmic scale
plt.xscale('log')

#show help info
help(plt.hist)
```
Bins
Too few bins will oversimplify reality and won't show you the deatils
Too many bins will overcomplicate reality and won't show the bigger picture.
```
plt.clf() # cleans up plot so you can start afresh
# change y ticks
plt.yticks([0, 2, 4, 6, 8 10])
## slightly modified version with different name
plt.yticks([0, 2, 4, 6, 8, 10],
          ['0', '2B', '4B', '6B', '8B', '10B'])

#list combination
list1 + list2

# chage plt scatter size
plt.scatter(x, y , s=nparray)

#list to numpy array
np_list = np.array(list)

#customization
plt.text(x, y, text) # add text on specific position
plt.grid(True) # show grid line

#Dictionary

list.index(item) i# get the index of element, but not recoomended

sth in box # check if sth in box

world["sealand"] = 0.00028 # add or update pair
del(world["sealand"]) # delete the pair sealand

#Pandas
store data in the form of dataframe

# create yourself
brics = pd.DataFrame(dict)

#set row labels
cars.index = listofname

# set first column as row lable
cars = pd.read_csv('cars.csv', index_col = 0)

#column access []
brics["country"] # this select the column "country" from dataframe brics

# seelct column but in datafram formate
brics[["country"]]


#Row access[]
brics[1:4] # get the 2, 3, 4 row

* loc (lable-based)
* iloc (integer position-based)

brics.loc["Ru"]
brics.loc[["Ru"]]
brics.loc[["Ru", "Cn", "In"]] # select multiple row

brics.loc[[row], [column]]

brics.loc[:, ["country", 'capital']] # all rows but two column

brics.iloc[[1]]
brics.iloc[[1, 2, 3], [2, 3]]

#comparison
special case : True == 1, False == 0

# Boolean Operators
and
or
not
# For NumPy is different
np.logical_and()
np.logical_or()
np.logical_not()

np.logical_and(bmi > 21, bmi < 22)

# if, elif, else
if condition :
    expression
elif:
    expression
else :
    expression

# filtering pandas DataFrames
is_huge = brics["area"] > 8
brics[is_huge]
brics[brics["area"] > 8]

while conditin :
    expression



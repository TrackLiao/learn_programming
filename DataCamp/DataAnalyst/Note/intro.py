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
# scatter plot good for unorderd data
# bar chart good for comparison of categorical data
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

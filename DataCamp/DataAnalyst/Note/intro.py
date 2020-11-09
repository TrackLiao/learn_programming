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
pd.read_csv()
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


plt.plot(x, y, argument....)
# color="tomato", you can search wiki for web colors for more option
# linwidth=1 , you can change to different number, 1 is default value
# linestyle='-', other option are --, -., :
# marker='x', other option are s, o, d, *, h 

#setting a style
plt.style.use('fivethirtyeight'), # other option: ggplot, seaborn, default

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

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

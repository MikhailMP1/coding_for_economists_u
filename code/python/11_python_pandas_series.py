# Introduction to pandas and numpy
# Pandas is a python library for data manipulation
import pandas as pd
import numpy as np

# Let's look at pd.Series
# A series is a one-dimensional array-like object

# Let's define our first pd.Series
# Documentation: https://pandas.pydata.org/docs/reference/api/pandas.Series.html
ps = pd.Series([1, 'a', 2, np.pi])
print(ps)

# Which data type does our pd.Series have?
print(type(ps))

# We can access the values
print(ps.values)

# Access elements of pd.Series by indexing
print(ps[0:2])

# Define a custom index
series_1 = pd.Series(
  data = ["Schnitzel",
         "Lemonade",
         "Whiskey"],
  index = ["Food",
           "Soda",
           "Alcohol"]
)

# Advanced indexing of pd.Series 
# using .loc[]
print(series_1.loc["Food"])

# Accesing more than a single index
print(series_1.loc[["Food", "Alcohol"]])

# using .iloc[]
print(series_1.iloc[0])

# Access elements from a range of indexes
print(series_1.loc["Food": "Alcohol"])



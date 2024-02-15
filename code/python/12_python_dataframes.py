# Intro do pandas.DataFrames
import pandas as pd
import numpy as np

# Create some raw data to construct df
data = {'Tokyo': 30_000_000, 'Delhi': 50_000_000, 'Shanghai': 20_000_000}

# Create df from dict
df = pd.DataFrame(data=data, index=[0])

print(df)

# Create a dataframe from a csv
df_raw = pd.read_csv('https://osf.io/yzntm/download')

# Inspect
print(df_raw.head())

# What are the dimensions of our data?
print(df_raw.shape)

# Access number of rows
print(df_raw.shape[0])

# Name of columns
print(df_raw.columns)

# Create new column; multiple ways of doing so
# df.nnights = 1
# df['nnights'] = 1
df = df_raw.assign(nnights=1)

# Delete df_raw since we do not need it anymore
del df_raw

# Let's check out accommodationtype varialbe
df['accommodationtype''].head()

# We want to clean this up
df['accommodationtype'] = df['accommodationtype'].str.split('@').str[1]

# How many nights in each accommodationtype?
df.accommodationtype.value_counts()

# Clean up missing value
df.accommodationtype.replace("", "Unknown", inplace=True)

# Look at guestreviewsrating
df['guestreviewsrating'].head()

# Create clean variable for ratings
df['ratings'] = df['guestreviewsrating'].str.split('/').str[0].str.strip()

# Convert to float 
df['ratings'] = df['ratings'].astype(float)

# What's the average rating?
print(df.ratings.mean())

# If you have matplolib installed then you can
#df.ratings.hist()

# Small exercise: There's a variable called center1distance. What's the average distance to the center?
# Need to split at whitespace
df['distance_numeric'] = df['center1distance'].str.split().str[0].str.strip()

# Convert to float
df['distance_numeric'] = df['distance_numeric'].astype(float)

# There are a few ratings-related variables; let's inspect them
print(df.filter(regex='rating').head())

df.rename(columns={'rating_reviewcout': 'rating_count',
         'rating2_ta': 'ratingta'},
          inplace=True)

# Rename the following variables:
# ratings2_ta_reviewcount: ratingta_count
# addresscountryname: country
# starrating: stars
# s_city: city
df.rename(columns={
  'ratings2_ta_reviewcount': 'ratingta_count',
  'addresscountryname': 'country',
  'starrating': 'stars',
  's_city': 'city'
},
         inplace=True)

# Subsetting data
# Only look at hotels
print(df.loc[df['accommodationtype'] == 'Hotel'])

# How to check for missing values
print(df.ratings.isnull().sum())

# How many are missing per country?
print(df.ratings.isnull().groupby(df.country).sum())
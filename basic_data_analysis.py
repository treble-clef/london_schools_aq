## After downloading the Excel data, open the file and delete any excess rows and columns so that the first row is the header and the dataset begins in the first column.
## Then delete the first sheet (which is just information about the dataset) and save as a .csv file.
import numpy as np
import pandas as pd
file = "C:/Users/mayda/Downloads/Schools_ParliamentaryConstituencies.csv"
df = pd.read_csv(file)

#################
## Data Basics ##
#################

## View various aspects of the data:
print(df.head())
print(df.tail())
print(df.dtypes)
print(df.index)
print(df.columns)

## Summarize the numerical values of the data
print(df.describe())

## Which schools are the most polluted?
high_to_low = df.sort_values("NO2ug/m3 mean 2013", ascending = False)
high_to_low.iloc[0:5,[1,2,5,7]]

## Which schools are the least polluted?
low_to_high = df.sort_values("NO2ug/m3 mean 2013", ascending = True)
low_to_high.iloc[0:5,[1,2,5,7]]

## Number of schools that have air quality above and below the limit:
df["Above limit"].value_counts()

#Day 31: Pandas and Importing Data
#
#

import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

input("Welcome. Please press enter.")

df = pd.read_csv('pokemon_data.csv', index_col=1)

print(df)

input()

print(df.head(10))
input()

print(df.tail(10))
input()
inpt = input("Now, who would you like to get information for?")
outpt = df.loc[inpt]
query = DataFrame(outpt)
query.to_csv('Pokemon_Query.csv')
print(outpt)

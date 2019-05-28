#Day 41: Introduction to Seaborn using the country population spreadsheet


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("country_population.csv")
plt.figure("Country Population")
plt.subplot(2,2,1)
sns.set_style('darkgrid')
one = sns.scatterplot(x='2016',y='1960',data=df, color='mediumvioletred')


plt.subplot(2,2,2)
sns.set_style('whitegrid')
two = sns.barplot(x='2016',y='1960',data=df, color='darkorchid')


plt.subplot(2,2,3)
sns.set_style('dark')
three = sns.lineplot(x='2016',y='1960', data=df, color='dodgerblue')

plt.subplot(2,2,4)
sns.set_style('white')
four = sns.boxplot(x='2016',y='1960', data=df, color='chartreuse')

plt.show()

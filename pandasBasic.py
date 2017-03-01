import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

##  IO Basics - p.2 Data Analysis with Python and Pandas Tutorial
style.use('ggplot')

web_stats = { 'Day': [ 1,2,3,4,5,6],
              'Visitors':[43,44,56,78,87,98],
              'Bounce_Rate':[90,555,44,55,66,89]}
df = pd.DataFrame(web_stats)

##print(df)
##print(df.head(2))
##print(df.tail())
##print(df.tail(2))

##df.set_index('Day', inplace=True)
print( df )

print(df['Visitors'])
print(df.Visitors)
print(df[['Visitors', 'Bounce_Rate']])

print(df.Visitors.tolist())
print(np.array(df[['Visitors', 'Bounce_Rate']]))

df2=pd.DataFrame( np.array(df[['Visitors', 'Bounce_Rate']]) )
print(df2)

##  IO Basics - p.3 Data Analysis with Python and Pandas Tutorial
df = pd.read_csv('ZILL-Z77006_LPC.csv')
print(df.head())
df.set_index('Date', inplace=True)
print(df.head())
df.to_csv('newcsv.csv')

df = pd.read_csv('newcsv.csv')
print(df.head())

df = pd.read_csv('newcsv.csv', index_col=0)
print(df.head())

df.columns = ['Austin_HPI']
print(df.head())
df.to_csv('newcsv3.csv')
df.to_csv('newcsv4.csv', header=False)

df=pd.read_csv('newcsv4.csv', names=['Date','Austin_HPI'], index_col=0)
print(df.head())

df.to_html('example.html')

df=pd.read_csv('newcsv4.csv', names=['Date','Austin_HPI'])
print(df.head())

df.rename(columns={'Austin_HPI':'77006_HPI'}, inplace=True)
print(df.head())














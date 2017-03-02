import quandl
import pandas as pd
#Building dataset - p.4 Data Analysis with Python and Pandas Tutorial

##df = quandl.get('FMAC/HPI_AK')
##print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#This is a list
print(fiddy_states)
print("###############")

#This is a dataframe
print(fiddy_states[0])
print("###############")

#This is a column
print(fiddy_states[0][0])
print("###############")

for abbv in fiddy_states[0][0][1:]:
    print('FMAC/HPI_'+abbv)

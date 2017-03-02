#!python
# -*- coding: utf-8 -*-
import pandas as pd
import codecs
url="http://rate.bot.com.tw/xrt?Lang=zh-TW"

df = pd.read_html(url)

f = codecs.open('forex.html', 'w', "utf-8") #write unicode to file
f.write(df[0].to_html())

df = pd.read_html('forex.html', encoding = 'utf8')
f.close()

kk = df[0] #kk is a DataFrame
kk = kk[[u'���O', u'���O.1', u'�{���ײv', 'Unnamed: 3', u'�Y���ײv']]
kk.columns = [u'���O',u'�{���R�J',u'�{����X',u'�Y���R�J',u'�Y����X']
print(kk)

#df=df[0]
#print(df[0])

#df.drop(df.columns[[5,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]], axis=1) #axis=1 denote column

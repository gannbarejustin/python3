#!python
# -*- coding: utf-8 -*-
import pandas as pd
##url="http://rate.bot.com.tw/xrt?Lang=zh-TW"
##
##df = pd.read_html(url)
##
##f = open('forex.html', 'w')
##f.write(df[0].to_html())

df = pd.read_html('forex.html')

print(df[0][0][0])

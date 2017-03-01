#!python

import pandas as pd
url="http://rate.bot.com.tw/xrt?Lang=zh-TW"

df = pd.read_html(url)
print(df[0])
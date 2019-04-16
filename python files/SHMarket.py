#使用tushare步骤：
# 1. 导入 tushare
# 2. 设置 token
# 3. 初始化 Pro 接口
# 4. 数据调取

#import tushare
#
# print('tushare version: ' + tushare.__version__)
# tushare.set_token('8f8f3d53921ba974ece21d699a09d6f7381e0f2bdeb29ff535ef0945')
# pro = tushare.pro_api()
# data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
# print(data)

import mpl_finance
import tushare as ts
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.pylab import date2num
import numpy as np

def format_date(x,pos):
    if x<0 or x>len(date_tickers)-1:
        return ''
    return date_tickers[int(x)]

sns.set()
pro = ts.pro_api('8f8f3d53921ba974ece21d699a09d6f7381e0f2bdeb29ff535ef0945')

df = pro.index_daily(ts_code='000001.SH', start_date='20150901')
df = df.sort_values(by='trade_date', ascending=True)
df['trade_date2'] = df['trade_date'].copy()
df['trade_date'] = pd.to_datetime(df['trade_date']).map(date2num)
df['dates'] = np.arange(0, len(df))
df.head()
date_tickers = df.trade_date2.values
fig, ax = plt.subplots(figsize=(10,5))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
mpl_finance.candlestick_ochl(
    ax=ax,
    quotes=df[['dates', 'open', 'close', 'high', 'low']].values,
    width=0.7,
    colorup='r',
    colordown='g',
    alpha=0.7)
ax.set_title('SH Exchange(2018.9-)', fontsize=20)
df.close.rolling(60).mean().plot()
plt.show()

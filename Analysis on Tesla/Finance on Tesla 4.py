import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('dark_background')
df = pd.read_csv('Tesla_Stocks_File.csv', parse_dates = True, index_col=0)
##df['100 Moving Average'] = df['Adj Close'].rolling(window=100 ,min_periods=0).mean()
##print(df.head())
df_ohlc=df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
#print(df_ohlc.head())
ax1 = plt.subplot2grid((6,1),(0,0),rowspan = 5, colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan = 1, colspan=1, sharex=ax1)
#sharex for operations on both the graphs at the same time remove
#it for seperate operation and analysis
ax1.xaxis_date()
# display the mdates taken by matplotlib earlier and display them
ax1.set_title('Candlestick Graph 10 Days Average')
candlestick_ohlc(ax1 , df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num) , df_volume.values, 0)
ax2.set_title('Volume 10 Days Average')
plt.tight_layout()
plt.show()

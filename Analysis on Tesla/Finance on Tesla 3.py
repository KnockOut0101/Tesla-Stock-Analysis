import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import matplotlib.gridspec as gridspec

style.use('dark_background')
df = pd.read_csv('Tesla_Stocks_File.csv', parse_dates = True, index_col=0)

##100 moving average
##(Basically takes today's price and 99 price(s) of it prior to today's price)
##then take out the average.
'''df['100 Moving Average']'''
##Moving Average Experiment
'''df['100 Moving Average'] = df['Adj Close'].rolling(window=100).mean()
print("The Diffrence Between df.head() and df.tail() with Respect to Moving Average")
print("df.tail()")
print(df.tail())
print("df.head()")
print(df.head())
print("Usage of df.head() with 100 results")
print(df.head(100))'''
##Calculation of 100 days with no minimum limit
df['100 Moving Average'] = df['Adj Close'].rolling(window=100 ,min_periods=0).mean()
print(df.head())
##Using subplots for representation of 2 graphs to have datarepresented in a simple comparable manner along with x axis shared
ax1 = plt.subplot2grid((6,1),(0,0),rowspan = 5, colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan = 5, colspan=1, sharex=ax1)
##sharex for operations on both the graphs at the same time remove it for seperate operation and analysis
ax1.plot(df.index , df['Adj Close'], label='Adj Close')
ax1.plot(df.index , df['100 Moving Average'], label='100 Moving Average')
ax1.set_title('Adj Close & Moving Average(100 Values at a time)')
ax1.legend()
ax2.bar(df.index , df['Volume'], label='Volume')
ax2.set_title('Volume with shared x axis with the upper graph')
plt.tight_layout()
plt.show()


import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
#### The style used for implementation of the graphs
style.use('dark_background')



####reading data
'''start = dt.datetime(2000,1,1)
end = dt.datetime.now()

df = web.DataReader('TSLA', 'yahoo', start, end)'''
####csv file creation
'''df.to_csv('Tesla_Stocks_File.csv')'''

df = pd.read_csv('Tesla_Stocks_File.csv', parse_dates = True, index_col=0)
'''print(df.head())'''
####selective printing
print(df[['Open','High']].head())
df.plot(figsize=(15,15))
##df.plot()
plt.xlabel("Tesla OHLC Graph")
plt.ylabel("Value")
represent=plt.show()
represent

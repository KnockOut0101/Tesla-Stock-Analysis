import datetime as dt
#using plt to utilize pyplot to make charts,maps,graphs etc
import matplotlib.pyplot as plt
#style is for visualization of graphs,charts and maps by pyplot
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('dark_background')# one of the many styles available

start = dt.datetime(2000,1,1)# starting Date 
end = dt.datetime.now()# ending Date till the present time

df = web.DataReader('TSLA', 'yahoo', start, end)

print(df.head())# starting representation of rows of data.
print(df.tail())# final representation of rows of data. till the last value

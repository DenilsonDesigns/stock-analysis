import pandas_datareader.data as web
import datetime
import pandas_datareader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2019, 2, 1)

tesla = web.DataReader('TSLA', 'yahoo', start, end)
ford = web.DataReader('FORD', 'yahoo', start, end)
gm = web.DataReader('GM', 'yahoo', start, end)

print(tesla.head())
print(ford.head())
print(gm.head())

# Plot based on opening prices
# tesla['Open'].plot(label='Tesla', figsize=(16, 8), title='Open Price')
# ford['Open'].plot(label='FORD')
# gm['Open'].plot(label='GM')
# # plt.legend()
# plt.show()

# Plot based on closing prices
# tesla['Adj Close'].plot(label='Tesla', figsize=(16, 8),
#                         title='Adj Close Price')
# ford['Adj Close'].plot(label='FORD')
# gm['Adj Close'].plot(label='GM')
# # plt.legend()
# plt.show()

# daily volume
tesla['Volume'].plot(label='Tesla', figsize=(16, 8),
                     title='Volume')
ford['Volume'].plot(label='FORD')
gm['Volume'].plot(label='GM')
# plt.legend()
# plt.show()

# dates of max trading volumes for each stock
print("Tesla max: {}".format(tesla['Volume'].idxmax()))
print("Ford max: {}".format(ford['Volume'].idxmax()))
print("GM max: {}".format(gm['Volume'].idxmax()))


# Create a new column for each dataframe called “Total Traded” which is the Open Price multiplied by the Volume Traded.

import pandas_datareader.data as web
import datetime
import pandas_datareader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import mplfinance as mpf
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DateLocator, MONDAY

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2019, 2, 1)

tesla = web.DataReader('TSLA', 'yahoo', start, end)
ford = web.DataReader('FORD', 'yahoo', start, end)
gm = web.DataReader('GM', 'yahoo', start, end)

# print(tesla.head())
# print(ford.head())
# print(gm.head())

# Plot based on opening prices
# tesla['Open'].plot(label='Tesla', figsize=(16, 8), title='Open Price')
# ford['Open'].plot(label='FORD')
# gm['Open'].plot(label='GM')
# # plt.legend()
# plt.show()
# *************

# Plot based on closing prices
# tesla['Adj Close'].plot(label='Tesla', figsize=(16, 8),
#                         title='Adj Close Price')
# ford['Adj Close'].plot(label='FORD')
# gm['Adj Close'].plot(label='GM')
# # plt.legend()
# plt.show()
# ***********

# daily volume
# tesla['Volume'].plot(label='Tesla', figsize=(16, 8),
#                      title='Volume')
# ford['Volume'].plot(label='FORD')
# gm['Volume'].plot(label='GM')
# plt.legend()
# plt.show()
# *********

# dates of max trading volumes for each stock
# print("Tesla max: {}".format(tesla['Volume'].idxmax()))
# print("Ford max: {}".format(ford['Volume'].idxmax()))
# print("GM max: {}".format(gm['Volume'].idxmax()))
# *************

# Create a new column for each dataframe called “Total Traded” which is the Open Price multiplied by the Volume Traded.
tesla['Total Traded'] = tesla['Open'] * tesla['Volume']
ford['Total Traded'] = ford['Open'] * ford['Volume']
gm['Total Traded'] = gm['Open'] * gm['Volume']

# Plot this "Total Traded"
# tesla['Total Traded'].plot(label='Tesla', figsize=(16, 8))
# ford['Total Traded'].plot(label='Ford')
# gm['Total Traded'].plot(label='GM')
# ***********

# plt.ylabel('Total Traded')
# plt.legend()
# plt.show()

# print("Tesla total highest trading day: {}".format(
#     tesla['Total Traded'].idxmax()))
# ****************

# Plotting moving average of GM
gm['MA50'] = gm['Open'].rolling(50).mean()
gm['MA200'] = gm['Open'].rolling(200).mean()
# gm[['Open', 'MA50', 'MA200']].plot(label='GM', figsize=(20, 15))

# plt.show()
# car_comp = pd.concat([tesla['Close'], ford['Close'], gm['Close']], axis=1)
# print(car_comp)
# car_comp.columns = ['Tesla Close', 'Ford Close', 'GM close']
# print(car_comp)
# scatter_matrix(car_comp, figsize=(10, 10), alpha=0.1, hist_kwds={'bins': 50})
# plt.show()
# **************

# Creating a Candlestick Chart for Ford
# ford_reset = ford.loc['2018-12':'2019-02'].reset_index()
# # print(ford_reset)
# ford_reset['date_ax'] = ford_reset['Date'].apply(lambda date: date2num(date))
# # print(ford_reset)
# # print(ford_reset.head())

# list_of_cols = ['date_ax', 'Open', 'High', 'Low', 'Close']
# ford_values = [tuple(vals) for vals in ford_reset[list_of_cols].values]

# # print(ford_values)
# mondays = WeekdayLocator(MONDAY)
# alldays = DateLocator()
# week_formatter = DateFormatter('%b %d')
# day_formatter = DateFormatter('%d')

# fig, ax = plt.subplots()
# fig.subplots_adjust(bottom=0.2)
# ax.xaxis.set_major_locator(mondays)
# ax.xaxis.set_major_formatter(week_formatter)

# mpf.plot(ford_values)
# *******************

# Calculate the return from the Close price column
tesla['returns'] = tesla['Close'].pct_change(1)
ford['returns'] = ford['Close'].pct_change(1)
gm['returns'] = gm['Close'].pct_change(1)

print(tesla.head())
print(ford.head())
print(gm.head())

# ford['returns'].hist(bins=50, label='Tesla', figsize=(10, 8), alpha=0.5)
# gm['returns'].hist(bins=100, label='GM', alpha=0.5)
# tesla['returns'].hist(bins=100, label='Ford', alpha=0.5)

# tesla['returns'].plot(kind='kde', label='Tesla', figsize=(10, 8), alpha=0.5)
# gm['returns'].plot(kind='kde', label='gm', figsize=(10, 8), alpha=0.5)
# ford['returns'].plot(kind='kde', label='ford', figsize=(10, 8), alpha=0.5)
# plt.legend()
# plt.show()
# ********************

# Box plots comparing the returns
box_df = pd.concat([tesla['returns'], gm['returns'], ford['returns']], axis=1)
box_df.columns = ['Tesla Returns', 'GM Returns', 'Ford Returns']
box_df.plot(kind='box', figsize=(8, 11), colormap='jet')

plt.legend()
plt.show()

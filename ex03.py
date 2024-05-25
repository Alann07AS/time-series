import pandas as pd
import numpy as np


business_dates = pd.bdate_range('2021-01-01', '2021-12-31')

#generate tickers
tickers = ['AAPL', 'FB', 'GE', 'AMZN', 'DAI']

#create indexs
index = pd.MultiIndex.from_product([business_dates, tickers], names=['Date', 'Ticker'])

# create DFs
market_data = pd.DataFrame(index=index,
                        data=np.random.randn(len(index), 1),
                        columns=['Price'])

print(market_data)

# Use pivot table
pivot_table_result = pd.pivot_table(market_data, values='Price', index='Date', columns=['Ticker'], aggfunc='mean')

# (return(d) = (price(d)-price(d-1))/price(d-1)) 
# market_data["Ticker"] = ((market_data["Ticker"] - market_data["Ticker"][-1:]) / market_data["Ticker"][-1:])
pivot_table_result = ((pivot_table_result - pivot_table_result.shift(1)) / pivot_table_result.shift(1))

print(pivot_table_result)
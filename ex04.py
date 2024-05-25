import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Apple stock data (assuming 'AAPL.csv' is the data file)
apple_stock_data = pd.read_csv('AAPL.csv')
apple_stock_data['Date'] = pd.to_datetime(apple_stock_data['Date'])
apple_stock_data.set_index('Date', inplace=True)

# Task 1: Drop missing values and compute daily future returns
daily_returns = apple_stock_data['Adj Close'].dropna().pct_change()
# daily_returns = (daily_returns.shift(-1)-daily_returns)/daily_returns

# Task 2: Create a Series with a random boolean array
np.random.seed(42)
long_only_signal = pd.Series(np.random.choice([0, 1], size=len(daily_returns), p=[0.5, 0.5]), index=daily_returns.index)

# Task 3: Backtest the signal
pnl = (long_only_signal * daily_returns.shift(-1) - long_only_signal).fillna(0)
print(pnl)
# Task 4: Compute the return of the strategy
strategy_return = pnl.sum() / long_only_signal.sum()

# Task 5: Input signal is always to buy. Compute daily PnL and total PnL
always_buy_signal = pd.Series(1, index=daily_returns.index)
always_buy_pnl = (always_buy_signal * daily_returns.shift(-1) - always_buy_signal).fillna(0)
always_buy_total_pnl = always_buy_pnl.sum()

# Plot the daily PnL of Q5 and Q3 on the same plot
plt.plot(pnl.cumsum(), label='Long Only Signal')
plt.plot(always_buy_pnl.cumsum(), label='Always Buy Signal')
plt.legend()
plt.title('Daily PnL Comparison')
plt.xlabel('Date')
plt.ylabel('Cumulative PnL')
plt.show()

# Display the results
print(f"Strategy Return: {strategy_return:.2%}")
print(f"Always Buy Total PnL: {always_buy_total_pnl:.2%}")

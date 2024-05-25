import pandas as pd
import plotly.graph_objects as go

# Load Apple stock data
apple_stock_data = pd.read_csv('AAPL.csv')  # Replace with the actual path to your data file

# Task 1: Preprocess the data
# Check for missing values
print(apple_stock_data.isnull().sum())

# Convert string dates to datetime objects
apple_stock_data['Date'] = pd.to_datetime(apple_stock_data['Date'])

# Set the date column as the index
apple_stock_data.set_index('Date', inplace=True)

# Task 2: Generate a candlestick chart using Plotly
fig = go.Figure(data=[go.Candlestick(x  =apple_stock_data.index,
                open=apple_stock_data['Open'],
                high=apple_stock_data['High'],
                low=apple_stock_data['Low'],
                close=apple_stock_data['Close'])])

fig.update_layout(title='Apple Stock Candlestick Chart',
                  xaxis_title='Date',
                  yaxis_title='Stock Price',
                  xaxis_rangeslider_visible=False)

# Show the candlestick chart
fig.show()

# Task 3: Aggregate the data to the last business day of each month
monthly_aggregated_data = apple_stock_data.resample('BM').last()
print(f'Number of months in the considered period: {monthly_aggregated_data.count()}')

# Task 4: Compute daily returns based on the Open price
# Using pct_change function
apple_stock_data['Daily_Returns_pct_change'] = apple_stock_data['Open'].pct_change()

# Using vectorized approach
apple_stock_data['Daily_Returns_vectorized'] = (apple_stock_data['Open'] - apple_stock_data['Open'].shift(1)) / apple_stock_data['Open'].shift(1)

# Display the processed DataFrame
print(apple_stock_data.head())

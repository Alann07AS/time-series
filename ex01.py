import pandas as pd
import numpy as np

# 1st January 2010 to 31 December 2020
dates = pd.date_range("2010-01-01", "2020-12-31")
integer_series = pd.Series(index=dates, data=np.arange(0, len(dates)))

print(integer_series)

moyenne = integer_series.rolling(window=7).mean()
print(moyenne)
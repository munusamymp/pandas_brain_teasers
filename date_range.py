import pandas as pd

start = pd.Timestamp.fromtimestamp(0).strftime('%Y-%m-%d')
times = pd.date_range(start, periods=2, freq='M')
print(times)
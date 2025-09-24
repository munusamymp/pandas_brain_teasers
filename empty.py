import pandas as pd

s = pd.Series([], dtype='float64')
print('full' if s.all() else 'empty')
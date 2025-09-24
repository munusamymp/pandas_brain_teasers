import numpy as np
import pandas as pd 

s = pd.Series([1, np.nan, 3, None, 5])
s.fillna(3)
print(s.sum())
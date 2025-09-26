import numpy as np
import pandas as pd

s = pd.Series([1, 2, np.nan, 4])
print(s[~pd.isnull(s)])
# or s[s.notna()]
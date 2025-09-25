import numpy as np
import pandas as pd

v = pd.Series([.1, 1., 1.1])
out = v * v
expected = pd.Series([.01, 1., 1.21])
if np.allclose(out, expected):
    print("Match Worked!")
else:
    print("Match Failed!")

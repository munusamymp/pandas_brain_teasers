import pandas as pd

nums = pd.Series([1, 2, 3, 4, 5, 6])
print(nums[(nums > 2) and (nums < 5)])

# use bitwise operators & and to work.
# nums>2 is a series of Boolean values:

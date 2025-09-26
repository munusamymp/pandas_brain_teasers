import pandas as pd

y3k = pd.Timestamp(3000, 1, 1)
print(f'They arrived to Earth on {y3k:%B %d}.')

import pandas as pd

df = pd.DataFrame([[1,2],[3,4]], columns=['x', 'y'])
print(df.to_csv())
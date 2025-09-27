import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Clark Kent', 'Diana Prince', 'Bruce Wayne'],
})

df2 = pd.DataFrame({
    'id': [2, 1, 4],
    'hero': ['Wonder Woman', 'Superman', 'Aquaman'],
})

df = pd.merge(df1, df2, on='id')
print(df)
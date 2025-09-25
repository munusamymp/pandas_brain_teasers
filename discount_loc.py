import pandas as pd

df = pd.DataFrame([
    ['Bugs', True, 72.3],
    ['Elmer', False, 63.4],
    ['Daffy', True, 90.5]
], columns=['Customer', 'Member', 'Amount'])

df.loc[df['Member'], 'Amount'] *= 0.9
print(df)
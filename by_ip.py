import pandas as pd

df = pd.DataFrame([
    ['133.43.96.45', pd.Timedelta('3s')],
    ['133.68.18.180', pd.Timedelta('2s')],
    ['133.43.96.45', pd.NaT],
    ['133.43.96.45', pd.Timedelta('4s')],
    ['133.43.96.45', pd.Timedelta('2s')],
], columns=['IP', 'Duration'])

by_ip = (df['Duration'].fillna(pd.Timedelta(seconds=1))
         .groupby(df['IP'])
         .sum()
         )

print(by_ip)
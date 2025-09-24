from io import StringIO
import pandas as pd

csv_data = '''\
day,hits
2020-01-01,100
2020-02-02,120
2020-02-03,130
'''

df = pd.read_csv(StringIO(csv_data), parse_dates=['day'])
print(df['day'].dt.month.unique())
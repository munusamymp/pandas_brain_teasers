import pandas as pd

s1 = pd.to_datetime(['2020-01-01T00:00:00+00:00', '2020-01-01T01:00:00+00:00'])
s2 = pd.to_datetime([pd.Timestamp(2020, 1, 1), pd.Timestamp(2020, 2, 2)])

print(s1 == s2)

# tz-aware and tz-naive timestamps are never equal
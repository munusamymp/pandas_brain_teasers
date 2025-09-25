import pandas as pd

df = pd.DataFrame([
    ['Bugs', True, 72.3],
    ['Elmer', False, 63.4],
    ['Daffy', True, 90.5]
], columns=['Customer', 'Member', 'Amount'])

df[df['Member']]['Amount'] *= 0.9
print(df)

# The change is not reflected in df. The reason is that Pandas does a lot of work
# under the hood to avoid copying data. However, in some cases it can’t, and
# then you’ll get a copy of the data.
# To avoid this problem, use .loc to explicitly state you want to modify the

import pandas as pd

simpsons = pd.Series(['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie'])
print(simpsons)

print('Bart' in simpsons.values)
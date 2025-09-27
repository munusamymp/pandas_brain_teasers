import pandas as pd

heroes = pd.Series(['Spiderman', 'batman', 'WONDER', 'ironman', 'Thor'])
if heroes.str.find('Ironman').any():
    print("Not found!")
else:
    print("Found!")
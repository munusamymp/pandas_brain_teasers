import pandas as pd

cities = pd.DataFrame([
    ('Vienna', 'Austria', 1_897_491),
    ('Sofia', 'Bulgaria', 1_238_438),
    ('Zurich', 'Switzerland', 428_737),
], columns=['City', 'Country', 'Population'])

def population_of(city):
    return cities.loc[cities['City'] == city]['Population']

city = 'Vienna'
print(population_of(city))

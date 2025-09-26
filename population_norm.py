import unicodedata
import pandas as pd

cities = pd.DataFrame([
    ('Vienna', 'Austria', 1_897_491),
    ('Sofia', 'Bulgaria', 1_238_438),
    ('Zurich', 'Switzerland', 428_737),
], columns=['City', 'Country', 'Population'])

def population_of(city):
    city = normalize(city)
    return cities[cities['city_norm'] == city]['Population']

def normalize(name):
    return unicodedata.normalize('NFKC', name).casefold()
    
cities['city_norm'] = cities['City'].apply(normalize)

city = 'Vienna'
print(population_of(city))

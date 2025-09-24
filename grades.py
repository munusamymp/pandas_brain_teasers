import pandas as pd

grades = pd.Series([88, 92, 79])
bonuses = pd.Series([5, 2, 3, 4])

final_grades = grades + bonuses
print(final_grades)
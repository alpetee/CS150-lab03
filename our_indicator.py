import pandas as pd
from pandas_datareader import wb
#
# df = wb.get_indicators()[['id','name']]
# df = df[df.name == 'Individuals using the Internet (% of population)']

df = wb.get_indicators()[['id','name']]
df = df[df.name == 'Carbon dioxide (CO2) emissions (total) excluding LULUCF (% change from 1990)']

print(df)

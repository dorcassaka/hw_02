import json 
import matplotlib.pyplot as plt
import pprint
import pandas as pd

data = pd.read_csv('data/popsex.csv', nrows= 12)

a = data[data.Location == 'Afghanistan']

plt.plot(a.Time, a.PopTotal/10**3)
plt.plot(a.Time, a.PopFemale/10**3)


plt.legend(['Population Total', 'Population Female'])
plt.xlabel('Year')
plt.ylabel('Population (In Millions)')
plt.show()

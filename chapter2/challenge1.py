'''
Temperature graph for Zhanjiang, China
02/09/2019
'''
from matplotlib import pyplot as plt
import numpy as np


#time of day
tod = ['12am', '4am', '7am', '10am', '1pm', '4pm', '7pm', '10pm']
temp = [70, 69, 69, 69, 71, 76, 73, 71]

plt.xlabel = ('Time of day')
plt.ylabel = ('Temperature')
plt.xticks(np.arange(len(tod)), tod)

plt.plot(tod, temp, marker='o')
plt.show()

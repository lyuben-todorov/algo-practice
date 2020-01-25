import matplotlib.pyplot as plt
import numpy as np
import random as rand
import math as math

data_pairs = 10
data = np.array([])
a = 5
samples = 1000 
for i in range(0,samples):
    r = rand.random()*1000 -500
    y = r + a*i
    data = np.append(data, [y])

plt.plot(data, 'ro')


sum_xy = 0
for i in range(0,samples):
    xy = i*data[i]
    sum_xy+=xy
sum_xx = 0
for i in range(0,samples):
    xx = data[i]*data[i]
    sum_xx += xx

tangent = sum_xx/sum_xy
print(tangent)
result = []
for i in range(0,samples):
    result.append(tangent*i)

plt.plot(result)
plt.show() 
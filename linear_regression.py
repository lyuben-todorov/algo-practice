import matplotlib.pyplot as plt
import numpy as np
import random as rand
import math as math

data = np.array([0 ,5,5,6,7,11])
samples = 6
# for i in range(0,samples):
#     r = rand.random()*1000 -500
#     y = r + a*i
#     data = np.append(data, [y])
    
plt.plot(data, 'ro')


sum_xy = 0
for i in range(1,samples):
    xy = i*data[i]
    sum_xy+=xy
sum_xx = 0
for i in range(0,samples):
    xx = data[i]*data[i]
    sum_xx += xx

tangent = sum_xx/sum_xy
print(tangent)
result = []

def loss_function(a,x,y):
    e =(a*x-y)
    loss = (e**2)*np.log(e**2 +1)
    print('%s %s : %s'% (x,y,loss))
    return loss

total_loss = 0
for i in range(1, samples):
    total_loss+=(loss_function(34/15, i, data[i]))
    result.append(tangent*i)
print(total_loss)
plt.plot(result)
plt.show()
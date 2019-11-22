import matplotlib.pyplot as plt
import numpy as np
import random as rand
import math as math
import sympy as sp

# Problem formulation:
# We want to fit a line of the form y=ax through those points. 
# The error  (which of course depends on the choice of a ) that our fit makes at every input location x , is measured by the following error criterion: 
# (ax−y)2⋅log((ax−y)2+1) , where obviously the log is the natural logarithm.
# Now, let the function E:a↦E(a) be the total error over all points, depending on parameter a.

# Find the minimum value that E  attains, to three decimals accuracy behind the decimal point:  


data = np.array([0, 5,5,6,7,11])

samples = 6
x = sp.Symbol('x')
y = sp.Symbol('y')
a = sp.Symbol('a')
iterations = 0

def get_df():
    f = ((a * x - y) ** 2) * sp.log((a * x - y) ** 2 + 1)
    f_deriv = f.diff(a)
    f_deriv = sp.lambdify([a, x, y], f_deriv)
    
    return f_deriv
def get_f():
    return sp.lambdify([a,x,y],((a * x - y) ** 2) * sp.log((a * x - y) ** 2 + 1))
def loss_function(a, x, y):
    loss = ((a*x-y)**2)*np.log((a*x-y)**2 + 1)
    return loss
def gradient_descent():
    loss = 1000000.0
    max_iterations = 10000
    gamma = 0.000001
    f = get_f()
    df = get_df()
    global iterations
    a = 2
    while(loss > 0.00002  and max_iterations > iterations):
        last_a = a
        sum_roc = 0
        for i in range(1, samples):
            roc = df(a, i, data[i]) # rate of change
            sum_roc += roc
        sum_roc = sum_roc*gamma
        a = last_a - sum_roc
        
        loss = abs(a-last_a)
        print('a = %s  ---- loss = %s' % (a,loss))

        iterations += 1
    return  a
optimal_a = gradient_descent()

total_loss = 0
for i in range(1, samples):
    total_loss+=loss_function(optimal_a, i, data[i])

print('Found minimum loss: %s' % total_loss)
print('For a-value: %s' % optimal_a)
print('In %s steps'% iterations)




# xvalues = []
# yvalues = []

# for j in np.linspace(2.1,2.2, 20000):
#     total_loss = 0
#     for i in range(1, samples):
#         total_loss+=loss_function(j, i, data[i])
#     xvalues.append(j)
#     yvalues.append(total_loss)
#     print(total_loss)

# print(" result")
# print(min(yvalues))
# print(xvalues[yvalues.index(min(yvalues))])

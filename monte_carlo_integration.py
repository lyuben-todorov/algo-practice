import math as math
import random as rand
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def f(x1, x2, x3, x4, x5):
        return math.pow(x1, 7/11.0) + math.pow(x2, 8/11.0) + math.pow(x3, 9/11.0) + math.pow(x4, 10/11.0) + math.sin(x5)


samples = 1000000
results = []
for i in range(samples):
        a = rand.random()
        b = rand.random()
        c = rand.random()

        d = rand.random()
        e_range = math.sqrt(1-d*d)

        e = rand.uniform(0,e_range)

        dice = rand.random()

        if dice < 0.5:
                y = f(a, b, c, d, e)
        else:
                y = f(a, b, c, e, d)
        results.append(y)

area_approx = 0
for number in results:
        area_approx += number

print(area_approx/samples*3.14/4)

sns.distplot(results, hist=False, kde=True,
             kde_kws={'linewidth': 3})
plt.show()

# least square method   0 2 5 7   -1 5 12 20    y = -1.13793 + 2.89655x

import numpy as np

x = []
y = []
n = int(input(f"Enter number of data: "))
x = np.zeros(n)
y = np.zeros(n)
for i in range(n):
    x[i] = float(input(f"Enter value of x[{i}]: "))
    y[i] = float(input(f"Enter value of y[{i}]: "))
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x*y)
sum_x2 = np.sum(x*x)

m = ( (n * sum_xy) - (sum_x * sum_y) ) / ( (n * sum_x2) - (sum_x ** 2) )
a = (sum_y - m * sum_x)/n

print(f" The equation is: y = {a:.5f} + {m:.5f}x")

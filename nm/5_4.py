# least square method   

import numpy as np
import math

x = []
y = []
n = int(input(f"Enter number of data: "))
x = np.zeros(n)
y = np.zeros(n)
for i in range(n):
    x[i] = float(input(f"Enter value of x[{i}]: "))
    y[i] = float(input(f"Enter value of y[{i}]: "))
Y = np.log(y)
sum_x = np.sum(x)
sum_lny = np.sum(Y)
sum_xlny = np.sum(x*Y)
sum_x2 = np.sum(x*x)

m = ( (n * sum_xlny) - (sum_x * sum_lny) ) / ( (n * sum_x2) - (sum_x ** 2) )
a = (sum_lny - m * sum_x)/n
B = m
A = np.exp(a)
print(f" The equation is: y = {A:.5f} + {B:.5f}x")

# newton forward  10 20 30 40 50 60   5 4 6 10 12 9   
#                 3 4 5 6 7 8 9   4.8 8.4 14.5 23.6 36.2 52.8 73.9   3.5 ans 6.32

import numpy as np
import math

n = int(input("Enter number of data: "))

x = np.zeros(n)
y = np.zeros((n, n))

print("Enter x and y values:")
for i in range(n):
    x[i] = float(input(f"x[{i}] = "))
print()
for i in range(n):
    y[i][0] = float(input(f"y[{i}] = "))

xp = float(input("Enter interpolation point: "))
for j in range(1, n):
    for i in range(n - j):
        y[i][j] = y[i+1][j-1] - y[i][j-1]

h = x[1] - x[0]
p = (xp - x[0]) / h

result = y[0, 0]
p_term = 1

for i in range(1, n):
    p_term *= (p - (i - 1))
    result += (p_term * y[0, i]) / math.factorial(i)

print(f"\nInterpolated value at yp = {result}")

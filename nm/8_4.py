#crank nicholson method
# ut = uxx
# boundary value: 1. u(0,t) = u(1,t)
#                 2. u(x,0) = sin pi x
# h = 0.2  k = 0.02   0<=x<=1  0<=t<=0.1

import numpy as np

h = 0.2
k = 0.02
x = np.arange(0, 1 + h, h)
t = np.arange(0, 0.1 + k, k)

nx = len(x)
nt = len(t)
r = k / h**2   # r = 0.5 here

# Initialize solution matrix: rows = time, columns = space
u = np.zeros((nt, nx))

# Initial condition
u[0, :] = np.sin(np.pi * x)

# Boundary conditions
u[:, 0] = 0
u[:, -1] = 0

# Build the tridiagonal matrices for interior points
n_interior = nx - 2   # unknowns at each time level

A = np.zeros((n_interior, n_interior))   # for u^(n+1) (LHS)
B = np.zeros((n_interior, n_interior))   # for u^n (RHS)

for i in range(n_interior):
    A[i, i] = 2 * (1 + r)
    B[i, i] = 2 * (1 - r)
    if i > 0:
        A[i, i-1] = -r
        B[i, i-1] = r
    if i < n_interior - 1:
        A[i, i+1] = -r
        B[i, i+1] = r

# Time-stepping loop
for n in range(nt - 1):
    b = B @ u[n, 1:-1]

    # Add boundary contributions (zero here, but included for generality)
    b[0]  += r * u[n+1, 0]
    b[-1] += r * u[n+1, -1]

    u[n+1, 1:-1] = np.linalg.solve(A, b)

print("Solution matrix (rows = time steps, columns = x):\n")
print(np.round(u, 4))

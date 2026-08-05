# power method   2 -1 0 -1 2 -1 0 -1 2     ans 3.14    0.7 -1 0.7    8


import numpy as np

N = 3

def get_matrix():
    print("Enter the elements of the matrix row-wise:")
    A = []
    for i in range(N):
        row = []
        for j in range(N):
            val = float(input(f"  Enter element [{i+1}][{j+1}]: "))
            row.append(val)
        A.append(row)
    print()
    return np.array(A)

A = get_matrix()

x = np.ones(N)
tol = 0.001
err = 1
count = 0

eigen_old = 0

while err > tol:
    y = np.dot(A, x)
    eigen_new = max(abs(y))
    if eigen_new == 0:
        print("Power method failed: zero vector encountered.")
        break
    x = y / eigen_new

    err = abs(eigen_new - eigen_old)

    eigen_old = eigen_new
    count += 1

    
    print("Eigenvalue =", eigen_new)
    print("Eigenvector =", x)
    print()

print("Dominant Eigenvalue =", eigen_new)
print("Corresponding Eigenvector =", x)
print("Number of iterations =", count)


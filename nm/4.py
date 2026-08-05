# Gauss-Elimination Method by partial pivoting method  3 2 3 18 1 4 9 16 2 1 1 10   ans 7 -9 5

def input_matrix(name="Matrix"):
    print(f"Enter values for {name}:")
    a = [[0.0 for j in range(4)] for i in range(3)]
    for i in range(3):
        for j in range(4):
            a[i][j] = float(input(f"Enter a[{i+1}][{j+1}]: "))
    print()
    return a

def print_matrix(a, name="Matrix"):
    print(name)
    for row in a:
        print(" ".join(f"{x:8.3f}" for x in row))
    print()

def gauss_elimination(a):
    n = 3
    for i in range(n):
        row = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[row][i]):
                row = j
        if row != i:
            a[i], a[row] = a[row], a[i]

        for k in range(i + 1, n):
            factor = a[k][i] / a[i][i]
            for j in range(i, n + 1):
                a[k][j] -= factor * a[i][j]

        print(f"Step {i+1}:")
        print_matrix(a)

    x = [0.0 for i in range(n)]
    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += a[i][j] * x[j]
        x[i] = (a[i][n] - sum) / a[i][i]
    
    print("Solution:")
    print(f"x = {x[0]:.4f}")
    print(f"y = {x[1]:.4f}")
    print(f"z = {x[2]:.4f}")

a = input_matrix("Matrix A")
print("Initial Matrix:")
print_matrix(a)
gauss_elimination(a)

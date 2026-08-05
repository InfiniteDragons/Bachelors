# Gauss-Jordan Method  1 1 1 6 2 -1 1 3 1 2 -1 3    ans 1.2 2.1 2.5

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

def gauss_jordan(a):
    n = 3
    for i in range(n):
        if a[i][i] == 0:
            print("No unique solution exists.")
            return
        pivot = a[i][i]
        for j in range(n + 1):
            a[i][j] /= pivot
        for k in range(n):
            if k != i:
                factor = a[k][i]
                for j in range(n + 1):
                    a[k][j] -= factor * a[i][j]
        print(f"Step {i+1}:")
        print_matrix(a)

    print("Solution:")
    print(f"x = {a[0][3]:.4f}")
    print(f"y = {a[1][3]:.4f}")
    print(f"z = {a[2][3]:.4f}")

a = input_matrix("Matrix A")
print("Initial Matrix:")
print_matrix(a)
gauss_jordan(a)

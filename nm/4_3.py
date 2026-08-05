#gauss seidel method 

n = 3

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

def gaussseidel(a):
    for i in range(n):
        


a = input_matrix("Matrix A")
print("Initial Matrix:")
print_matrix(a)
gaussseidel(a)


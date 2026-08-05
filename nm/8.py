#laplace equation using gauss seidel iteration method
#0   80  100  80  0
#50               50
#60               60
#50               50
#0   80  100  80  0

n = 5

x = [[0 for j in range(n)] for i in range(n)]

tol = 0.001
error = 1

x[0] = [0, 80, 100, 80, 0]
x[4] = [0, 80, 100, 80, 0]
x[1][0] = 50
x[2][0] = 60
x[3][0] = 50
x[1][4] = 50
x[2][4] = 60
x[3][4] = 50

while error > tol:
    error = 0
    for i in range(1,n-1):
        for j in range(1,n-1):
            old = x[i][j]
            x[i][j] = (x[i-1][j] + x[i+1][j] + x[i][j-1] + x[i][j+1]) / 4
            if abs(x[i][j] - old)>error:
                error = abs(x[i][j]-old)

print("Solution of Laplace Equation:\n")

for row in x:
    for value in row:
        print(f"{value:7.2f}",end=" ")
    print()

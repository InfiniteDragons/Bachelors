# system of 2nd order RK-4 method  finite difference (y' = y(i+1) - y(i-1))/2h, y'' = (y(i+1) - 2*y(i) + y(i-1))/h^2

#y" + xy' + y = 3*x^2 + 2 y(0)=0, y(1)=1, y=?, h = 0.25

# Finite Difference Method
# y" + xy' + y = 3x^2 + 2
# y(0)=0, y(1)=1
# h = 0.25

x0 = 0
y0 = 0
xn = 1
yn = 1
h = 0.25

n = int((xn-x0)/h)

A = [[0 for j in range(n-1)] for i in range(n-1)]
B = [0 for i in range(n-1)]

for i in range(1, n):
    x = x0 + i*h

    f = (1/(h**2)) + (x/(2*h))
    g = (-2/(h**2)) + 1
    p = (1/(h**2)) - (x/(2*h))
    q = 3*x**2 + 2

    if i != 1:
        A[i-1][i-2] = p

    A[i-1][i-1] = g

    if i != n-1:
        A[i-1][i] = f

    B[i-1] = q

# Apply boundary conditions
B[0] = B[0] - p*y0
B[n-2] = B[n-2] - f*yn

print("Coefficient Matrix (A)")
for row in A:
    print(row)

print("\nConstant Matrix (B)")
for i in B:
    print(i)

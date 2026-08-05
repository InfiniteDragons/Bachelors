# Lagrange Interpolation Method   1 2 3 4 5   1 4 9 16 25   3.25  10.5625

def lagrange_interpolation(x, y, xp):
    n = len(x)
    yp = 0
    for i in range(n):
        temp = y[i]
        for j in range(n):
            if i != j:
                temp = temp * (xp - x[j]) / (x[i] - x[j])
        yp += temp
    return yp

n = int(input("Enter number of data: "))
x = []
y = []
print("Enter values of x:")
for i in range(n):
    x.append(float(input(f"x[{i}] = ")))
print("Enter values of y:")
for i in range(n):
    y.append(float(input(f"y[{i}] = ")))
xp = float(input("Enter interpolation point: "))
result = lagrange_interpolation(x, y, xp)
print(f"\nInterpolated value at yp = {result}")

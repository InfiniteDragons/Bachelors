#ordinary differential equation 1. RK-4 method 2. Finite difference method 3. Shooting method
# 1st order RK-4 method
#dy/dx = (y^2 - x^2)/(y^2 + x^2), n = 10 , y(0) = 1, y(2) = ?

x0 = 0
y0 = 1
xn = 2
n = 10
h = (xn - x0)/n

for i in range(1, n + 1):
    k1 = h * ((y0**2 - x0**2) / (y0**2 + x0**2))
    k2 = h * (((y0 + k1/2)**2 - (x0 + h/2)**2) /((y0 + k1/2)**2 + (x0 + h/2)**2))
    k3 = h * (((y0 + k2/2)**2 - (x0 + h/2)**2) /((y0 + k2/2)**2 + (x0 + h/2)**2))
    k4 = h * (((y0 + k3)**2 - (x0 + h)**2) /((y0 + k3)**2 + (x0 + h)**2))

    k = (k1 + 2*k2 + 2*k3 + k4) / 6

    y0 = y0 + k
    x0 = x0 + h

    print(f"{x0:.1f}\t{y0:.6f}")

print(f"\ny({xn}) = {y0:.6f}")

# system of 2nd order RK-4 method

#y" = xy'^2 - y^2 y(0)=1, y'(0)=0, y=?, x=0.2

def f(x, y, z):
    return z 

def g(x, y, z):
    return x*(z**2) - y**2

x0 = 0
y0 = 1
z0 = 0
h = 0.1

for i in range(2):
    k1 = h * f(x0, y0, z0)
    l1 = h * g(x0, y0, z0)

    k2 = h * f(x0 + h/2, y0 + k1/2, z0 + l1/2)
    l2 = h * g(x0 + h/2, y0 + k1/2, z0 + l1/2)

    k3 = h * f(x0 + h/2, y0 + k2/2, z0 + l2/2)
    l3 = h * g(x0 + h/2, y0 + k2/2, z0 + l2/2)

    k4 = h * f(x0 + h, y0 + k3, z0 + l3)
    l4 = h * g(x0 + h, y0 + k3, z0 + l3)

    y0 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
    z0 = z0 + (l1 + 2*l2 + 2*l3 + l4) / 6
    x0 = x0 + h

    print(f"x = {x0:.1f}, y = {y0:.6f}, y' = {z0:.6f}")

print(f"\ny({x0}) = {y0:.6f}")
print(f"z({x0}) = {z0:.6f}")
 
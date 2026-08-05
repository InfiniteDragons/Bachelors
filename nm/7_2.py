# system of 1st order RK-4 method


def f(x, y, z):
    return x * z + 1

def g(x, y, z):
    return -(x ** y)

x0 = 0
y0 = 0
z0 = 1
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

    k = (k1 + 2*k2 + 2*k3 + k4) / 6
    l = (l1 + 2*l2 + 2*l3 + l4) / 6

    y0 += k
    z0 += l
    x0 += h

    print(f"{x0:.1f}\t{y0:.6f}\t{z0:.6f}")

print(f"\ny({x0}) = {y0:.6f}")
print(f"z({x0}) = {z0:.6f}")

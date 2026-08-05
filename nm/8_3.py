#1-D heat equation using Bendre-Schmidt method
# ut = uxx
# boundary value: 1. u(0,t) = u(1,t)
#                 2. u(x,0) = sin pi x
# h = 0.2  k = 0.02   0<=x<=1  0<=t<=0.1

from math import sin, pi

h = 0.2
k = 0.02
r = k / (h*h)

nx = int(1/h) + 1
nt = int(0.1/k)
x = []

for i in range(nx):
    x.append(i*h)

u = []
for xi in x:
    u.append(sin(pi*xi))

u[0] = 0
u[nx-1] = 0

print("Initial Values (t = 0)")
for i in range(nx):
    print(f"{u[i]:7.4f}", end=" ")
print()

for t in range(nt):
    new = u[:]
    for i in range(1, nx-1):
        new[i] = (u[i-1] + u[i+1]) / 2
    new[0] = 0
    new[nx-1] = 0
    u = new
    print(f"\nt = {(t+1)*k:.2f}")
    for i in range(nx):
        print(f"{u[i]:7.4f}", end=" ")
    print()

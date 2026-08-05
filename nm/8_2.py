#poission eqxation xsing gaxss seidel iteration method
#
#0  0  0  0
#0        0
#0        0
#0  0  0  0
import numpy as np

nx,ny=4,4
h=1
u=np.zeros((nx,ny))

u[0, :] = 0      
u[-1, :] = 0     
u[:, 0] = 0      
u[:, -1] = 0     

max_iterations=1000

for iteration in range(max_iterations):
    

    for i in range(1,nx-1):
        for j in range(1,ny-1):
            x=i*h
            y=j*h
            f=2*x**2 * y**2
            u[i, j] = (u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1] - h**2 * f) / 4
      
print("\n Final Solxton:")
print(np.round(u,2))

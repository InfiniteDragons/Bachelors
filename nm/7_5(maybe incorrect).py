# Shooting Method
# y" + xy' + y = 3x^2 + 2
# y(0)=0, y(1)=1, h=0.25

def f(x, y, z):
    return z

def g(x, y, z):
    return 3*x*x + 2 - y - x*z

x0, y0, xn, yn, h = 0, 0, 1, 1, 0.25

def rk4(s):
    x, y, z = x0, y0, s
    while x < xn:
        k1 = h*f(x,y,z)      
        l1 = h*g(x,y,z)

        k2 = h*f(x+h/2,y+k1/2,z+l1/2)
        l2 = h*g(x+h/2,y+k1/2,z+l1/2)
        
        k3 = h*f(x+h/2,y+k2/2,z+l2/2)
        l3 = h*g(x+h/2,y+k2/2,z+l2/2)
        
        k4 = h*f(x+h,y+k3,z+l3)       
        l4 = h*g(x+h,y+k3,z+l3)

        y += (k1+2*k2+2*k3+k4)/6
        z += (l1+2*l2+2*l3+l4)/6
        x += h
    return y

s1, s2 = 0, 1
y1 = rk4(s1)
y2 = rk4(s2)

s = s1 + (yn-y1)*(s2-s1)/(y2-y1)

print("Correct Initial Slope =", round(s,6))
print("y(1) =", round(rk4(s),6))

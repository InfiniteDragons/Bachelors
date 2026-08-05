# numerical integration  gauss legendre method 2point
# I = ∫0^6 1/(1+x^2) dx  
# u1 = −0.5773502692 u2 = 0.5773502692

u = 6
l = 0
w1 =1
w2 = 1

u1 = float(input("Enter the first root of the Legendre polynomial: "))
u2 = float(input("Enter the second root of the Legendre polynomial: "))

t1 = ((u-l) * u1 /2) + ((u+l)/2)
t2 = ((u-l) * u2 /2) + ((u+l)/2)

ft1 = 1/(1+t1**2)
ft2 = 1/(1+t2**2)

I = (u-l)* ((w1 *ft1) + (w2 * ft2)) /2
print("The value of the integral using 2 point Gauss-Legendre method is:", I)

# numerical integration  1.trapezoid rule  2.Simpson's 1/3 rule  3.simpson's 3/8 rule  4. booles rule  5. gauss legendre method
# I = ∫0^6 1/(1+x^2) dx

u = 6
l = 0
n = int(input("Enter the number of subintervals: "))
h = (u - l) / n

fx = 1 / (1 + l**2) + 1 / (1 + u**2)

for i in range(1, n):
    x = l + i * h
    fx += 2 * (1 / (1 + x**2))

I = (h / 2) * fx
print("The value of the integral using trapezoidal rule is:", I)

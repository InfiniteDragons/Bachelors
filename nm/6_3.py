# numerical integration  Simpson's 3/8 rule 
# I = ∫0^6 1/(1+x^2) dx

u = 6
l = 0
n = int(input("Enter the number of subintervals: "))
while n % 3 != 0:
    print("Invalid number of subintervals forSimpson's 3/8 rule!!!")
    print("Please enter a multiple of 3 for the number of subintervals.")
    n = int(input("Enter the number of subintervals: "))
h = (u - l) / n

fx = 1 / (1 + l**2) + 1 / (1 + u**2)

for i in range(1, n):
    x = l + i * h
    if i % 3 == 0:
        fx += 2 * (1 / (1 + x**2))
    else:
        fx += 3 * (1 / (1 + x**2))

I = (3 * h / 8) * fx
print("The value of the integral using Simpson's 3/8 rule is:", I)

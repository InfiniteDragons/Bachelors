# numerical integration  Simpson's 1/3 rule 
# I = ∫0^6 1/(1+x^2) dx

u = 6
l = 0
n = int(input("Enter the number of subintervals: "))
while n % 2 != 0:
    print("Invalid number of subintervals forSimpson's 1/3 rule!!!")
    print("Please enter an even number of subintervals.")
    n = int(input("Enter the number of subintervals: "))
h = (u - l) / n

fx = 1 / (1 + l**2) + 1 / (1 + u**2)

for i in range(1, n):
    x = l + i * h
    if i % 2 == 0:
        fx += 2 * (1 / (1 + x**2))
    elif i % 2 != 0:
        fx += 4 * (1 / (1 + x**2))

I = (h / 3) * fx
print("The value of the integral using Simpson's 1/3 rule is:", I)

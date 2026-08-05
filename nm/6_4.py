# numerical integration  booles rule 
# I = ∫0^6 1/(1+x^2) dx

u = 6
l = 0
n = int(input("Enter the number of subintervals: "))
while n % 4 != 0:
    print("Invalid number of subintervals for Boole's rule!!!")
    print("Please enter a multiple of 4 for the number of subintervals.")
    n = int(input("Enter the number of subintervals: "))
h = (u - l) / n

fx = 7 * (1 / (1 + l**2)) + 7 * (1 / (1 + u**2))

for i in range(1, n):
    x = l + i * h
    y = 1 / (1 + x**2)

    if i % 4 == 0:
        fx += 14 * y
    elif i % 4 == 2:
        fx += 12 * y
    else:          # i % 4 == 1 or 3
        fx += 32 * y

I = (2 * h / 45) * fx
print("The value of the integral using Boole's rule is:", I)

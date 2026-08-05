## Bisection method for f(x) = x*x - 5*x - 6

def bisection(a, b, fa, fb):
    i = 1
    while True:
        m = (a + b) / 2
        fm = m*m - 5*m - 6
        fa = a*a - 5*a - 6
        fb = b*b - 5*b - 6
        print(i, ". a= ", "%.2f" % a, " b= ", "%.2f" % b, " m= ", "%.2f" % m, " f(a)= ", "%.2f" % fa, " f(b)= ", "%.2f" % fb, " f(m)= ", "%.2f" % fm)
        if fm * fa <0:
            b = m
        elif fm * fb < 0:
            a = m
        if abs(fm) < 0.01:
            print("The root is: ", "%.2f" % m)
        i += 1

def main():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    fa = a*a - 5*a - 6
    fb = b*b - 5*b - 6
    if fa*fb > 0:
        print("Invalid input!!!\n")
        main()
    else:
        bisection(a, b, fa, fb)
    

if __name__ == "__main__":
    main()

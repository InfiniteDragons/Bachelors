## f(x) = 4*sin(x) - exp(x)

import math

def nr(x0, fx, dfx):
    while True:
        x1 = x0 - fx/dfx
        print("x0= ", "%.2f" % x0, " f(x0)= ", "%.2f" % fx, " f'(x0)= ", "%.2f" % dfx, " x1= ", "%.2f" % x1)
        if abs(x1 - x0) < 0.01:
            print("The root is: ", "%.2f" % x1)
            break
        x0 = x1
        fx = 4 * math.sin(x1) - math.exp(x1)
        dfx = 4 * math.cos(x1) - math.exp(x1)

def main():
    x0 = float(input("Enter the initial guess: "))
    fx = 4 * math.sin(x0) - math.exp(x0)
    dfx = 4 * math.cos(x0) - math.exp(x0)
    if dfx == 0:
        print("Derivative is zero. No solution found.")
        main()
    else:
        nr(x0, fx, dfx)

if __name__ == "__main__":
    main()

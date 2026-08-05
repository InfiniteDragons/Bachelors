## NR Method for f(x) = x*x - 4x - 10

import matplotlib.pyplot as plt
import numpy as np

def plot_graph(root, x0):
    x = np.linspace(-2, 20, 250)
    y = x**2 - 4*x - 10

    y0 = x0*x0 - 4*x0 - 10
    slope = 2*x0 - 4

    tangent = y0 + slope * (x - x0)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='f(x) = x² - 4x - 10')

    plt.plot(x, tangent, '--', label=f'Tangent at x₀ = {x0:.2f}')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Newton-Raphson Method')
    plt.grid(True)
    plt.legend()
    plt.show()

def nr(x0, fx, dfx):
    i = 1
    while True:
        x1 = x0 - fx/dfx
        print("%d." % i, "x0= ", "%.2f" % x0, " f(x0)= ", "%.2f" % fx, " f'(x0)= ", "%.2f" % dfx, " x1= ", "%.2f" % x1)
        if abs(x1 - x0) < 0.01:
            print("The root is: ", "%.2f" % x1)
            break
        x0 = x1
        fx = x1*x1 - 4*x1 - 10
        dfx = 2*x1 - 4
        i += 1

def main():
    x0 = float(input("Enter the initial guess: "))
    fx = x0*x0 - 4*x0 - 10
    dfx = 2*x0 - 4
    if dfx == 0:
        print("Derivative is zero. No solution found.")
        main()
    else:
        nr(x0, fx, dfx)
    root = nr(x0, fx, dfx)
    plot_graph(root, x0)

if __name__ == "__main__":
    main()

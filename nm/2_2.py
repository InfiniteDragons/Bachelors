## Secant Method for f(x) = x*x - 4x - 10

import matplotlib.pyplot as plt
import numpy as np

def plot_graph(root):
    x = np.linspace(-2, 20, 250)
    y = x**2 - 4*x - 10

    #slope = root.x

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='f(x) = x² - 4x - 10')

    plt.plot(root, 0, color = 'red', marker = 'o', label=f'Root at x = {root:.2f}')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Secant Method')
    plt.grid(True)
    plt.legend()
    plt.show()

def secant(x0, x1, fx0, fx1):
    i = 1
    while True:
        x = x0 - fx0*((x1-x0)/(fx1-fx0))
        print("%d." % i, "x0= ", "%.2f" % x0, " f(x0)= ", "%.2f" % fx0, " x1= ", "%.2f" % x1, " f(x1)= ", "%.2f" % fx1)
        if abs(x - x1) < 0.01:
            print("The root is: ", "%.2f" % x)
            break
        x0 = x1
        x1 = x
        fx0 = fx1
        fx1 = x1*x1 - 4*x1 - 10
        i += 1

def main():
    x0 = float(input("Enter the first end: "))
    x1 = float(input("Enter the second end: "))
    fx0 = x0*x0 - 4*x0 - 10
    fx1 = x1*x1 - 4*x1 - 10
    if fx0*fx1 == 0:
        print("No solution found.")
        main()
    else:
        secant(x0, x1, fx0, fx1)
    root = secant(x0, x1, fx0, fx1)
    plot_graph(root)

if __name__ == "__main__":
    main()

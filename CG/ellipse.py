import pygame as py
import sys

def midpoint_ellipse(screen, xc, yc, a, b, color):
    rx = a
    ry = b

    x = 0
    y = ry

    #region1
    p1 = (ry * ry) - (rx * rx * ry) + ( rx * rx / 4)
    while (2 * ry * ry * x) <= (2 * rx * rx * y):
        screen.set_at((xc + x, yc + y), color)
        screen.set_at((xc - x, yc + y), color)
        screen.set_at((xc + x, yc - y), color)
        screen.set_at((xc - x, yc - y), color)
        if p1 < 0:
            x  = x + 1
            y  = y
            p1 = p1 + (2 * ry * ry * x) + (ry * ry)
        else:
            x  = x + 1
            y  = y - 1
            p1 = p1 + (2 * ry * ry * x) - (2 * rx * rx * y) + (ry * ry)

    #region2
    p2 = (ry * ry) * ((x + 1/2) * (x + 1/2)) + (rx * rx) * ((y - 1) * (y - 1)) - (rx * rx * ry * ry)
    while y >= 0:
        screen.set_at((xc + x, yc + y), color)
        screen.set_at((xc - x, yc + y), color)
        screen.set_at((xc + x, yc - y), color)
        screen.set_at((xc - x, yc - y), color)
        if p2 > 0:
            x  = x
            y  = y - 1
            p2 = p2 - (2 * rx * rx * y) + (rx * rx)
        else:
            x  = x + 1
            y  = y - 1
            p2 = p2 + (2 * ry * ry * x) - (2 * rx * rx * y) + (rx * rx)


def main():
    py.init()
    width, height = 600, 600
    screen = py.display.set_mode((width, height))
    py.display.set_caption("Midpoint Ellipse Algorithm")
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
        screen.fill(BLACK)
        # midpoint_ellipse(screen, xc, yc, a, b, WHITE)
        midpoint_ellipse(screen, 300, 300, 150, 100, WHITE)
        # midpoint_ellipse(screen, 300, 300, 100, 150, WHITE)
        # midpoint_ellipse(screen, 300, 300, 200, 50, WHITE)
        # midpoint_ellipse(screen, 300, 300, 50, 200, WHITE)

        py.display.flip()
    py.quit()
    sys.exit()

if __name__ == "__main__":
    main()

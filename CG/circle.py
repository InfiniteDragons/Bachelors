import pygame as py
import sys

def circle(screen, xc, yc, r, color):
    x = 0
    y = r
    p = 1 - r

    while x < y:
        screen.set_at((xc + x, yc + y), color)
        screen.set_at((xc - x, yc + y), color)
        screen.set_at((xc + x, yc - y), color)
        screen.set_at((xc - x, yc - y), color)
        screen.set_at((xc + y, yc + x), color)
        screen.set_at((xc - y, yc + x), color)
        screen.set_at((xc + y, yc - x), color)
        screen.set_at((xc - y, yc - x), color)
        x = x + 1
        if p < 0:
            p = p + (2*x) + 1
        else:
            y = y - 1
            p = p + (2*x) - (2*y) + 1

def halfcircle(screen, xc, yc, r, color):
    x = 0
    y = r
    p = 1 - r

    while x < y:
        screen.set_at((xc + x, yc + y), color)
        screen.set_at((xc - x, yc + y), color)
        screen.set_at((xc + y, yc + x), color)
        screen.set_at((xc - y, yc + x), color)
        x = x + 1
        if p < 0:
            p = p + (2*x) + 1
        else:
            y = y - 1
            p = p + (2*x) - (2*y) + 1

def main():
    py.init()
    width, height = 600, 600
    screen = py.display.set_mode((width, height))
    py.display.set_caption("Midpoint Circle Algorithm")
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
        screen.fill(BLACK)
        circle(screen, 300, 300, 100, WHITE)
        circle(screen, 270, 270, 20, WHITE)
        circle(screen, 330, 270, 20, WHITE)
        halfcircle(screen, 300, 330, 20, WHITE)
        py.display.flip()
    py.quit()
    sys.exit()

if __name__ == "__main__":
    main()

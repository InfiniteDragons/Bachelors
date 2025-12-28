# Bresenham's Line drawing algorithm
import pygame as pg
import sys


def Bla(screen, x1, y1, x2, y2, color):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    
    x = x1
    y = y1
    
    if (x2 > x1):
        lx = 1
    else:
        lx = -1
    
    if (y2 > y1):
        ly = 1
    else:
        ly = -1

    if dx > dy:
        p = (2*dy)-dx
        for i in range(0, dx):
            if (p < 0):
                x = x+lx
                y = y
                p = p+(2*dy)
            else:
                x = x+lx
                y = y+ly
                p = p+(2*dy)-2*dx
            screen.set_at((round(x), round(y)), color)
    else:
        p = (2*dx)-dy
        for i in range(0, dy):
            if (p < 0):
                x = x
                y = y+ly
                p = p+2*dx
            else:
                x = x+lx
                y = y+ly
                p = p+2*dx-2*dy
            screen.set_at((round(x), round(y)), color)

def main():
    pg.init()
    width, height = 600, 600
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("BLA line")
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill(BLACK)
        Bla(screen, 100, 100, 500, 100, WHITE)
        Bla(screen, 100, 100, 100, 300, WHITE)
        Bla(screen, 500, 100, 500, 300, WHITE)
        Bla(screen, 100, 300, 500, 300, WHITE)
        
        Bla(screen, 300, 100, 300, 300, WHITE)
        
        Bla(screen, 100, 125, 200, 125, WHITE)
        Bla(screen, 100, 275, 200, 275, WHITE)
        Bla(screen, 400, 125, 500, 125, WHITE)
        Bla(screen, 400, 275, 500, 275, WHITE)
        
        Bla(screen, 200, 125, 200, 275, WHITE)
        Bla(screen, 400, 125, 400, 275, WHITE)

        Bla(screen, 100, 150, 125, 150, WHITE)
        Bla(screen, 100, 250, 125, 250, WHITE)
        Bla(screen, 475, 150, 500, 150, WHITE)
        Bla(screen, 475, 250, 500, 250, WHITE)

        Bla(screen, 125, 150, 125, 250, WHITE)
        Bla(screen, 475, 150, 475, 250, WHITE)
        
        pg.display.flip()
        pg.display.update()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()

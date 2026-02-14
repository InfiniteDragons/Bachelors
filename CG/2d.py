import pygame as pg
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

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
        for i in range(0, int(dy)):
            if (p < 0):
                x = x
                y = y+ly
                p = p+2*dx
            else:
                x = x+lx
                y = y+ly
                p = p+2*dx-2*dy
            screen.set_at((round(x), round(y)), color)

def translation(screen, x1, y1, x2, y2, tx, ty):
    x1new = x1 + tx
    y1new = y1 + ty
    x2new = x2 + tx
    y2new = y2 + ty
    Bla(screen, round(x1new), round(y1new), round(x2new), round(y2new), GREEN)

def scaling(screen, x1, y1, x2, y2, sx, sy, cx, cy):
    x1new = cx + sx * (x1 - cx)
    y1new = cy + sy * (y1 - cy)
    x2new = cx + sx * (x2 - cx)
    y2new = cy + sy * (y2 - cy)
    Bla(screen, round(x1new), round(y1new), round(x2new), round(y2new), RED)

def reflection(screen, x1, y1, x2, y2, axis, cx, cy):
    def reflect(x, y):
        x = x - cx
        y = y - cy
        if axis == 'x':
            y = -y
        elif axis == 'y':
            x = -x
        elif axis == 'origin':
            x = -x
            y = -y
        return (x + cx, y + cy)    
    return reflect(x1,y1)+reflect(x2,y2)

def rotation(screen, x1, y1, x2, y2, angle, cx, cy):
    import math
    rad = math.radians(angle)
    cos_theta = math.cos(rad)
    sin_theta = math.sin(rad)
    def rotate(x, y):
        x = x - cx
        y = y - cy
        xnew = x * cos_theta - y * sin_theta
        ynew = x * sin_theta + y * cos_theta
        return (xnew + cx, ynew + cy)
    return rotate(x1,y1)+rotate(x2,y2)

def main():
    pg.init()
    width, height = 600, 600
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("2D Transformation Line Drawing")
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill(BLACK)

        Bla(screen, 100, 100, 500, 100, WHITE)

        translation(screen, 100, 100, 500, 100, 50, 50)
        
        scaling(screen, 100, 100, 500, 100, 0.5, 0.5, 300, 300)
        
        a,b,c,d = reflection(screen, 100, 100, 500, 100, 'x', 300, 300)
        Bla(screen, a,b,c,d, BLUE)

        e,f,g,h = rotation(screen, 100, 100, 500, 100, 45, 300, 300)
        Bla(screen, e,f,g,h, ORANGE)

        pg.display.flip()
        pg.display.update()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()

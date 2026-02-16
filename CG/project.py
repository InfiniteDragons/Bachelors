import pygame as pg
import sys
import math

clock = pg.time.Clock()
width, height = 1500, 750
CENTER = (width // 2, height // 2)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


def draw_circle(screen, xc, yc, r, color):
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        screen.set_at((xc + x, yc + y), color)
        screen.set_at((xc - x, yc + y), color)
        screen.set_at((xc + x, yc - y), color)
        screen.set_at((xc - x, yc - y), color)
        screen.set_at((xc + y, yc + x), color)
        screen.set_at((xc - y, yc + x), color)
        screen.set_at((xc + y, yc - x), color)
        screen.set_at((xc - y, yc - x), color)

        x =  x + 1   
        if p < 0:
            p = p + (2*x) + 1
        else:
            y = y - 1
            p = p + (2*x) - (2*y) + 1


# ===============================
# PLANET CLASS
# ===============================
class Planet:
    def __init__(self, orbit_radius, size, color, speed):
        self.rx = orbit_radius
        self.ry = int(orbit_radius * 0.6)
        self.size = size
        self.color = color
        self.angle = 0
        self.speed = speed

    def update(self):
        self.angle += self.speed

    def draw(self, surface):
        x = CENTER[0] + int(math.cos(self.angle) * self.rx)
        y = CENTER[1] + int(math.sin(self.angle) * self.ry)

        draw_circle(surface, x, y, self.size, self.color)


# ===============================
# CREATE PLANETS
# ===============================
planets = [
    Planet(100, 8, GRAY, 0.02),     # Mercury
    Planet(170, 10, WHITE, 0.015),  # Venus
    Planet(250, 12, BLUE, 0.01),    # Earth
    Planet(340, 9, RED, 0.008),     # Mars
    Planet(450, 20, YELLOW, 0.006), # Jupiter
    Planet(550, 18, GRAY, 0.004),   # Saturn
    Planet(650, 16, BLUE, 0.002),   # Uranus
    Planet(750, 14, RED, 0.001),    # Neptune
]


def draw_orbit(screen, xc, yc, rx, ry, color):
    x = 0
    y = ry

    # For Region 1
    p1 = ry * ry - rx * rx * ry + 0.25 * rx * rx
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    while dx < dy:
        screen.set_at((xc + x, yc + y), color)
        screen.set_at((xc - x, yc + y), color)
        screen.set_at((xc + x, yc - y), color)
        screen.set_at((xc - x, yc - y), color)
        if p1 < 0:
            x = x + 1
            dx = 2 * ry * ry * x
            p1 = p1 + dx + ry * ry
        else:
            x = x + 1
            y = y - 1
            dx = 2 * ry * ry * x
            dy = 2 * rx * rx * y
            p1 = p1 + dx - dy + ry * ry

    # For Region 2
    p2 = (ry * ry) * ((x + 0.5) ** 2) + (rx * rx) * ((y - 1) ** 2) - (rx * rx * ry * ry)

    while y >= 0:
        screen.set_at((xc + x, yc + y), color)
        screen.set_at((xc - x, yc + y), color)
        screen.set_at((xc + x, yc - y), color)
        screen.set_at((xc - x, yc - y), color)
        if p2 > 0:
            y = y - 1
            dy = 2 * rx * rx * y
            p2 = p2 + rx * rx - dy
        else:
            y = y - 1
            x = x + 1
            dx = 2 * ry * ry * x
            dy = 2 * rx * rx * y
            p2 = p2 + dx - dy + rx * rx

  
def main():
    pg.init() 
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Computer Graphics Project")
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill(BLACK)

        # Draw Sun
        for i in range(30, 0, -1):
            draw_circle(screen, CENTER[0], CENTER[1], i, (255, 255 - i*8, 0))

        # Draw orbits
        for p in planets:
            draw_orbit(screen, CENTER[0], CENTER[1], p.rx, p.ry, (80, 80, 80))

        # Update and draw planets
        for p in planets:
            for i in range(p.size, 0, -1):
                draw_circle(screen, CENTER[0]+int(math.cos(p.angle)*p.rx), CENTER[1]+int(math.sin(p.angle)*p.ry), i, (p.color[0], p.color[1], p.color[2]))
            p.update()
            p.draw(screen)

        pg.display.flip()
        pg.display.update()
        clock.tick(60)
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()

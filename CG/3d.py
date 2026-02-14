import pygame as pg
import math
import sys
cube_vertices = [(-50, -50, -50), (-50, 50, -50), (50, 50, -50),
                 (50, -50, -50), (-50, -50, 50), (-50, 50, 50), (50, 50, 50), (50, -50, 50)]
WIDTH, HEIGHT = 700, 800
screen = pg.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
cube_edge = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]


def translate(vertices, tx, ty, tz):
    result = []
    for x, y, z in vertices:
        result.append((x+tx, y+ty, z+tz))
    return result


def rotate(vertices, angle):
    result = []
    rad = math.radians(angle)

    for x, y, z in vertices:
        x1 = x*math.cos(rad)-z*math.sin(rad)
        z1 = x*math.sin(rad)+z*math.cos(rad)
        result.append((x1, y, z1))
    return result


def scaling(vertices, sx, sy, sz):
    result = []
    for x, y, z in vertices:
        result.append((x*sx, y*sy, z*sz))
    return result


def reflect(vertices):
    result = []
    for x, y, z in vertices:
        result.append((-x, -y, z))
    return result


def projection(point):
    x, y, z = point
    distance = 200
    scale = distance/(distance-z)
    screen_x = x+WIDTH//2
    screen_y = -y+HEIGHT//2
    screen_x *= scale
    screen_y *= scale
    return (int(screen_x), int(screen_y))


def draw_cube(vertices):
    projected = []
    for v in vertices:
        projected.append(projection(v))
    for edge in cube_edge:
        start = projected[edge[0]]
        end = projected[edge[1]]
        pg.draw.line(screen, WHITE, start, end)


def main():
    pg.init()
    pg.display.set_caption("3-D transformation")
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill(BLACK)
        cube = cube_vertices
        translated = translate(cube, 10, 10, 10)
        rotated = rotate(cube, 30)
        scaled = scaling(cube, 1.4, 1.4, 1.4)
        reflection = reflect(cube)
        # draw_cube(cube)
        # draw_cube(translated)
        # draw_cube(rotated)
        draw_cube(scaled)
        # draw_cube(reflection)
        # pg.display.flip()
        pg.display.update()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()

import pygame
from pygame.locals import *

width = 200
height = 200

min_val = -0.5
max_val = 0.5

min_slider_value = -2.5
max_slider_value = 2.5

slider_max_v = max_slider_value
slider_min_v = min_slider_value
start = 1

max_iterations = 100

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def map_value(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()

    if (slider_max_v != max_slider_value or slider_min_v != min_slider_value or start):
        slider_max_v = max_slider_value
        slider_min_v = min_slider_value
        start = 0

        pixels = pygame.surfarray.pixels2d(screen)
        for x in range(width):
            for y in range(height):
                a = map_value(x, 0, width, slider_min_v, slider_max_v)
                b = map_value(y, 0, height, slider_min_v, slider_max_v)
                ca = a
                cb = b
                n = 0

                while n < max_iterations:
                    aa = a * a - b * b
                    bb = 2 * a * b
                    a = aa + ca
                    b = bb + cb
                    if a * a + b * b > 16:
                        break
                    n += 1

                bright = map_value(n, 0, max_iterations, 0, 1)
                bright = map_value(bright ** 0.5, 0, 1, 0, 255)

                if n == max_iterations:
                    bright = 0

                pixels[x][y] = (bright, bright, bright)

        del pixels
        pygame.display.update()

    clock.tick(60)

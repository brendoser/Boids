# Herd Immunity Simulation
# Boids move around, boids interact with each other
# Boids infect other boids until the "pandemic" ends
# TODO: Define Rules (Infection)
# TBD

# Python Imports
import pygame as pg
import numpy as np
from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
)
from random import seed
from random import random

# Settings (to be put in config file or smth later)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
FRAMERATE = 30
BOID_COUNT = 100
#seed(1)

class Boid():
    def __init__(self, size, speed):
        super(Boid, self).__init__()
        self.size = size
        self.color = (random()*255, random()*255, random()*255)
        # Pick random position
        self.pos = np.array([0, 0], dtype=float)
        self.pos[0] = random() * (SCREEN_WIDTH - size) + size
        self.pos[1] = random() * (SCREEN_HEIGHT - size) + size
        # Pick random speed
        self.vel = np.array([0,0], dtype=float)
        direction = random() * 2 * np.pi
        print(direction)
        self.vel[0] = np.cos(direction) * speed
        self.vel[1] = np.sin(direction) * speed
        print(self.vel)

    def update(self):
        # Update Position
        self.pos += self.vel
        # Check for wall collision
        if not(self.size < self.pos[0] < SCREEN_WIDTH - self.size):
            self.vel[0] *= -1
        if not (self.size < self.pos[1] < SCREEN_HEIGHT - self.size):
            self.vel[1] *= -1

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.pos, self.size)

def main():
    # Initialize and create drawing window
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pg.time.Clock()

    boiz = []
    for i in range(BOID_COUNT):
        boiz.append(Boid(5, 5))


    # Run until the game ends
    running = 1
    while running:
        # Look at every event in the queue
        for event in pg.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False

        for boi in boiz:
            boi.update()

        screen.fill(0)

        for boi in boiz:
            boi.draw(screen)

        pg.display.flip()
        clock.tick(FRAMERATE)

    pg.quit()


if __name__ == '__main__':
    main()

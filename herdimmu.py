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
from random import random

# Settings (to be put in config file or smth later)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
FRAMERATE = 30

# Basic Simulation Settings
BOID_COUNT = 200
INFEC_RAD = 20 # Infectious Radius
BOID_SIZE = 5
BOID_SPEED = 5

# Color Scheme
color_sick = (255, 0, 0)
color_well = (0, 255, 255)

# This class stores health information on individuals
class attr():
    def __init__(self):
        self.sick = 0

# This class stores information for a single boid
class Boid():
    def __init__(self, size, speed):
        self.size = size
        self.color = color_well
        # Pick random position
        self.pos = np.array([0, 0], dtype=float)
        self.pos[0] = random() * (SCREEN_WIDTH - size) + size
        self.pos[1] = random() * (SCREEN_HEIGHT - size) + size
        # Pick random direction
        self.vel = np.array([0,0], dtype=float)
        direction = random() * 2 * np.pi
        self.vel[0] = np.cos(direction) * speed
        self.vel[1] = np.sin(direction) * speed
        # Health Attributes
        self.attr = attr()


    def update(self):
        # Update Position
        self.pos += self.vel
        # Check for wall collision
        if not(self.size < self.pos[0] < SCREEN_WIDTH - self.size):
            self.vel[0] *= -1
        if not (self.size < self.pos[1] < SCREEN_HEIGHT - self.size):
            self.vel[1] *= -1
        # Change color if infected
        if self.attr.sick == 1:
            self.color = color_sick

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.pos, self.size)

    def check_sick(self, sick_boiz):
        # Look for nearby boids that are sick, return 1 if they are within range
        close = 0
        for sick_boi in sick_boiz:
            # Do rough check using simple math
            if abs(self.pos[0] - sick_boi.pos[0]) < INFEC_RAD:
                if abs(self.pos[1] - sick_boi.pos[1]) < INFEC_RAD:

                    # Do more complex check
                    x_dist = abs(self.pos[0] - sick_boi.pos[0])
                    y_dist = abs(self.pos[1] - sick_boi.pos[1])
                    if (pow(x_dist, 2) + pow(y_dist, 2)) < pow(INFEC_RAD, 2):
                        self.attr.sick = 1
                        close = 1
        return close

def main():
    # Initialize and create drawing window
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pg.time.Clock()

    # Create boid groups
    healthy_boiz = []
    for i in range(BOID_COUNT):
        healthy_boiz.append(Boid(5, 5))

    sick_boiz = []
    sick_boiz.append(healthy_boiz[0])
    healthy_boiz.pop(0)
    sick_boiz[0].attr.sick = 1

    running = 1
    while running:
        # Look at every event in the queue
        for event in pg.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False

        # Draw blank screen
        screen.fill(0)

        # Update and draw healthy boids
        for i, boi in enumerate(healthy_boiz):
            boi.update()

            # This check compares each healthy boid to all sick boids
            near = boi.check_sick(sick_boiz)
            if near == 1:
                sick_boiz.append(boi)
                healthy_boiz.pop(i)
            else:
                boi.draw(screen)

        # Update and draw sick boids
        for boi in sick_boiz:
            boi.update()
            boi.draw(screen)

        pg.display.flip()
        clock.tick(FRAMERATE)

    pg.quit()


if __name__ == '__main__':
    main()

# Herd Immunity Simulation
# Boids move around, boids interact with each other
# Boids infect other boids until the "pandemic" ends
# Rules:
# TBD

# Imports
import pygame
import numpy as np

# Import Keys
from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
)

# Settings (to be put in config file or smth later)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300
FRAMERATE = 30

# Initialize and create drawing window
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

boid_speed = 30
boid_size = 5

boid_pos = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
boid_vel = [np.sqrt(boid_speed/2), np.sqrt(boid_speed/2)]

# Run until the game ends
running = True
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False


    boid_pos[0] += boid_vel[0]
    boid_pos[1] += boid_vel[1]

    if boid_pos[0] > SCREEN_WIDTH-boid_size or boid_pos[0] < boid_size:
        boid_vel[0] *= -1
    
    if boid_pos[1] > SCREEN_HEIGHT-boid_size or boid_pos[1] < boid_size:
        boid_vel[1] *= -1


    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 255), boid_pos, boid_size)
    pygame.display.flip()
    clock.tick(FRAMERATE)


pygame.quit()

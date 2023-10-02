import pygame
from constants import *
from pygame.locals import *

pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# TODO create player object

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    # TODO draw the player and call player's update method
    pygame.display.update()
    clock.tick(FPS)

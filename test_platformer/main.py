import pygame
from constants import *
from world import World
pygame.init()
clock = pygame.time.Clock()

game_world = World("")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    game_world.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
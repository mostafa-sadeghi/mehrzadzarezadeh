import pygame
from constants import *
from world import World
from levels.level1 import world_data
from player import Player
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg = pygame.image.load("assets/sky.png")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_rect = bg.get_rect()
bg_rect.topleft = (0, 0)


game_world = World(world_data)

my_player = Player(100, SCREEN_HEIGHT-170)


def draw_grid():
    for i in range(20):
        pygame.draw.line(screen, (255, 255, 255),
                         (i * TILE_SIZE, 0), (i*TILE_SIZE, SCREEN_HEIGHT))
    for j in range(14):
        pygame.draw.line(screen, (255, 255, 255),
                         (0, j * TILE_SIZE), (SCREEN_WIDTH, j * TILE_SIZE))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, bg_rect)
    draw_grid()
    my_player.draw(screen)
    my_player.update()
    game_world.draw(screen)
    pygame.display.update()

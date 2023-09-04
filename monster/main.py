import pygame
from game import Game

from player import Player
from config import *

pygame.init()

display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
FPS = 60
clock = pygame.time.Clock()
player = Player()

monster_group = pygame.sprite.Group()
game = Game(player, monster_group)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.draw(display_surface)
    game.draw(display_surface)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

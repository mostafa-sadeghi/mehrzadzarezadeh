import pygame
from constants import *
from pygame.locals import *
from player import Player
from game import Game
pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
player = Player(player_bullet_group)
enemy_group = pygame.sprite.Group()
my_game = Game(player, enemy_group, player_bullet_group, enemy_bullet_group)
my_game.start_new_round()
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()

    display_surface.fill((0, 0, 0))

    player.update()
    player.draw(display_surface)
    player_bullet_group.draw(display_surface)
    player_bullet_group.update()
    enemy_group.update()
    enemy_group.draw(display_surface)

    pygame.display.update()
    clock.tick(FPS)

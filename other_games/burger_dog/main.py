import pygame
import random


WIN_WIDTH = 1000
WIN_HEIGHT = 600

display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Burger Dog")

player_right = pygame.image.load("dog_right.png")
player_left = pygame.image.load("dog_left.png")

player_image = player_right
player_rect = player_image.get_rect()
player_rect.bottom = WIN_HEIGHT
player_rect.centerx = WIN_WIDTH/2

PLAYER_NORMAL_VELOCITY = 5
FPS = 60
clock = pygame.time.Clock()
player_velocity = PLAYER_NORMAL_VELOCITY

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_rect.y -= player_velocity
    if keys[pygame.K_DOWN]:
        player_rect.y += player_velocity
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_velocity
        player_image = player_right
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_velocity
        player_image = player_left

    display_surface.fill((0,0,0))
    display_surface.blit(player_image, player_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

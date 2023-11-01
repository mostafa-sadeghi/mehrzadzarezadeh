import pygame
from constants import *


class World:
    def __init__(self, data):
        self.tile_list = []
        dirt_img = pygame.image.load("assets/dirt.png")
        grass_img = pygame.image.load("assets/grass.png")

        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 1:
                    img = pygame.transform.scale(
                        dirt_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = j * TILE_SIZE
                    img_rect.y = i * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if data[i][j] == 2:
                    img = pygame.transform.scale(
                        grass_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = j * TILE_SIZE
                    img_rect.y = i * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

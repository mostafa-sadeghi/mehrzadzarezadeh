import pygame
from constants import *

class World:
    def __init__(self, tile_map):
        self.tile_list = []
        self.image = pygame.image.load("assets/background.png")
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect(topleft = (0,0))

        for row in range(ROWS):
            for col in range(COLS):
                if tile_map[row][col] == 1:
                    img = DIRT_IMAGE
                    img_rect = img.get_rect()
                    img_rect.topleft = (col * TILE_SIZE, row*TILE_SIZE)
                    self.tile_list.append((img, img_rect))

    def draw(self,screen):
        screen.blit(self.image, self.rect)
        for row in range(ROWS):
            pygame.draw.line(screen, (240, 10,230), (0, row * 32), ((SCREEN_WIDTH, row * 32)))
        for col in range(COLS):
            pygame.draw.line(screen, (240, 10,230), (col * TILE_SIZE, 0), ((col * TILE_SIZE, SCREEN_HEIGHT)))

        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
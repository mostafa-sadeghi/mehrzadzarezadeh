import pygame
from constants import *


class Player:
    def __init__(self, x, y):
        img = pygame.image.load("assets/boy/Run (1).png")
        self.image = pygame.transform.scale(img, (60, 80))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

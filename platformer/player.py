import pygame
from constants import *
class Player:
    def __init__(self, x, y):

        self.frame_index = 0
        self.counter = 0

        self.images_right = []
        for i in range(1, 9):
            img = pygame.image.load(f"assets/boy/Run ({i}).png")
            img = pygame.transform.scale(img, (110, 80))
            self.images_right.append(img)

        self.image = self.images_right[0]
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0

    def update(self): 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.counter += 1

        if self.counter > 3:
            self.frame_index += 1
            self.counter = 0
            if self.frame_index > len(self.images_right) - 1:
                self.frame_index = 0
        self.image = self.images_right[self.frame_index]

    def draw(self, screen):
        screen.blit(self.image, self.rect)

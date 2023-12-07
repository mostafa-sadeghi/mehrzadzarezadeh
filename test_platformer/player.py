import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self,x,y):
        super().__init__()
        image = pygame.image.load("assets/boy/Idle (1).png")
        self.image = pygame.transform.scale(image, (image.get_width()* 0.2, image.get_height()* 0.2))
        # print(self.image.get_width(), self.image.get_height())
        self.rect = self.image.get_rect(topleft = (x,y))


    def update(self,screen):
        pygame.draw.rect(screen, (10,230,210), self.rect,4)

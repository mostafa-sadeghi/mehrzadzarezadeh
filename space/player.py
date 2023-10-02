import pygame
from pygame.sprite import Sprite
from constants import *


class Player(Sprite):
    def __init__(self, bullet_group):
        super().__init__()
        self.image = pygame.image.load("space/assets/player_ship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH/2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.velocity = 8

        self.bullet_group = bullet_group
        self.shoot_sound = pygame.mixer.Sound("space/assets/player_fire.wav")

    def update(self):
        """
        moves the player from left to right at the bottom of the screen
        player should not exit from the screen
        """

    def reset(self):
        """
        reset the players position
        """

import pygame
from pygame.sprite import Sprite
from constants import *
from player_bullet import PlayerBullet


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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.x < WINDOW_WIDTH:
            self.rect.x += self.velocity

    def reset(self):
        """
        reset the players position
        """

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def fire(self):
        PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)
        self.shoot_sound.play()

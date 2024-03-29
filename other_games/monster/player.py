import pygame
from pygame.sprite import Sprite
from config import *


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = WIN_HEIGHT
        self.rect.centerx = WIN_WIDTH/2

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.catch_sound = pygame.mixer.Sound("assets/catch.wav")
        self.die_sound = pygame.mixer.Sound("assets/die.wav")
        self.warp_sound = pygame.mixer.Sound("assets/warp.wav")

    def draw(self, display_surface):

        display_surface.blit(self.image, self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT - 100:
            self.rect.y += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.x += self.velocity

    def warp(self):
        if self.warps > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom = WIN_HEIGHT
            self.rect.centerx = WIN_WIDTH / 2

    def reset(self):
        self.rect.bottom = WIN_HEIGHT
        self.rect.centerx = WIN_WIDTH/2

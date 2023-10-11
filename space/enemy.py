from pygame.sprite import Sprite
import pygame

from enemy_bullet import EnemyBullet


class Enemy(Sprite):
    def __init__(self, x, y, velocity, bullet_group):
        super().__init__()
        self.image = pygame.image.load("space/assets/alien.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.direction = 1
        self.velocity = velocity

        self.bullet_group = bullet_group

        self.shoot_sound = pygame.mixer.Sound("space/assets/alien_fire.wav")

    def update(self):
        self.rect.x += self.direction * self.velocity

    def fire(self):
        EnemyBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)

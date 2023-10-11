import pygame
from enemy import Enemy
from constants import *


class Game:
    def __init__(self, player, enemy_group, player_bullet_group, enemy_bullet_group):
        self.score = 0
        self.round_number = 1
        self.player = player
        self.enemy_group = enemy_group
        self.player_bullet_group = player_bullet_group
        self.enemy_bullet_group = enemy_bullet_group

        self.font = pygame.font.Font("space/assets/Facon.ttf")

    def draw(self, screen):
        pass
    "نوشتن امتیاز و سایر پارامترهای بازی"

    def update(self):
        move_down = False
        for enemy in self.enemy_group.sprites():
            if enemy.rect.left <= 0 or enemy.rect.right >= WINDOW_WIDTH:
                move_down = True

        if move_down:
            for enemy in self.enemy_group.sprites():
                enemy.rect.y += 5 * self.round_number

    def start_new_round(self):
        for i in range(11):
            for j in range(5):
                enemy = Enemy(64 + i * 64, 64 + j * 64,
                              self.round_number, self.enemy_bullet_group)
                self.enemy_group.add(enemy)

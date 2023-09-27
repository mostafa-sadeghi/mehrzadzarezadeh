from random import randint, choice
import pygame
from config import WIN_HEIGHT, WIN_WIDTH

from monster import Monster


class Game:
    def __init__(self, player, monster_group):
        self.score = 0
        self.round_number = 0
        self.player = player
        self.monster_group = monster_group

        self.font = pygame.font.Font("assets/Abrushow.ttf")

        blue_monster = pygame.image.load("assets/blue_monster.png")
        green_monster = pygame.image.load("assets/green_monster.png")
        purple_monster = pygame.image.load("assets/purple_monster.png")
        yellow_monster = pygame.image.load("assets/yellow_monster.png")

        self.target_monsters_images = [
            blue_monster, green_monster, purple_monster, yellow_monster]

        self.target_monster_type = randint(0, 3)

        self.target_monster_image = self.target_monsters_images[self.target_monster_type]

        self.target_monster_rect = self.target_monster_image.get_rect()

        self.target_monster_rect.centerx = WIN_WIDTH/2
        self.target_monster_rect.top = 30

    def draw(self, display_surface):
        COLORS = (
            (28, 190, 241),
            (98, 214, 48),
            (231, 47, 251),
            (245, 165, 22)
        )
        score_text = self.font.render(
            f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topleft=(10, 10))

        warps_text = self.font.render(
            f'Warps: {self.player.warps}', True, (255, 255, 255))
        warps_rect = warps_text.get_rect(topleft=(10, 30))

        display_surface.blit(score_text, score_rect)
        display_surface.blit(warps_text, warps_rect)
        display_surface.blit(self.target_monster_image,
                             self.target_monster_rect)

        pygame.draw.rect(
            display_surface, COLORS[self.target_monster_type], (0, 100, WIN_WIDTH, WIN_HEIGHT - 200), 4)

    def start_new_round(self):
        self.round_number += 1
        for i in range(self.round_number):
            self.monster_group.add(
                Monster(
                    randint(0, WIN_WIDTH-64),
                    randint(100, WIN_HEIGHT-164),
                    self.target_monsters_images[0],
                    0
                )
            )
            self.monster_group.add(
                Monster(randint(0, WIN_WIDTH-64), randint(100, WIN_HEIGHT-164), self.target_monsters_images[1], 1))
            self.monster_group.add(
                Monster(randint(0, WIN_WIDTH-64), randint(100, WIN_HEIGHT-164), self.target_monsters_images[2], 2))
            self.monster_group.add(
                Monster(randint(0, WIN_WIDTH-64), randint(100, WIN_HEIGHT-164), self.target_monsters_images[3], 3))

    def update(self):
        self.check_collisions()

    def check_collisions(self):

        collided_monster = pygame.sprite.spritecollideany(
            self.player, self.monster_group)

        if collided_monster:
            if collided_monster.type == self.target_monster_type:
                self.score += 100
                collided_monster.remove(self.monster_group)
                self.player.catch_sound.play()
                if self.monster_group:
                    self.choose_new_target()
                else:
                    self.start_new_round()

            else:
                pass

    def choose_new_target(self):
        new_target_monster = choice(self.monster_group.sprites())
        self.target_monster_image = new_target_monster.image
        self.target_monster_type = new_target_monster.type

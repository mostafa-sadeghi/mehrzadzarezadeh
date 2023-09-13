from random import randint
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

    def draw(self, display_surface):
        score_text = self.font.render(
            f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topleft=(10, 10))

        display_surface.blit(score_text, score_rect)

    def start_new_round(self):
        self.round_number += 1
        for i in range(self.round_number):
            self.monster_group.add(
                        Monster(
                            randint(0, WIN_WIDTH-64),
                            randint(100, WIN_HEIGHT-164),
                            self.target_monsters_images[0],
                            "blue"
                           )
                           )
            self.monster_group.add(
                Monster(randint(0, WIN_WIDTH-64), randint(100, WIN_HEIGHT-164), self.target_monsters_images[1], "green"))
            self.monster_group.add(
                Monster(randint(0, WIN_WIDTH-64), randint(100, WIN_HEIGHT-164), self.target_monsters_images[2], "purple"))
            self.monster_group.add(
                Monster(randint(0, WIN_WIDTH-64), randint(100, WIN_HEIGHT-164), self.target_monsters_images[3], "yellow"))

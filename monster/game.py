import pygame


class Game:
    def __init__(self, player, monster_group):
        self.score = 0
        self.round_number = 0
        self.player = player
        self.monster_group = monster_group

        self.font = pygame.font.Font("assets/Abrushow.ttf")

    def draw(self, display_surface):
        score_text = self.font.render(
            f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topleft=(10, 10))

        display_surface.blit(score_text, score_rect)

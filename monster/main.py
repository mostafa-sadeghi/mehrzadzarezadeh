import pygame
from pygame.sprite import Sprite
from random import randint, choice

pygame.init()
WIN_WIDTH = 1200
WIN_HEIGHT = 700

display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


FPS = 60
clock = pygame.time.Clock()


class Monster(Sprite):
    def __init__(self, x, y, image, monster_type):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.type = monster_type

        self.velocity = randint(1, 5)
        self.dx = choice([-1, 1])
        self.dy = choice([-1, 1])

    def update(self):
        self.rect.x += self.dx * self.velocity
        self.rect.y += self.dy * self.velocity

        if self.rect.left <= 0 or self.rect.right >= WIN_WIDTH:
            self.dx *= -1

        if self.rect.top <= 100 or self.rect.bottom >= WIN_WIDTH - 100:
            self.dy *= -1



monster_group = pygame.sprite.Group()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()

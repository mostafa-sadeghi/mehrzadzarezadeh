import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


knight = pygame.image.load("knight.png")
knight_rect = knight.get_rect()
knight_rect.center = (50, 300)
blue_monster = pygame.image.load("blue_monster.png")
blue_monster_rect = blue_monster.get_rect()
blue_monster_rect.center = (350, 300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        knight_rect.x += 5
    if keys[pygame.K_LEFT]:
        blue_monster_rect.x -= 5

    if knight_rect.colliderect(blue_monster_rect):
        blue_monster_rect.x = WINDOW_WIDTH + 100

    display_surface.fill((0, 0, 0))
    pygame.draw.rect(display_surface, (255, 255, 255), knight_rect, 5)
    display_surface.blit(knight, knight_rect)
    display_surface.blit(blue_monster, blue_monster_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()

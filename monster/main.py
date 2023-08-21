import pygame

pygame.init()
WIN_WIDTH = 1200
WIN_HEIGHT = 700

display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


FPS = 60
clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()

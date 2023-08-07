import pygame
import random
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch The Clown")


bgpicture = pygame.image.load("images/background.png")
bgpicture_rect = bgpicture.get_rect()
bgpicture_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

bgmusic = pygame.mixer.Sound("sounds/Bad Piggies Theme.mp3")
bgmusic.set_volume(0.4)
bgmusic.play(-1)



clown_image = pygame.image.load("images/clown.png")
clown_image_rect = clown_image.get_rect()
clown_image_rect.center = (WINDOW_WIDTH/2 , WINDOW_HEIGHT/2)

dx = random.choice([-1, 1])
dy = random.choice([-1, 1])
clown_velocity = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clown_image_rect.x += dx * clown_velocity
    clown_image_rect.y += dy * clown_velocity

    if clown_image_rect.left < 0 or clown_image_rect.right > WINDOW_WIDTH:
        dx *= -1
    if clown_image_rect.top < 0 or clown_image_rect.bottom > WINDOW_HEIGHT:
        dy *= -1

    display_surface.blit(bgpicture, bgpicture_rect)
    display_surface.blit(clown_image, clown_image_rect)
    pygame.display.update()

pygame.quit()
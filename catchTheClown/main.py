import pygame
import random
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch The Clown")

clock = pygame.time.Clock()

bgpicture = pygame.image.load("images/background.png")
bgpicture_rect = bgpicture.get_rect()
bgpicture_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

bgmusic = pygame.mixer.Sound("sounds/Bad Piggies Theme.mp3")
bgmusic.set_volume(0.4)
bgmusic.play(-1)

# TODO
"""
loading click sound and miss sound
"""

clown_image = pygame.image.load("images/clown.png")
clown_image_rect = clown_image.get_rect()
clown_image_rect.center = (WINDOW_WIDTH/2 , WINDOW_HEIGHT/2)

dx = random.choice([-1, 1])
dy = random.choice([-1, 1])

score = 0
# TODO  define player_lives 

font = pygame.font.SysFont('arial',22)

score_text = font.render(f"Score: {score}", True, (255,0,0))
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

# TODO define and render lives_text

clown_velocity = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if clown_image_rect.collidepoint(event.pos):
                score += 1
                # TODO play click sound

            else:
                pass
                # TODO decrease the player's lives
                # play miss sound


                

    clown_image_rect.x += dx * clown_velocity
    clown_image_rect.y += dy * clown_velocity

    if clown_image_rect.left < 0 or clown_image_rect.right > WINDOW_WIDTH:
        dx *= -1
    if clown_image_rect.top < 0 or clown_image_rect.bottom > WINDOW_HEIGHT:
        dy *= -1
    score_text = font.render(f"Score: {score}", True, (255,0,0))
    # TODO  rerender lives text

    display_surface.blit(bgpicture, bgpicture_rect)
    display_surface.blit(score_text, score_rect)
    # TODO blit the player_lives
    display_surface.blit(clown_image, clown_image_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
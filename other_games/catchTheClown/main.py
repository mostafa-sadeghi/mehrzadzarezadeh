import pygame
import random
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch The Clown")

clock = pygame.time.Clock()

bgpicture = pygame.image.load("catchTheClown/images/background.png")
bgpicture_rect = bgpicture.get_rect()
bgpicture_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

bgmusic = pygame.mixer.Sound("catchTheClown/sounds/Bad Piggies Theme.mp3")
bgmusic.set_volume(0.4)
bgmusic.play(-1)

click_sound = pygame.mixer.Sound("catchTheClown/sounds/click_sound.wav")
miss_sound = pygame.mixer.Sound("catchTheClown/sounds/miss_sound.wav")

clown_image = pygame.image.load("catchTheClown/images/clown.png")
clown_image_rect = clown_image.get_rect()
clown_image_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

dx = random.choice([-1, 1])
dy = random.choice([-1, 1])

score = 0
player_lives = 3

font = pygame.font.SysFont('arial', 22)

score_text = font.render(f"Score: {score}", True, (255, 0, 0))
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

lives_text = font.render(f"lives: {player_lives}", True, (255, 0, 0))
lives_rect = lives_text.get_rect()
lives_rect.topleft = (WINDOW_WIDTH - 100, 10)


clown_velocity = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if clown_image_rect.collidepoint(event.pos):
                score += 1
                click_sound.play()

            else:
                player_lives -= 1

    if player_lives == 0:
        bgmusic.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    bgmusic.play()
                    is_paused = False
                    score = 0
                    player_lives = 5

                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    clown_image_rect.x += dx * clown_velocity
    clown_image_rect.y += dy * clown_velocity

    if clown_image_rect.left < 0 or clown_image_rect.right > WINDOW_WIDTH:
        dx *= -1
    if clown_image_rect.top < 0 or clown_image_rect.bottom > WINDOW_HEIGHT:
        dy *= -1
    score_text = font.render(f"Score: {score}", True, (255, 0, 0))
    lives_text = font.render(f"lives: {player_lives}", True, (255, 0, 0))

    display_surface.blit(bgpicture, bgpicture_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(clown_image, clown_image_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()

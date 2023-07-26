from random import randint
import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("game2")

GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

PLAYER_STARTING_LIVES = 5
PLAYER_STARTING_VELOCITY = 5
COIN_STARTING_VELOCITY = 8
FPS = 60

player_velocity = PLAYER_STARTING_VELOCITY
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

score = 0

clock = pygame.time.Clock()

my_font = pygame.font.Font("AttackGraffiti.ttf", 32)

score_text = my_font.render(f"Score: {score}", \
                            False, GREEN, \
                            DARKGREEN)
score_rect = score_text.get_rect()
score_rect.midleft = (90, 38)

title_text = my_font.render("Dragon Game", True, DARKGREEN, GREEN)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH / 2
title_rect.centery = 38

lives_text = my_font.render(f"Lives: {player_lives}", True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.center = (WINDOW_WIDTH - 150, 38)


game_over_text = my_font.render("Game Over", False, GREEN)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WINDOW_WIDTH/2,\
                              WINDOW_HEIGHT/2)


continue_text = my_font.render("Press any key to continue...",\
                               False, DARKGREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH/2,\
                             WINDOW_HEIGHT/2 + 50)


dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

player = pygame.transform.scale(
    pygame.image.load("dragon_right.png"), (50, 50))
player_rect = player.get_rect()
player_rect.centerx = 50
player_rect.bottom = WINDOW_HEIGHT

coin_image = pygame.transform.scale(pygame.image.load("coin.png"), (32, 32))
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + 200
coin_rect.y = randint(64, WINDOW_HEIGHT - 32)

bgsound = pygame.mixer.Sound("bgmusic.mp3")
loss = pygame.mixer.Sound("loss.wav")
success = pygame.mixer.Sound("success.wav")
bgsound.play(-1)
loss.set_volume(.2)
success.set_volume(.2)

running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_rect.top > 74:
        player_rect.y -= PLAYER_STARTING_VELOCITY

    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_STARTING_VELOCITY

    if coin_rect.x < 0:
        player_lives -= 1
        loss.play()
        coin_rect.x = WINDOW_WIDTH + 200
        coin_rect.y = randint(64, WINDOW_HEIGHT - 32)

    coin_rect.x -= coin_velocity

    if player_rect.colliderect(coin_rect):
        score += 1
        success.play()
        coin_velocity += 0.5
        coin_rect.x = WINDOW_WIDTH + 200
        coin_rect.y = randint(64, WINDOW_HEIGHT - 32)

    lives_text = my_font.render(f"Lives: {player_lives}", True, GREEN, DARKGREEN)
    score_text = my_font.render(f"Score: {score}", True, GREEN, DARKGREEN)

    if player_lives == 0:
        display_surface.blit(game_over_text,\
                             game_over_text_rect)
        display_surface.blit(continue_text,\
                             continue_text_rect)
        pygame.display.update()
        bgsound.stop()



        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    is_paused = False
                    player_lives = PLAYER_STARTING_LIVES
                    score = 0
                    coin_velocity = COIN_STARTING_VELOCITY
                    bgsound.play(-1)

                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False





    display_surface.fill(BLACK)
    display_surface.blit(dragon_left_image,
                         dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    pygame.draw.line(display_surface, (255, 255, 255),
                     (0, 75), (WINDOW_WIDTH, 75), 4)

    display_surface.blit(player, player_rect)
    display_surface.blit(coin_image, coin_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("game2")

GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

system_font = pygame.font.SysFont('calibri', 64)
my_font = pygame.font.Font("AttackGraffiti.ttf", 32)

system_text = system_font.render("Dragon Game!", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)


my_text = my_font.render("Dragon", True, GREEN)
my_text_rect = my_text.get_rect()
my_text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 100)


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


bgsound = pygame.mixer.Sound("bgmusic.mp3")
loss = pygame.mixer.Sound("loss.wav")
success = pygame.mixer.Sound("success.wav")
bgsound.play(-1)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(dragon_left_image,
                         dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    pygame.draw.line(display_surface, (255, 255, 255),
                     (0, 75), (WINDOW_WIDTH, 75), 4)

    display_surface.blit(player, player_rect)

    # display_surface.blit(system_text, system_text_rect)
    # display_surface.blit(my_text, my_text_rect)
    pygame.display.update()

pygame.quit()

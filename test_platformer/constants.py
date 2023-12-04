import pygame

screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
FPS = 60
TILE_SIZE = 32
ROWS = SCREEN_HEIGHT // TILE_SIZE
COLS = SCREEN_WIDTH // TILE_SIZE

DIRT_IMAGE = pygame.image.load("assets/dirt.png")
GRASS_IMAGE = pygame.image.load("assets/grass.png")
WATER_IMAGE = pygame.image.load("assets/water.png")
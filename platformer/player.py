import pygame
from constants import *
class Player:
    def __init__(self, x, y):
        self.frame_index = 0
        self.counter = 0
        self.images_right = []
        self.images_left = []
        self.idle_images_left = []
        self.idle_images_right = []
        for i in range(1, 9):
            img = pygame.image.load(f"assets/boy/Run ({i}).png")
            img = pygame.transform.scale(img, (110, 80))
            self.images_right.append(img)
            img = pygame.transform.flip(img, True, False)
            self.images_left.append(img)

        for i in range(1, 10):
            img = pygame.image.load(f"assets/boy/Idle ({i}).png")
            img = pygame.transform.scale(img, (110, 80))
            self.idle_images_right.append(img)
            img = pygame.transform.flip(img, True, False)
            self.idle_images_left.append(img)
        self.image = self.images_left[0]
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.direction = -1

    def update(self, tile_list, screen): 
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = -1
            dx -= 5
            self.counter += 1
            self.image = self.images_left[self.frame_index]

        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.counter += 1
            dx += 5
            self.image = self.images_right[self.frame_index]

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            
            self.counter += 1
            if self.direction == 1:
                self.image = self.idle_images_right[self.frame_index]
            elif self.direction == -1:
                self.image = self.idle_images_left[self.frame_index]

        if self.counter > 2:
            self.frame_index += 1
            self.counter = 0
            if self.frame_index > len(self.images_right) - 1:
                self.frame_index = 0
        self.vel_y += 1
        dy += self.vel_y
        if self.direction == 1:
            rect = pygame.Rect(self.rect.x +40, self.rect.y + 5, self.image.get_width()-60, self.image.get_height()-15)
        elif self.direction == -1:
            rect = pygame.Rect(self.rect.x +20, self.rect.y + 5, self.image.get_width()-60, self.image.get_height()-15)
        # rect = pygame.Rect(self.rect.x , self.rect.y , self.image.get_width(), self.image.get_height())

        for tile in tile_list:
            if tile[1].colliderect(rect.x + dx, rect.y, self.image.get_width()-60, self.image.get_height()-15):
                dx = 0
            if tile[1].colliderect(rect.x, rect.y + dy, self.image.get_width()-60, self.image.get_height()-15):
                self.vel_y = 0
                dy = tile[1].top - rect.bottom
                


        self.rect.x += dx
        self.rect.y += dy
        pygame.draw.rect(screen, (255,0,0),rect,2)
        


    def draw(self, screen):
        screen.blit(self.image, self.rect)

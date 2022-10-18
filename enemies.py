import pygame
from pygame.locals import *


class Enemies(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/goblin.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = self.x, self.y
    def movimento(self):
        if self.y == 0:
            self.y += 2
        elif self.x == 0:
           self.x += 2
        elif self.y == 720:
            self.y -= 2
        elif self.x == 1080:
            self.x -= 2
        elif self.x == 520 and self.y < 350:
            self.y += 2
        elif self.x == 520 and self.y > 350:
            self.y -= 2
        elif self.y == 350 and self.x > 520:
            self.x -= 2
        elif self.y == 350 and self.x < 520:
            self.x += 2
        elif 500 < self.x < 580 and self.y < 350:
            self.y += 2
        elif 500 < self.x < 580 and self.y > 350:
            self.y -= 2
        elif 374 <= self.y <= 445 and self.x < 520:
            self.x += 2
        elif 374 <= self.y <= 445 and self.x > 520:
            self.x -= 2
        self.rect.topleft = self.x, self.y

import pygame
from pygame.locals import *

class Obstaculos(pygame.sprite.Sprite):
    def __init__(self, imagem, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = x, y
    def coord_x(self):
        return self.x
    def coord_y(self):
        return self.y

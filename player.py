import pygame
from pygame.locals import *
from pickle import TRUE

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/perso_baixo.png'))
        self.sprites.append(pygame.image.load('sprites/perso_cima1.png'))
        self.sprites.append(pygame.image.load('sprites/perso_direita.png'))
        self.sprites.append(pygame.image.load('sprites/perso_esquerda.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.image = pygame.transform.scale(self.image, (24, 34))
    def baixo(self):
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (24, 34))
    def cima(self):
        self.image = self.sprites[1]
        self.image = pygame.transform.scale(self.image, (24, 34))
    def direita(self):
        self.image = self.sprites[2]
        self.image = pygame.transform.scale(self.image, (24, 34))
    def esquerda(self):
        self.image = self.sprites[3]
        self.image = pygame.transform.scale(self.image, (24, 34))


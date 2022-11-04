import pygame
from pygame.locals import *


class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, z):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/balacinza10.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.movimento = z
        self.rect.topleft = x, y
    def movimentobala(self):
        if self.movimento == 'cima':
            self.y -= 12
            self.rect.topleft = self.x, self.y
        if self.movimento == 'baixo':
            self.y += 12
            self.rect.topleft = self.x, self.y
        if self.movimento == 'esquerda':
            self.x -= 12
            self.rect.topleft = self.x, self.y
        if self.movimento == 'direita':
            self.x += 12
            self.rect.topleft = self.x, self.y
        if self.movimento == 'nordeste':
            self.x += 12
            self.y -= 12
            self.rect.topleft = self.x, self.y
        if self.movimento == 'noroeste':
            self.x -= 12
            self.y -= 12
            self.rect.topleft = self.x, self.y
        if self.movimento == 'sudeste':
            self.x += 12
            self.y += 12
            self.rect.topleft = self.x, self.y
        if self.movimento == 'sudoeste':
            self.x -= 12
            self.y += 12
            self.rect.topleft = self.x, self.y
    def coordenadas(self):
        lista_coordenadas = (self.x, self.y)
        return lista_coordenadas

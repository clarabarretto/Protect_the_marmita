import pygame
from pygame.locals import *
from pickle import TRUE

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/perso.png'))
        self.sprites.append(pygame.image.load('sprites/persocima.png'))
        self.sprites.append(pygame.image.load('sprites/persocima1.png'))
        self.sprites.append(pygame.image.load('sprites/persocima2.png'))
        self.sprites.append(pygame.image.load('sprites/persodireita.png'))
        self.sprites.append(pygame.image.load('sprites/persodireita1.png'))
        self.sprites.append(pygame.image.load('sprites/persodireita2.png'))
        self.sprites.append(pygame.image.load('sprites/persoesquerda.png'))
        self.sprites.append(pygame.image.load('sprites/persoesquerda1.png'))
        self.sprites.append(pygame.image.load('sprites/persoesquerda2.png'))
        self.sprites.append(pygame.image.load('sprites/persosul.png'))
        self.sprites.append(pygame.image.load('sprites/persosul1.png'))
        self.sprites.append(pygame.image.load('sprites/persosul2.png'))
        self.atual = 0
        self.atualcima = 1
        self.atualdireita = 4
        self.atualesquerda = 7
        self.atualsul = 10
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
    def baixo(self, x, y):
        self.image = self.sprites[int(self.atualsul)]
        self.atualsul += 0.2
        if self.atualsul > 12.5:
            self.atualsul = 10
        self.rect.topleft = x, y
    def cima(self, x, y):
        self.image = self.sprites[int(self.atualcima)]
        self.atualcima += 0.2
        if self.atualcima > 4:
            self.atualcima = 1
        self.rect.topleft = x, y
    def direita(self, x, y):
        self.image = self.sprites[int(self.atualdireita)]
        self.atualdireita += 0.2
        if self.atualdireita > 7:
            self.atualdireita = 4
        self.rect.topleft = x, y
    def esquerda(self, x, y):
        self.image = self.sprites[int(self.atualesquerda)]
        self.atualesquerda += 0.2
        if self.atualesquerda > 10:
           self.atualesquerda = 7
        self.rect.topleft = x, y
    def parado(self, x, y):
        self.image = self.sprites[0]
        self.rect.topleft = x, y
    def tiro_baixo(self, x, y):
        self.image = self.sprites[10]
        self.rect.topleft = x, y
    def tiro_cima(self, x, y):
        self.image = self.sprites[1]
        self.rect.topleft = x, y
    def tiro_esquerda(self, x, y):
        self.image = self.sprites[7]
        self.rect.topleft = x, y
    def tiro_direita(self, x, y):
        self.image = self.sprites[4]
        self.rect.topleft = x, y
    def movimento_tiro(self, x, y, position):
        if position == 'cima':
            self.image = self.sprites[int(self.atualcima)]
            self.atualcima += 0.2
            if self.atualcima > 4:
                self.atualcima = 1
            self.rect.topleft = x, y
        elif position == 'baixo':
            self.image = self.sprites[int(self.atualsul)]
            self.atualsul += 0.2
            if self.atualsul > 12.5:
                self.atualsul = 10
            self.rect.topleft = x, y
        elif position == 'direita':
            self.image = self.sprites[int(self.atualdireita)]
            self.atualdireita += 0.2
            if self.atualdireita > 7:
                self.atualdireita = 4
            self.rect.topleft = x, y
        elif position == 'esquerda':
            self.image = self.sprites[int(self.atualesquerda)]
            self.atualesquerda += 0.2
            if self.atualesquerda > 10:
                self.atualesquerda = 7
            self.rect.topleft = x, y

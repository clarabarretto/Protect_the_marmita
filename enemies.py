import pygame
from pygame.locals import *
from random import randint


class Enemies(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/inimigo1_1.png'))
        self.sprites.append(pygame.image.load('sprites/inimigo1_2.png'))
        self.inicio = 80
        self.numero = randint(1,5)
        if self.numero <= 2:
            self.escolha = 'player'
        else:
            self.escolha = 'geladeira'
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = self.x, self.y
    def movimento(self, x, y, x2, y2):
        self.image = self.sprites[int(self.atual)]
        self.atual += 0.2
        if self.atual > 2:
            self.atual = 0
        if self.y == 0:
            self.y += 2
        elif self.x == 0:
           self.x += 2
        elif self.y == 720:
            self.y -= 2
        elif self.x == 1080:
            self.x -= 2
        elif self.inicio > 0:
            if self.x > 0 and self.x <= 160:
                self.x += 2
            elif self.x <= 1080 and self.x >= 920:
                self.x -= 2
            elif self.y > 0 and self.y <= 160:
                self.y += 2
            elif self.y <= 720 and self.y >= 560:
                self.y -= 2
        elif self.escolha == 'geladeira':
            if self.x == x2 and self.y < y2:
                self.y += 2
            elif self.x == x2 and self.y > y2:
                self.y -= 2
            elif self.y == y2 and self.x > x2:
                self.x -= 2
            elif self.y == y2 and self.x < x2:
                self.x += 2
            elif x2 - 80 <= self.x <= x2 + 80 and self.y < y2:
                self.y += 2
            elif x2 - 80 <= self.x <= x2 + 80 and self.y > y2:
                self.y -= 2
            elif y2 - 80 <= self.y <= y2 + 80 and self.x < x2:
                self.x += 2
            elif y2 - 80 <= self.y <= y2 + 80 and self.x > x2:
                self.x -= 2
            else:
                if self.x < x2 and self.y > y2:
                    self.x += 2
                    self.y -= 2
                elif self.x > x2 and self.y > y2:
                    self.x -= 2
                    self.y -= 2
                elif self.x < x2 and self.y < y2:
                    self.x += 2
                    self.y += 2
                elif self.x > x2 and self.y < y2:
                    self.x -= 2
                    self.y += 2
        elif self.escolha == 'player':
            if self.x == x and self.y < y or self.x == x + 1 and self.y < y:
                self.y += 2
            elif self.x == x and self.y > y or self.x == x + 1 and self.y > y:
                self.y -= 2
            elif self.y == y and self.x > x or self.y == y + 1 and self.x > x:
                self.x -= 2
            elif self.y == y and self.x < x or self.y == y + 1 and self.x < x:
                self.x += 2
            elif x - 80 <= self.x <= x + 80 and self.y < y:
                self.y += 2
            elif x - 80 <= self.x <= x + 80 and self.y > y:
                self.y -= 2
            elif y - 80 <= self.y <= y + 80 and self.x < x:
                self.x += 2
            elif y - 80 <= self.y <= y + 80 and self.x > x:
                self.x -= 2
            else:
                if self.x < x and self.y > y:
                    self.x += 2
                    self.y -= 2
                elif self.x > x and self.y > y:
                    self.x -= 2
                    self.y -= 2
                elif self.x < x and self.y < y:
                    self.x += 2
                    self.y += 2
                elif self.x > x and self.y < y:
                    self.x -= 2
                    self.y += 2
        self.rect.topleft = self.x, self.y
        self.inicio -= 1
    
    def coord_x(self):
        return self.x
    
    def coord_y(self):
        return self.y

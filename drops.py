import pygame
from pygame.locals import *
from random import randint

def dropar_vida(x, y):
    chance = randint(1, 25)

    lista_coordenadas_vida = [x, y]

    if chance == 1:
        drop = True
    else:
        drop = False

    lista_coordenadas_vida.append(drop)
    return lista_coordenadas_vida
    
def dropar_bota(x, y):
    chance = randint(1, 25)

    lista_coordenadas_bota = [x, y]

    if chance == 2:
        drop2 = True
        
    else:
        drop2 = False

    lista_coordenadas_bota.append(drop2)
    return lista_coordenadas_bota

def dropar_gun(x, y):
    chance = randint(1, 50)

    lista_coordenadas_gun = [x, y]

    if chance == 3:
        drop3 = True

    else:
        drop3 = False

    lista_coordenadas_gun.append(drop3)
    return lista_coordenadas_gun

def dropar_tiro_rapido(x, y):
    chance = randint(1, 25)

    lista_coordenadas_tiro_rapido = [x, y]

    if chance == 4:
        drop = True
    else:
        drop = False

    lista_coordenadas_tiro_rapido.append(drop)
    return lista_coordenadas_tiro_rapido

def dropar_ceifador(x, y):
    chance = randint(1, 50)

    lista_coordenadas_ceifador = [x, y]

    if chance == 4:
        drop = True
    else:
        drop = False

    lista_coordenadas_ceifador.append(drop)
    return lista_coordenadas_ceifador

class Moedas(pygame.sprite.Sprite):
    def __init__(self,  x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/moeda1.1.png'))
        self.sprites.append(pygame.image.load('sprites/moeda3.png'))
        self.sprites.append(pygame.image.load('sprites/moeda5.png'))
        self.numero = randint(1,10)
        if self.numero <= 3:
            self.escolha = 'moeda3'
            self.atual = 1
        elif self.numero >= 5:
            self.escolha = 'moeda1'
            self.atual = 0
        else:
            self.escolha = 'moeda5'
            self.atual = 2
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = self.x, self.y
    def identify_moeda(self):
        return self.escolha


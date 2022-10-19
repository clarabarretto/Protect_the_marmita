import pygame
from sys import exit 
from pygame.locals import *
from random import randint


def dropar_vida(x, y):
    chance = randint(1, 10)

    lista_coordenadas_vida = [x, y]

    if chance == 1:
        drop = True
    else:
        drop = False

    lista_coordenadas_vida.append(drop)
    return lista_coordenadas_vida
    
def dropar_bota(x, y):
    chance = randint(1, 10)

    lista_coordenadas_bota = [x, y]

    if chance == 2:
        drop2 = True
        
    else:
        drop2 = False

    lista_coordenadas_bota.append(drop2)
    return lista_coordenadas_bota

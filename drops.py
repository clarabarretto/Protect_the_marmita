import pygame
from sys import exit 
from pygame.locals import *
from random import randint

def dropar(x, y):
    chance = randint(1, 10)
    lista_coordenadas = [x, y]
    if chance == 1:
        drop = True
    else:
        drop = False

    lista_coordenadas.append(drop)
    return lista_coordenadas

import pygame
from sys import exit 
from pygame.locals import *
from random import randint

pygame.init()

class Vida:
    def __init__(self, vida):
        self.vida = vida
        self.coordenada = []
        self.coordenada.append(self.x)
        self.corrdenada.append(self.y)
    
    def cura(self):
        #quando jogador encostar no bloco:
        self.vida += 20
        
    def dano(self):
        #quando jogador encostar no zumbi:
        self.vida -= 20
        
def dropar(x, y):
    chance = randint(1, 20)
    lista_coordenadas_vida = [x, y]
    if chance == 1:
        drop = True
    else:
        drop = False

    lista_coordenadas_vida.append(drop)
    return lista_coordenadas_vida
    


        
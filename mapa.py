import pygame
from pygame.locals import *
import obstaculo

class map(pygame.sprite.Sprite):
    def __init__(self, tela):
        pygame.sprite.Sprite.__init__(self)
        self.window = tela
        self.img_mapa = {0:{'sprite': pygame.image.load('sprites/terra.png'), 'tipo' : 'piso'},
                         1:{'sprite': pygame.image.load('sprites/arvore.png'), 'tipo' : 'parede'},
                         2:{'sprite': pygame.image.load('sprites/grama2.png'), 'tipo' : 'piso'},
                         3:{'sprite': pygame.image.load('sprites/terrapedras.png'), 'tipo' : 'piso'},
                         4:{'sprite': pygame.image.load('sprites/madeira.png'), 'tipo' : 'parede'},
                         5:{'sprite': pygame.image.load('sprites/chaocozinha.png'), 'tipo' : 'piso'},
                         6:{'sprite': pygame.image.load('sprites/terragrama.png'), 'tipo' : 'piso'}}                        
        self.maps = {'mapa 1': [[1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1],
                                [1,2,2,2,2,2,2,2,2,2,2,4,0,0,0,4,2,2,2,2,2,2,2,2,2,2,1],
                                [1,2,4,4,4,4,4,4,4,4,4,4,0,0,0,4,4,4,4,4,4,4,4,4,4,2,1],
                                [1,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,2,1],
                                [1,2,4,0,0,6,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,4,2,1],
                                [1,2,4,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,6,0,0,0,0,4,2,1],
                                [1,2,4,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,2,1],
                                [1,4,4,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,4,4,1],
                                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                                [3,0,0,0,0,0,0,0,0,0,0,6,0,0,0,6,0,0,0,0,0,0,0,0,0,0,3],
                                [3,0,0,0,6,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                                [1,4,4,0,0,0,0,0,0,0,0,0,6,6,0,0,0,0,0,0,0,6,0,0,4,4,1],
                                [1,2,4,0,0,0,0,0,6,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,4,2,1],
                                [1,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,4,2,1],
                                [1,2,4,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,2,1],
                                [1,2,4,4,4,4,4,4,4,4,4,4,0,0,0,4,4,4,4,4,4,4,4,4,4,2,1],
                                [1,2,2,2,2,2,2,2,2,2,2,4,0,0,0,4,2,2,2,2,2,2,2,2,2,2,1],
                                [1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1]]}
        self.map = self.maps['mapa 1']
    def draw_mapa(self):
        for i in range(len(self.maps['mapa 1'])):
            for j in range(27):
                self.window.blit(self.img_mapa[self.map[i][j]]['sprite'], (40*j, 40*i)) 
    def check_obstaculos(self):
        sprites_obstaculos = pygame.sprite.Group()
        for i in range(len(self.maps['mapa 1'])):
            for j in range(27):
                if self.img_mapa[self.map[i][j]]['tipo'] == 'parede':
                    sprites_obstaculos.add(obstaculo.Obstaculos(self.img_mapa[self.map[i][j]]['sprite'], 40*j, 40*i))
        return sprites_obstaculos

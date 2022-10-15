from pickle import TRUE
import pygame
from pygame.locals import *
from sys import exit 
from random import randint
from random import choice

pygame.init()
coordenadas_y = [408, 374, 442, 0, 720]
coordenadas_x = [504, 528, 552, 576, 0, 1080]
coordenadas = [[0, 504], [0, 528], [0, 552], [0, 576], [720, 504], [720, 528], [720, 552], [720, 576], [408, 0], [408, 1080], [374, 0], [374, 1080], [442, 0], [442, 1080]]
space = False
larg = 1080
alt = 720
points = 0
fonte = pygame.font.SysFont('arial', 20, True, True)
fonte_inicial = pygame.font.SysFont('arial', 3000, True, False)
tela = pygame.display.set_mode((larg, alt))
texto_inicial = fonte.render('AssaCInato!', False, (0,0,0))
pygame.display.set_caption('AssaCInato')
x = 300
y = 580
x2 = 520
y2 = 350
var_inimigo = 0
relogio = pygame.time.Clock()
mapa = pygame.image.load('sprites/mapamundi.png')

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
    def baixo(self, x, y):
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (24, 34))
        self.rect.topleft = x, y
    def cima(self, x, y):
        self.image = self.sprites[1]
        self.image = pygame.transform.scale(self.image, (24, 34))
        self.rect.topleft = x, y
    def direita(self, x, y):
        self.image = self.sprites[2]
        self.image = pygame.transform.scale(self.image, (24, 34))
        self.rect.topleft = x, y
    def esquerda(self, x, y):
        self.image = self.sprites[3]
        self.image = pygame.transform.scale(self.image, (24, 34))
        self.rect.topleft = x, y
class Enemies(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/goblin.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = self.x, self.y
    def movimento(self):
        if self.y == 0:
            self.y += 2
        elif self.x == 0:
           self.x += 2
        elif self.y == 720:
            self.y -= 2
        elif self.x == 1080:
            self.x -= 2
        elif self.x == 520 and self.y < 350:
            self.y += 2
        elif self.x == 520 and self.y > 350:
            self.y -= 2
        elif self.y == 350 and self.x > 520:
            self.x -= 2
        elif self.y == 350 and self.x < 520:
            self.x += 2
        elif 500 < self.x < 580 and self.y < 350:
            self.y += 2
        elif 500 < self.x < 580 and self.y > 350:
            self.y -= 2
        elif 374 <= self.y <= 445 and self.x < 520:
            self.x += 2
        elif 374 <= self.y <= 445 and self.x > 520:
            self.x -= 2
        self.rect.topleft = self.x, self.y


        

todas_as_sprites = pygame.sprite.Group()

player = Player(x , y)
todas_as_sprites.add(player)
inimigos = pygame.sprite.Group()
while True:
    var_direita = True
    var_esquerda = True
    var_cima = True
    var_baixo = True
    spawn = choice(coordenadas)
    relogio.tick(30)
    tela.fill((0,0,0))
    mensage = f"score : {points}"
    text = fonte.render(mensage, False, (0, 0, 0))
    tela.blit(mapa, (0,0))
    var_inimigo = randint(0, 100)
    rect = pygame.draw.rect(tela,(200, 100, 0), (x2, y2, 20, 20))
    for sprite in todas_as_sprites:
        if sprite.rect.colliderect(rect):
            if x + 25 == x2:
                var_direita = False
            if (x2 + 15) <= x and x <= (x2 + 35):
                var_esquerda = False
            if y2 - 45 <= y and y <= y2 - 27:
                var_baixo = False
            if y2 + 10 <= y and y <= y2 + 37:
                var_cima = False

    if 15 < var_inimigo < 20:
        inimigos.add(Enemies(spawn[1], spawn[0]))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a and x != 0 and var_esquerda == True:
                x -= 5
                player.esquerda(x, y)
            if event.key == K_d and x != 1055 and var_direita == True:
                x += 5
                player.direita(x, y)
            if event.key == K_w and y != 0 and var_cima == True:
                y -= 5
                player.cima(x, y)
            if event.key == K_s and y != 685 and var_baixo == True:
                y += 5
                player.baixo(x, y)
            if event.key == K_SPACE:
                space = True
    if pygame.key.get_pressed()[K_a] and x != 0 and var_esquerda == True:
        x -= 5
        player.esquerda(x, y)
    if pygame.key.get_pressed()[K_d] and x != 1055 and var_direita == True:
        x += 5
        player.direita(x, y)
    if pygame.key.get_pressed()[K_w] and y != 0 and var_cima == True:
        y -= 5
        player.cima(x, y)
    if pygame.key.get_pressed()[K_s] and y != 685 and var_baixo == True:
        y += 5
        player.baixo(x, y)
    rect = pygame.draw.rect(tela,(200, 100, 0), (x2, y2, 20, 20))
    for sprite in todas_as_sprites:
        for enemies in inimigos:
            if sprite.rect.colliderect(enemies):
                inimigos.remove(enemies)
                points += 1
    for enemies in inimigos:
        if enemies.rect.colliderect(rect):
            print('game over!')
            exit()
    if points == 50:
        print('parabens caraio')
        exit()
    inimigos.draw(tela)
    for enemy in inimigos:
        enemy.movimento()
    if y > 720:
        y = 0
    if y < 0:
        y = 720
    if x > 1080:
        x = 0
    if x < 0:
        x = 1080   
    tela.blit(text, (980, 10))
    if space == False:
        tela.blit(texto_inicial, (500, 240))
    inimigos.update()
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.update()

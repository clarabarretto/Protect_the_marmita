import pygame
import enemies as en
import projetil as pr
from pygame.locals import *
from sys import exit 
from random import randint
from random import choice
import personagem as perso
import pupvida

pygame.init()

coordenadas_y = [408, 374, 442, 0, 720]
coordenadas_x = [504, 528, 552, 576, 0, 1080]
coordenadas = [(0, 504), (0, 528), (0, 552), (0, 576), (720, 504), (720, 528), (720, 552), (720, 576), (408, 0), (408, 1080), (374, 0), (374, 1080), (442, 0), (442, 1080)]
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
todas_as_sprites = pygame.sprite.Group()
player = perso.Player(x, y)
todas_as_sprites.add(player)
inimigos = pygame.sprite.Group()
bala = pygame.sprite.Group()
var_tiro = 7
desenho = False
lista_drop_vida = list()
listatempvida = list()

while True:
    var_direita = True
    var_esquerda = True
    var_cima = True
    var_baixo = True
    var_tiro += 1
    spawn = choice(coordenadas)
    relogio.tick(30)
    tela.fill((0,0,0))
    mensage = f"score : {points}"
    text = fonte.render(mensage, False, (0, 0, 0))
    tela.blit(mapa, (0,0))
    var_inimigo = randint(0, 100)
    rect = pygame.draw.rect(tela,(255, 0, 0), (x2, y2, 20, 20))

    for tiro in bala:
        tiro.movimentobala()

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

    for tiro in bala:
        for enemies in inimigos:
            if tiro.rect.colliderect(enemies):
                bala.remove(tiro)
                inimigos.remove(enemies)
                x_inimigo = enemies.coord_x()
                y_inimigo = enemies.coord_y()
                drop = pupvida.dropar(x_inimigo, y_inimigo)
                if drop[2]:
                    desenho = True
                    listatempvida.append(x_inimigo)
                    listatempvida.append(y_inimigo)
                    copia = listatempvida[:]
                    lista_drop_vida.append(copia)
                    listatempvida.clear()

                points += 1
    if desenho:
        for c in lista_drop_vida:
            pygame.draw.rect(tela, (200, 0, 0), (c[0], c[1], 20, 20))

    for tiro in bala:
        if tiro.rect.colliderect(rect):
            bala.remove(tiro)

    if 15 < var_inimigo < 20:
        inimigos.add(en.Enemies(spawn[1], spawn[0]))

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
            if event.key == K_UP and event.key == K_RIGHT and var_tiro >= 8:
                bala.add(pr.Bala(x + 25, y, 'nordeste'))
                var_tiro = 0
            if event.key == K_UP and event.key == K_LEFT and var_tiro >= 8:
                bala.add(pr.Bala(x, y, 'noroeste'))
                var_tiro = 0
            if event.key == K_DOWN and event.key == K_RIGHT and var_tiro >= 8:
                bala.add(pr.Bala(x + 25, y + 24, 'sudeste'))
                var_tiro = 0
            if event.key == K_DOWN and event.key == K_LEFT and var_tiro >= 8:
                bala.add(pr.Bala(x , y + 24, 'sudoeste'))
                var_tiro = 0
            if event.key == K_UP and event.key == K_RIGHT and var_tiro >= 8:
                bala.add(pr.Bala(x + 25, y + 1, 'nordeste'))
                var_tiro = 0
            if event.key == K_UP and var_tiro >= 8:
                bala.add(pr.Bala(x + 12, y - 1, 'cima'))
                var_tiro = 0
            if event.key == K_DOWN and var_tiro >= 8:
                bala.add(pr.Bala(x + 12, y + 25, 'baixo'))
                var_tiro = 0
            if event.key == K_LEFT and var_tiro >= 8:
                bala.add(pr.Bala(x - 1, y + 17, 'esquerda'))
                var_tiro = 0
            if event.key == K_RIGHT and var_tiro >= 8:
                bala.add(pr.Bala(x + 25, y + 17, 'direita'))
                var_tiro = 0

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
    if pygame.key.get_pressed()[K_RIGHT] and pygame.key.get_pressed()[K_UP] and var_tiro >= 8:
        bala.add(pr.Bala(x + 25, y + 1, 'nordeste'))
        var_tiro = 0
    if pygame.key.get_pressed()[K_LEFT] and pygame.key.get_pressed()[K_UP] and var_tiro >= 8:
        bala.add(pr.Bala(x, y, 'noroeste'))
        var_tiro = 0
    if pygame.key.get_pressed()[K_RIGHT] and pygame.key.get_pressed()[K_DOWN] and var_tiro >= 8:
        bala.add(pr.Bala(x + 25, y + 24, 'sudeste'))
        var_tiro = 0
    if pygame.key.get_pressed()[K_LEFT] and pygame.key.get_pressed()[K_DOWN] and var_tiro >= 8:
        bala.add(pr.Bala(x , y + 24, 'sudoeste'))
        var_tiro = 0
    if pygame.key.get_pressed()[K_UP] and var_tiro >= 8:
        bala.add(pr.Bala(x + 12, y - 1, 'cima'))
        var_tiro = 0
    if pygame.key.get_pressed()[K_DOWN] and var_tiro >= 8:
        bala.add(pr.Bala(x + 12, y + 25, 'baixo'))
        var_tiro = 0
    if pygame.key.get_pressed()[K_LEFT] and var_tiro >= 8:
        bala.add(pr.Bala(x - 1, y + 17, 'esquerda'))
        var_tiro = 0
    if pygame.key.get_pressed()[K_RIGHT] and var_tiro >= 8:
        bala.add(pr.Bala(x + 25, y + 17, 'direita'))
        var_tiro = 0

    rect = pygame.draw.rect(tela,(250, 0, 0), (x2, y2, 20, 20))

    for sprite in todas_as_sprites:
        for enemies in inimigos:
            if sprite.rect.colliderect(enemies):
                print('DERROTA')
                exit()

    for enemies in inimigos:
        if enemies.rect.colliderect(rect):
            print('game over!')
            exit()

    if points >= 50:
        print('parabens caraio')
        exit()

    inimigos.draw(tela)

    for enemy in inimigos:
        enemy.movimento()

    bala.draw(tela)

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
    bala.update()
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.update()

import pygame
import enemies as en
import projetil as pr
from pygame.locals import *
from sys import exit
from random import randint
from random import choice
import personagem as perso
import drops
import mapa as mp

pygame.init()

# olhar linha 141 e 259
larg = 1080
alt = 720
fonte = pygame.font.SysFont('arial', 20, True, True)
fonte_inicial = pygame.font.SysFont('arial', 3000, True, False)
fonte2 = pygame.font.SysFont('arial', 120, True, False)
tela = pygame.display.set_mode((larg, alt))
texto_inicial = fonte.render('AssaCInato!', False, (0, 0, 0))
pygame.display.set_caption('AssaCInato')
menu_image = pygame.image.load('sprites/menu.png')

class Almoco(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/geladeira.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = 520, 360


def pause():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    main()


def cria_Botao(msg, x, y, larg, alt, hover, cor):
    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed(3)

    if(x + larg > mouse[0] and y + alt > mouse[1] > y):
        pygame.draw.rect(tela, hover, (int(x), int(y), int(larg), int(alt)))
        if(click[0] == 1):
            main()

    else:
        pygame.draw.rect(tela, cor, (x, y, larg, alt))

    texto_botao = (fonte.render(msg, True, (255, 0, 0)))
    tela.blit(texto_botao, ((540), int(y)))


def menu():
    titulo = fonte2.render("NOME DO JOGO", True, (255, 0, 0))

    while True:
        tela.blit(menu_image, (0, 0))
        cria_Botao("JOGAR", (larg / 2), (alt / 2),
                   150, 150, (15, 15, 15), (0, 0, 0))
        tela.blit(titulo, (65, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()


def main():
    coordenadas_y = [408, 374, 442, 0, 720]
    coordenadas_x = [504, 528, 552, 576, 0, 1080]
    coordenadas = [(0, 520), (0, 480), (0, 560), (720, 520), (720, 480), (720, 560),
                   (320, 0), (320, 1080), (360, 0), (360, 1080), (400, 0), (400, 1080)]
    space = False
    var_pause = False
    points = 0
    x = 520
    y = 320
    x2 = 520
    y2 = 360
    xbv = 0
    ybv = 0
    var_inimigo = 0
    relogio = pygame.time.Clock()

    mapa = pygame.image.load('sprites/mapamundi.png')

    #corações:
    coracao = pygame.image.load(
        'sprites/heart_pixel_art_16x16_20x20.png').convert_alpha()
    coracao_vivo = pygame.image.load('sprites/coracao48.png')
    coracao_morto = pygame.image.load('sprites/coracao_morto.png')

    bota = pygame.image.load('sprites/botas1.png')
    todas_as_sprites = pygame.sprite.Group()
    sprite_almoco = pygame.sprite.Group()
    almoco = Almoco()
    sprite_almoco.add(almoco)
    player = perso.Player(x, y)
    todas_as_sprites.add(player)
    inimigos = pygame.sprite.Group()
    bala = pygame.sprite.Group()
    var_tiro = 7
    mapa = mp.map(tela)

    speed = False
    pegar_bota = False
    efeito_velocidade = False
    lista_speed = list()
    listatempspeed = list()

    desenho_vida = False
    pegar_vida = False
    lista_drop_vida = list()
    listatempvida = list()
    texto_perdeu = fonte2.render('YOU LOSE!', False, (255, 0, 0))
    texto_ganhou = fonte2.render("YOU WIN!", False, (0, 255, 0))
    lista_barra_vida = [[5, 5], [58, 5], [111, 5], [164, 5], [217, 5]]
    coordenadas_vida = ([5, 5], [58, 5], [111, 5], [164, 5], [217, 5])
    lista_passagem_vida = []

    while True:
        if var_pause == True:
            pause()
        var_direita = True
        var_esquerda = True
        var_cima = True
        var_baixo = True
        var_tiro += 1
        spawn = choice(coordenadas)
        relogio.tick(30)
        tela.fill((0,0,0))
        mapa.draw_mapa()
        var_inimigo = randint(0, 100)
 
        # desenhar cada coração cinza e vermelho (por cima)
        for r in coordenadas_vida:
            tela.blit(coracao_morto, (r[0], r[1]))
        for c in lista_barra_vida:
            tela.blit(coracao_vivo, (c[0], c[1]))

        for tiro in bala:
            tiro.movimentobala()

        for sprite in todas_as_sprites:
            if sprite.rect.colliderect(almoco):
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
                    drop = drops.dropar_vida(x_inimigo, y_inimigo)
                    drop2 = drops.dropar_bota(x_inimigo, y_inimigo)


                    #condição pra dropar o 'coração de vida'
                    if drop[2]:
                        desenho_vida = True
                        listatempvida.append(x_inimigo)
                        listatempvida.append(y_inimigo)
                        copia = listatempvida[:]
                        lista_drop_vida.append(copia)
                        listatempvida.clear()

                    #condição pra dropar a 'bota'
                    if drop2[2] and speed == False:
                        speed = True
                        listatempspeed.append(x_inimigo)
                        listatempspeed.append(y_inimigo)
                        copia2 = listatempspeed[:]
                        lista_speed.append(copia2)
                        listatempspeed.clear()
                    points += 1

        if speed:
            if len(lista_speed) >= 1:
                for c in lista_speed:
                    bota_rect = bota.get_rect(topleft = (c[0], c[1]))
                for sprite in todas_as_sprites:
                    if sprite.rect.colliderect(bota_rect):
                        pegar_bota = True
                        del lista_speed[0]

        for c in lista_speed:
            tela.blit(bota, (c[0], c[1]))
                            
        if desenho_vida:
            if len(lista_drop_vida) >= 1:
                for c in lista_drop_vida:
                    coracao_rect = coracao.get_rect(topleft=(c[0], c[1]))
                    for sprite in todas_as_sprites:
                        if sprite.rect.colliderect(coracao_rect):
                            pegar_vida = True
                            lista_passagem_vida.append(c)

        for c in lista_drop_vida:
            tela.blit(coracao, (c[0], c[1]))

        for tiro in bala:
            if tiro.rect.colliderect(almoco):
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
                    if pegar_bota == True:
                        x -= 5
                    player.esquerda(x, y)
                if event.key == K_d and x != 1055 and var_direita == True:
                    x += 5
                    if pegar_bota == True:
                        x += 5
                    player.direita(x, y)
                if event.key == K_w and y != 0 and var_cima == True:
                    y -= 5
                    if pegar_bota == True:
                        y -= 5
                    player.cima(x, y)
                if event.key == K_s and y != 685 and var_baixo == True:
                    y += 5
                    if pegar_bota == True:
                        y += 5
                    player.baixo(x, y)
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
                    bala.add(pr.Bala(x, y + 24, 'sudoeste'))
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
                if event.key == K_SPACE:
                    if pegar_vida:
                        if len(lista_barra_vida) < 5:
                            qtd = len(lista_barra_vida)
                            lista_barra_vida.append(coordenadas_vida[qtd])
                            indice_coord = lista_passagem_vida[-1]
                            indice_apagar_vida = lista_drop_vida.index(
                                indice_coord)
                            del lista_drop_vida[indice_apagar_vida]
                            pegar_vida = False

        if pygame.key.get_pressed()[K_a] and x != 0 and var_esquerda == True:
            x -= 5
            if pegar_bota == True:
                x -= 5
            player.esquerda(x, y)
        if pygame.key.get_pressed()[K_d] and x != 1055 and var_direita == True:
            x += 5
            if pegar_bota == True:
                x += 5
            player.direita(x, y)
        if pygame.key.get_pressed()[K_w] and y != 0 and var_cima == True:
            y -= 5
            if pegar_bota == True:
                y -= 5
            player.cima(x, y)
        if pygame.key.get_pressed()[K_s] and y != 685 and var_baixo == True:
            y += 5
            if pegar_bota == True:
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
            bala.add(pr.Bala(x, y + 24, 'sudoeste'))
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

        for sprite in todas_as_sprites:
            for enemies in inimigos:
                if sprite.rect.colliderect(enemies):
                    # quando encostar no player perde 1 barra de vida
                    if len(lista_barra_vida) > 1:
                        inimigos.remove(enemies)
                        quantidade = len(lista_barra_vida) - 1
                        del lista_barra_vida[quantidade]

                    else:
                        inimigos.remove(enemies)
                        quantidade = len(lista_barra_vida) - 1
                        del lista_barra_vida[quantidade]
                        tela.blit(texto_perdeu, (250, 300))
                        var_pause = True
                        tela.blit(coracao_morto, (5, 5))

        for enemies in inimigos:
            if enemies.rect.colliderect(almoco):
                tela.blit(texto_perdeu, (250, 300))
                var_pause = True

        if points >= 50:
            tela.blit(texto_ganhou, (250, 300))
            var_pause = True

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

        mensage = f"score : {points}"
        text = fonte.render(mensage, False, (255, 255, 255))
        tela.blit(text, (980, 10))
        # if space == False:
        # tela.blit(texto_inicial, (500, 240))      #esse era o if que apagava o nome 'assacinato'

        inimigos.update()
        bala.update()
        sprite_almoco.draw(tela)
        todas_as_sprites.draw(tela)
        todas_as_sprites.update()
        pygame.display.update()
     
# main()
menu()

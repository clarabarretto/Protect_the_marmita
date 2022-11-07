import pygame
import enemies as en
import drops
import projetil as pr

from pygame.locals import *
from sys import exit
from random import randint
from random import choice
import personagem as perso
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
pygame.display.set_caption('Protect the Marmita!')
menu_image = pygame.image.load('sprites/menu.jpg')

pygame.mixer.init()

pygame.mixer.music.load("sounds/theme.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

som_dano = pygame.mixer.Sound('sounds/hurt.wav')
som_morte = pygame.mixer.Sound('sounds/dano.wav')
som_morte_inimigo = pygame.mixer.Sound('sounds/morte.wav')
som_bala = pygame.mixer.Sound('sounds/bala.wav')
som_dano_geladeira = pygame.mixer.Sound('sounds/dano_geladeira.mp3')
som_passos = pygame.mixer.Sound('sounds/andando.mpeg')

class Almoco(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/geladeira.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = 520, 360

def gun_dispare(x, y, bala):
    bala.add(pr.Bala(x + 25, y, 'nordeste'))
    bala.add(pr.Bala(x, y, 'noroeste'))
    bala.add(pr.Bala(x + 25, y + 24, 'sudeste'))
    bala.add(pr.Bala(x, y + 24, 'sudoeste'))
    bala.add(pr.Bala(x + 25, y + 1, 'nordeste'))
    bala.add(pr.Bala(x + 12, y - 1, 'cima'))
    bala.add(pr.Bala(x + 12, y + 25, 'baixo'))
    bala.add(pr.Bala(x - 1, y + 17, 'esquerda'))
    bala.add(pr.Bala(x + 25, y + 17, 'direita'))
    return bala
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

    if(x - 70 + larg > mouse[0] and y - 80 + alt > mouse[1] > y - 80):
        pygame.draw.rect(tela, hover, (int(x - 70), int(y - 80), int(larg), int(alt)))
        if(click[0] == 1):
            main()

    else:
        pygame.draw.rect(tela, cor, (x - 70, y -80 , larg, alt))

    texto_botao = (fonte.render(msg, True, (255, 0, 0)))
    tela.blit(texto_botao, ((510), int(y - 50)))


def menu():

    while True:
        tela.blit(menu_image, (0, 0))
        cria_Botao("JOGAR", ((larg / 2)), ((alt / 2)),
                   150, 80, (15, 15, 15), (0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()


def main():
    coordenadas = [(0, 520), (0, 480), (0, 560), (720, 520), (720, 480), (720, 560),
                   (320, 0), (320, 1080), (360, 0), (360, 1080), (400, 0), (400, 1080)]
    var_pause = False
    points = 0
    x = 520
    y = 320
    x2 = 520
    y2 = 360
    var_inimigo = 0
    relogio = pygame.time.Clock()
    var_tempo = 0
    qntd_inimigos = 0

    

    #corações:
    coracao = pygame.image.load(
        'sprites/heart_pixel_art_16x16_20x20.png').convert_alpha()
    coracao_vivo = pygame.image.load('sprites/coracao48.png')
    coracao_morto = pygame.image.load('sprites/coracao_morto.png')

    bota = pygame.image.load('sprites/botas1.png')
    arma = pygame.image.load('sprites/specialgun.png')
    ceifador_imagem = pygame.image.load('sprites/deadall.png')
    cartucho_imagem = pygame.image.load('sprites/cartuchorapido.png')

    todas_as_sprites = pygame.sprite.Group()
    sprite_almoco = pygame.sprite.Group()
    almoco = Almoco()
    sprite_almoco.add(almoco)
    player = perso.Player(x, y)
    todas_as_sprites.add(player)
    inimigos = pygame.sprite.Group()
    bala = pygame.sprite.Group()
    var_tiro = 7
    vida_almoco = 5
    var_parado = 0
    mapa = mp.map(tela)
    obstaculos = mapa.check_obstaculos()
    var_som = 0

    #sempre usar a variavel que tem pegar antes 

    #cartucho
    ceifador = False
    pegar_ceifador = False
    lista_ceifador = list()
    listatempceifador = list()
    var_tempo_ceifador_drop = 0

    #cartucho
    cartucho = False
    pegar_cartucho = False
    lista_cartucho = list()
    listatempcartucho = list()
    var_tempo_cartucho = 0
    var_tempo_cartucho_drop = 0

    #bota
    speed = False
    pegar_bota = False
    lista_speed = list()
    listatempspeed = list()
    var_tempo_bota = 0
    var_tempo_bota_drop = 0

    #specila gun
    gun = False
    pegar_gun = False
    lista_gun = list()
    listatempgun = list()
    var_tempo_gun = 0
    var_tempo_gun_drop = 0

    #vida
    desenho_vida = False
    pegar_vida = False
    lista_drop_vida = list()
    listatempvida = list()
    texto_perdeu = fonte2.render('FOI DE F!', False, (255, 0, 0))
    texto_ganhou = fonte2.render("YOU WON!", False, (0, 255, 0))
    lista_barra_vida = [[5, 5], [58, 5], [111, 5], [164, 5], [217, 5]]
    coordenadas_vida = ([5, 5], [58, 5], [111, 5], [164, 5], [217, 5])
    lista_passagem_vida = []

    moedas = pygame.sprite.Group()
    moeda1 = 0
    moeda3 = 0
    moeda5 = 0

    while True:
        if var_pause == True:
            pause()
        var_tempo_gun_drop -= 1
        var_tempo_bota_drop -= 1
        var_tempo_cartucho_drop -= 1
        var_tempo_ceifador_drop -= 1
        if var_tempo_ceifador_drop == 0:
            lista_ceifador.clear()
            ceifador = False
        if var_tempo_gun_drop == 0:
            lista_gun.clear()
            gun = False
        if var_tempo_bota_drop == 0:
            lista_speed.clear()
            speed = False
        if var_tempo_cartucho_drop == 0:
            lista_cartucho.clear()
            cartucho = False
        var_tempo_bota -= 1
        if var_tempo_bota == 0:
            speed = False
            pegar_bota = False
        var_tempo_gun -= 1
        if var_tempo_gun == 0:
            gun = False
            pegar_gun = False
        var_tempo_cartucho -= 1
        if var_tempo_cartucho == 0:
            cartucho = False
            pegar_cartucho = False
        if pegar_cartucho is True:
            var_tiro += 3
        var_tempo += 1
        var_parado += 1
        var_direita = True
        var_esquerda = True
        var_cima = True
        var_baixo = True
        var_tiro += 1
        var_som += 1
        if var_tiro >= 8:     
            var_sprite_tiro = None
        spawn = choice(coordenadas)
        obstaculos.draw(tela)
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
                if x == x2 - 32:
                    var_direita = False
                if x == x2 + 32:
                    var_esquerda = False
                if y == y2 - 32:
                    var_baixo = False
                if y == y2 + 32:
                    var_cima = False
                if x == x2 - 34:
                    var_direita = False
                if x == x2 + 34:
                    var_esquerda = False
                if y == y2 - 34:
                    var_baixo = False
                if y == y2 + 34:
                    var_cima = False
                if x == x2 - 36:
                    var_direita = False
                if x == x2 + 36:
                    var_esquerda = False
                if y == y2 - 36:
                    var_baixo = False
                if y == y2 + 36:
                    var_cima = False
                if x == x2 - 38:
                    var_direita = False
                if x == x2 + 38:
                    var_esquerda = False
                if y == y2 - 38:
                    var_baixo = False
                if y == y2 + 38:
                    var_cima = False
                if x == x2 - 40:
                    var_direita = False
                if x == x2 + 40:
                    var_esquerda = False
                if y == y2 - 40:
                    var_baixo = False
                if y == y2 + 40:
                    var_cima = False
        
        for sprite in todas_as_sprites:
            for obs in obstaculos:
                if sprite.rect.colliderect(obs):
                    if x == obs.coord_x() - 32:
                        var_direita = False
                    if x == obs.coord_x() + 32:
                        var_esquerda = False
                    if y == obs.coord_y() - 32:
                        var_baixo = False
                    if y == obs.coord_y() + 32:
                        var_cima = False
                    if x == obs.coord_x() - 34:
                        var_direita = False
                    if x == obs.coord_x() + 34:
                        var_esquerda = False
                    if y == obs.coord_y() - 34:
                        var_baixo = False
                    if y == obs.coord_y() + 34:
                        var_cima = False
                    if x == obs.coord_x() - 36:
                        var_direita = False
                    if x == obs.coord_x() + 36:
                        var_esquerda = False
                    if y == obs.coord_y() - 36:
                        var_baixo = False
                    if y == obs.coord_y() + 36:
                        var_cima = False
                    if x == obs.coord_x() - 38:
                        var_direita = False
                    if x == obs.coord_x() + 38:
                        var_esquerda = False
                    if y == obs.coord_y() - 38:
                        var_baixo = False
                    if y == obs.coord_y() + 38:
                        var_cima = False
                    if x == obs.coord_x() - 40:
                        var_direita = False
                    if x == obs.coord_x() + 40:
                        var_esquerda = False
                    if y == obs.coord_y() - 40:
                        var_baixo = False
                    if y == obs.coord_y() + 40:
                        var_cima = False
        
        for tiro in bala:
            for enemies in inimigos:
                if tiro.rect.colliderect(enemies):
                    bala.remove(tiro)
                    inimigos.remove(enemies)
                    x_inimigo = enemies.coord_x()
                    y_inimigo = enemies.coord_y()
                    som_morte_inimigo.play()
                    escolha_moedas = randint(1, 100)
                    if escolha_moedas <= 19:
                        moedas.add(drops.Moedas(enemies.coord_x(), enemies.coord_y()))
                    drop = drops.dropar_vida(x_inimigo, y_inimigo)
                    drop2 = drops.dropar_bota(x_inimigo, y_inimigo)
                    drop3 = drops.dropar_gun(x_inimigo, y_inimigo)
                    drop4 = drops.dropar_tiro_rapido(x_inimigo, y_inimigo)
                    drop5 = drops.dropar_ceifador(x_inimigo, y_inimigo)
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
                        var_tempo_bota_drop = 500
                        listatempspeed.append(x_inimigo)
                        listatempspeed.append(y_inimigo)
                        copia2 = listatempspeed[:]
                        lista_speed.append(copia2)
                        listatempspeed.clear()

                    #condiação pra dropar 'special gun'
                    if drop3[2] and gun == False:
                        gun = True
                        var_tempo_gun_drop = 500
                        listatempgun.append(x_inimigo)
                        listatempgun.append(y_inimigo)
                        copia3 = listatempgun[:]
                        lista_gun.append(copia3)
                        listatempgun.clear()

                    #condição pra dropar 'cartucho'
                    if drop4[2] and cartucho is False:
                        cartucho = True
                        var_tempo_cartucho_drop = 500
                        listatempcartucho.append(x_inimigo)
                        listatempcartucho.append(y_inimigo)
                        copia4 = listatempcartucho[:]
                        lista_cartucho.append(copia4)
                        listatempcartucho.clear()

                    #condição pra dropar 'ceifador'
                    if drop5[2] and ceifador is False:
                        ceifador = True
                        var_tempo_ceifador_drop = 500
                        listatempceifador.append(x_inimigo)
                        listatempceifador.append(y_inimigo)
                        copia5 = listatempceifador[:]
                        lista_ceifador.append(copia5)
                        listatempceifador.clear()

        for sprite in todas_as_sprites:
            for moeda in moedas:
                if sprite.rect.colliderect(moeda):
                    if moeda.identify_moeda() == 'moeda1':
                        moeda1 += 1
                        points += 1
                    elif moeda.identify_moeda() == 'moeda3':
                        moeda3 += 1
                        points += 3
                    elif moeda.identify_moeda() == 'moeda5':
                        moeda5 += 1
                        points += 5
                    moedas.remove(moeda)


        for tiro in bala:
            if tiro.coordenadas()[0] > 1080 or tiro.coordenadas()[0] < 0:
                bala.remove(tiro)
            if tiro.coordenadas()[1] > 720 or tiro.coordenadas()[1] < 0:
                bala.remove(tiro)


        if cartucho:
            if len(lista_cartucho) >= 1:
                for c in lista_cartucho:
                    cartucho_rect = cartucho_imagem.get_rect(topleft = (c[0], c[1]))
                    for sprite in todas_as_sprites:
                        if sprite.rect.colliderect(cartucho_rect):
                            pegar_cartucho = True
                            var_tempo_cartucho = 700
                            var_tempo_cartucho_drop = 0
                            del lista_cartucho[0]

        for c in lista_cartucho:
            tela.blit(cartucho_imagem, (c[0], c[1]))

        if ceifador:
            if len(lista_ceifador) >= 1:
                for c in lista_ceifador:
                    ceifador_rect = ceifador_imagem.get_rect(topleft = (c[0], c[1]))
                    for sprite in todas_as_sprites:
                        if sprite.rect.colliderect(ceifador_rect):
                            pegar_ceifador = True
                            var_tempo_ceifador_drop = 0
                            del lista_ceifador[0]
        
        if pegar_ceifador:
            ceifador = False
            pegar_ceifador = False
            for enemie in inimigos:
                inimigos.remove(enemie)
                som_morte_inimigo.play()
                


        for c in lista_ceifador:
            tela.blit(ceifador_imagem, (c[0], c[1]))

        if gun:
            if len(lista_gun) >= 1:
                for c in lista_gun:
                    arma_rect = arma.get_rect(topleft = (c[0], c[1]))
                    for sprite in todas_as_sprites:
                        if sprite.rect.colliderect(arma_rect):
                            pegar_gun = True
                            var_tempo_gun = 700
                            var_tempo_gun_drop = 0
                            del lista_gun[0]

        for c in lista_gun:
            tela.blit(arma, (c[0], c[1]))

        if speed:
            if len(lista_speed) >= 1:
                for c in lista_speed:
                    bota_rect = bota.get_rect(topleft = (c[0], c[1]))
                for sprite in todas_as_sprites:
                    if sprite.rect.colliderect(bota_rect):
                        pegar_bota = True
                        var_tempo_bota = 700
                        var_tempo_bota_drop = 0
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

        if qntd_inimigos <= 499:
            if qntd_inimigos < 50:
                if 18 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1
            elif qntd_inimigos >= 50 and qntd_inimigos < 200:
                if 16 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1
            elif qntd_inimigos >= 200 and qntd_inimigos < 250:
                if 14 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1
            elif qntd_inimigos >= 250 and qntd_inimigos < 300:
                if 18 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1
            elif qntd_inimigos >= 300 and qntd_inimigos < 350:
                if 16 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1
            elif qntd_inimigos >= 350 and qntd_inimigos < 400:
                if 14 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1
            elif qntd_inimigos >= 400 and qntd_inimigos < 450:
                if 16 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1
            elif qntd_inimigos >= 450 and qntd_inimigos < 500:
                if 14 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1
            elif qntd_inimigos >= 500 and qntd_inimigos < 550:
                if 18 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1
            elif qntd_inimigos >= 550 and qntd_inimigos < 700:
                if 16 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1
            elif qntd_inimigos >= 700 and qntd_inimigos < 800:
                if 14 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1
            elif qntd_inimigos >= 800 and qntd_inimigos < 850:
                if 10 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1
            elif qntd_inimigos >= 850 and qntd_inimigos < 900:
                if 18 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1
            elif qntd_inimigos >= 900 and qntd_inimigos < 1000:
                if 14 <= var_inimigo <= 20:
                    inimigos.add(en.Enemies(spawn[1], spawn[0]))
                    qntd_inimigos += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_UP and event.key == K_RIGHT and var_tiro >= 8:
                    if pegar_gun == False:
                        bala.add(pr.Bala(x + 25, y, 'nordeste'))
                        som_bala.play()
                    else:
                        gun_dispare(x, y, bala)
                    player.tiro_cima(x, y)
                    var_sprite_tiro = 'cima'
                    var_parado = 0
                    var_tiro = 0
                    som_bala.play()
                if event.key == K_UP and event.key == K_LEFT and var_tiro >= 8:
                    if pegar_gun == False:
                        bala.add(pr.Bala(x, y, 'noroeste'))
                        som_bala.play()
                    else:
                        bala = gun_dispare(x, y, bala)
                    player.tiro_cima(x, y)
                    var_sprite_tiro = 'cima'
                    var_parado = 0
                    var_tiro = 0
                    som_bala.play()
                if event.key == K_DOWN and event.key == K_RIGHT and var_tiro >= 8:
                    if pegar_gun == False:
                        bala.add(pr.Bala(x + 25, y + 24, 'sudeste'))
                        som_bala.play()
                    else:
                        bala = gun_dispare(x, y, bala)
                    player.tiro_baixo(x, y)
                    var_sprite_tiro = 'baixo'
                    var_parado = 0
                    var_tiro = 0
                    som_bala.play()
                if event.key == K_DOWN and event.key == K_LEFT and var_tiro >= 8:
                    if pegar_gun == False:
                        bala.add(pr.Bala(x, y + 24, 'sudoeste'))
                        som_bala.play()
                    else:
                        bala = gun_dispare(x, y, bala)
                    player.tiro_baixo(x, y)
                    var_sprite_tiro = 'baixo'
                    var_parado = 0
                    var_tiro = 0
                    som_bala.play()
                if event.key == K_UP and event.key == K_RIGHT and var_tiro >= 8:
                    if pegar_gun == False:
                        bala.add(pr.Bala(x + 25, y + 1, 'nordeste'))
                        som_bala.play()
                    else:
                        bala = gun_dispare(x, y, bala)
                    player.tiro_cima(x, y)
                    var_sprite_tiro = 'baixo'
                    var_parado = 0
                    var_tiro = 0
                    som_bala.play()
                if event.key == K_UP and var_tiro >= 8:
                    if pegar_gun == False:
                        bala.add(pr.Bala(x + 12, y - 1, 'cima'))
                        som_bala.play()
                    else:
                        bala = gun_dispare(x, y, bala)
                    player.tiro_cima(x, y)
                    var_sprite_tiro = 'cima'
                    var_parado = 0
                    var_tiro = 0
                    som_bala.play()
                if event.key == K_DOWN and var_tiro >= 8:
                    if pegar_gun == False:
                        bala.add(pr.Bala(x + 12, y + 25, 'baixo'))
                        som_bala.play()
                    else:
                        bala = gun_dispare(x, y, bala)
                    player.tiro_baixo(x, y)
                    var_sprite_tiro = 'baixo'
                    var_parado = 0
                    var_tiro = 0
                    som_bala.play()
                if event.key == K_LEFT and var_tiro >= 8:
                    if pegar_gun == False:
                        bala.add(pr.Bala(x - 1, y + 17, 'esquerda'))
                        som_bala.play()
                    else:
                        bala = gun_dispare(x, y, bala)
                    player.tiro_esquerda(x, y)
                    var_sprite_tiro = 'esquerda'
                    var_parado = 0
                    var_tiro = 0
                    som_bala.play()
                if event.key == K_RIGHT and var_tiro >= 8:
                    if pegar_gun == False:
                        bala.add(pr.Bala(x + 25, y + 17, 'direita'))
                        som_bala.play()
                    else:
                        bala = gun_dispare(x, y, bala)
                    player.tiro_direita(x, y)
                    var_sprite_tiro = 'direita'
                    var_parado = 0
                    var_tiro = 0
                    som_bala.play()
                if event.key == K_a and x != 0 and var_esquerda == True:
                    if var_som > 8:
                        som_passos.play()
                        var_som = 0
                    if pegar_bota == False:
                        x -= 4
                    var_parado = 0
                    if pegar_bota == True:
                        x -= 8
                    if var_sprite_tiro is None:
                        player.esquerda(x, y)
                    else:
                        player.movimento_tiro(x, y, var_sprite_tiro)
                if event.key == K_d and x != 1055 and var_direita == True:
                    if var_som > 8:
                        som_passos.play()
                        var_som = 0
                    if pegar_bota == False:
                        x += 4
                    var_parado = 0
                    if pegar_bota == True:
                        x += 8
                    if var_sprite_tiro is None:
                        player.direita(x, y)
                    else:
                        player.movimento_tiro(x, y, var_sprite_tiro)
                if event.key == K_w and y != 0 and var_cima == True:
                    if var_som > 8:
                        som_passos.play()
                        var_som = 0
                    if pegar_bota == False:
                        y -= 4
                    var_parado = 0
                    if pegar_bota == True:
                        y -= 8
                    if var_sprite_tiro is None:
                        player.cima(x, y)
                    else:
                        player.movimento_tiro(x, y, var_sprite_tiro)
                if event.key == K_s and y != 685 and var_baixo == True:
                    if var_som > 8:
                        som_passos.play()
                        var_som = 0
                    if pegar_bota == False:
                        y += 4
                    var_parado = 0
                    if pegar_bota == True:
                        y += 8
                    if var_sprite_tiro is None:
                        player.baixo(x, y)
                    else:
                        player.movimento_tiro(x, y, var_sprite_tiro)
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

        if pygame.key.get_pressed()[K_RIGHT] and pygame.key.get_pressed()[K_UP] and var_tiro >= 8:
            if pegar_gun == False:
                bala.add(pr.Bala(x + 25, y + 1, 'nordeste'))
                som_bala.play()
            else:
                bala = gun_dispare(x, y, bala)
            player.tiro_cima(x, y)
            var_sprite_tiro = 'cima'
            var_parado = 0
            var_tiro = 0
            som_bala.play()
        if pygame.key.get_pressed()[K_LEFT] and pygame.key.get_pressed()[K_UP] and var_tiro >= 8:
            if pegar_gun == False:
                bala.add(pr.Bala(x, y, 'noroeste'))
                som_bala.play()
            else:
                bala = gun_dispare(x, y, bala)
            player.tiro_cima(x, y)
            var_sprite_tiro = 'cima'
            var_parado = 0
            var_tiro = 0
            som_bala.play()
        if pygame.key.get_pressed()[K_RIGHT] and pygame.key.get_pressed()[K_DOWN] and var_tiro >= 8:
            if pegar_gun == False:
                bala.add(pr.Bala(x + 25, y + 24, 'sudeste'))
                som_bala.play()
            else:
                bala = gun_dispare(x, y, bala)
            player.tiro_baixo(x, y)
            var_sprite_tiro = 'baixo'
            var_parado = 0
            var_tiro = 0
            som_bala.play()
        if pygame.key.get_pressed()[K_LEFT] and pygame.key.get_pressed()[K_DOWN] and var_tiro >= 8:
            if pegar_gun == False:
                bala.add(pr.Bala(x, y + 24, 'sudoeste'))
                som_bala.play()
            else:
                bala = gun_dispare(x, y, bala)
            player.tiro_baixo(x, y)
            var_sprite_tiro = 'baixo'
            var_parado = 0
            var_tiro = 0
            som_bala.play()
        if pygame.key.get_pressed()[K_UP] and var_tiro >= 8:
            if pegar_gun == False:
                bala.add(pr.Bala(x + 12, y - 1, 'cima'))
                som_bala.play()
            else:
                bala = gun_dispare(x, y, bala)
            player.tiro_cima(x, y)
            var_sprite_tiro = 'cima'
            var_parado = 0
            var_tiro = 0
            som_bala.play()
        if pygame.key.get_pressed()[K_DOWN] and var_tiro >= 8:
            if pegar_gun == False:
                bala.add(pr.Bala(x + 12, y + 25, 'baixo'))
                som_bala.play()
            else:
                bala = gun_dispare(x, y, bala)
            player.tiro_baixo(x, y)
            var_sprite_tiro = 'baixo'
            var_parado = 0
            var_tiro = 0
            som_bala.play()
        if pygame.key.get_pressed()[K_LEFT] and var_tiro >= 8:
            if pegar_gun == False:
                bala.add(pr.Bala(x - 1, y + 17, 'esquerda'))
                som_bala.play()
            else:
                bala = gun_dispare(x, y, bala)
            player.tiro_esquerda(x, y)
            var_sprite_tiro = 'esquerda'
            var_parado = 0
            var_tiro = 0
            som_bala.play()
        if pygame.key.get_pressed()[K_RIGHT] and var_tiro >= 8:
            if pegar_gun == False:
                bala.add(pr.Bala(x + 25, y + 17, 'direita'))
                som_bala.play()
            else:
                bala = gun_dispare(x, y, bala)
            player.tiro_direita(x, y)
            var_sprite_tiro = 'direita'
            var_parado = 0
            var_tiro = 0
            som_bala.play()
        if pygame.key.get_pressed()[K_a] and x != 0 and var_esquerda == True:
            if var_som > 8:
                som_passos.play()
                var_som = 0
            if pegar_bota == False:
                x -= 4
            var_parado = 0
            if pegar_bota == True:
                x -= 8
            if var_sprite_tiro is None:
                player.esquerda(x, y)
            else:
                player.movimento_tiro(x, y, var_sprite_tiro)
        if pygame.key.get_pressed()[K_d] and x != 1055 and var_direita == True:
            if var_som > 8:
                som_passos.play()
                var_som = 0
            if pegar_bota == False:
                x += 4
            var_parado = 0
            if pegar_bota == True:
                x += 8
            if var_sprite_tiro is None:
                player.direita(x, y)
            else:
                player.movimento_tiro(x, y, var_sprite_tiro)
        if pygame.key.get_pressed()[K_w] and y != 0 and var_cima == True:
            if var_som > 8:
                som_passos.play()
                var_som = 0
            if pegar_bota == False:
                y -= 4
            var_parado = 0
            if pegar_bota == True:
                y -= 8
            if var_sprite_tiro is None:
                player.cima(x, y)
            else:
                player.movimento_tiro(x, y, var_sprite_tiro)
        if pygame.key.get_pressed()[K_s] and y != 685 and var_baixo == True:
            if var_som > 8:
                som_passos.play()
                var_som = 0
            if pegar_bota == False:
                y += 4
            var_parado = 0
            if pegar_bota == True:
                y += 8
            if var_sprite_tiro is None:
                player.baixo(x, y)
            else:
                player.movimento_tiro(x, y, var_sprite_tiro)
        if var_parado >= 8:
            player.parado(x, y)

        for sprite in todas_as_sprites:
            for enemies in inimigos:
                if sprite.rect.colliderect(enemies):
                    # quando encostar no player perde 1 barra de vida
                    points += 1
                    if len(lista_barra_vida) > 1:
                        som_dano.play()
                        inimigos.remove(enemies)
                        quantidade = len(lista_barra_vida) - 1
                        del lista_barra_vida[quantidade]
                        

                    else:
                        som_morte.play()
                        inimigos.remove(enemies)
                        quantidade = len(lista_barra_vida) - 1
                        del lista_barra_vida[quantidade]
                        tela.blit(texto_perdeu, (250, 300))
                        var_pause = True
                        tela.blit(coracao_morto, (5, 5))

        for enemies in inimigos:
            if enemies.rect.colliderect(almoco):
                vida_almoco -= 1
                inimigos.remove(enemies)
                som_dano_geladeira.play()
                tela.blit(texto_perdeu, (250, 300))
                var_pause = True

        if points >= 500:
            tela.blit(texto_ganhou, (250, 300))
            var_pause = True

        inimigos.draw(tela)

        for enemy in inimigos:
            enemy.movimento(x, y, x2, y2)

        bala.draw(tela)

        mensage = f"score : {points}"
        text = fonte.render(mensage, False, (255, 255, 255))
        tela.blit(text, (960, 10))
            #esse era o if que apagava o nome 'assacinato'
        moedas.draw(tela)
        moedas.update()
        inimigos.update()
        bala.update()
        sprite_almoco.draw(tela)
        todas_as_sprites.draw(tela)
        obstaculos.update()
        todas_as_sprites.update()
        pygame.display.update()
     
# main()
menu()




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

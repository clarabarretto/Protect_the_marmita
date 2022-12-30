

time1 = input()
time2 = input()
gols_time1 = 0
gols_time2 = 0
i = 0

while True:
    i += 1
    finalizacao = input()
    if finalizacao == 'gol':
        if i%2 == 0:
            gols_time2 += 1
        elif i%2 == 1:
            gols_time1 += 1
    if i >= 5:
        if gols_time1 == gols_time2 and i == 10:
            print(f'Ambas as seleções terminaram com {gols_time1} gols, mas o desempate vai ficar para outro dia.')
        elif i%2 == 0:
            rodadas_restantes = (10 - i)/2
            if gols_time1 > gols_time2:
                teste2 = rodadas_restantes + gols_time2
                if gols_time1 > teste2:
                    print(f'{time1} vence a disputa de pênaltis por {gols_time1} a {gols_time2} e avança de fase!')
                    break
            elif gols_time2 > gols_time1:
                teste2 = rodadas_restantes + gols_time1
                if gols_time2 > teste2:
                    print(f'{time2} vence a disputa de pênaltis por {gols_time2} a {gols_time1} e avança de fase!')
                    break
            teste2 = 0
        elif i%2 == 1:
            rodadas_restantes = (10 - i)//2
            rodadas_time1 = rodadas_restantes
            rodadas_time2 = rodadas_time1 + 1
            if gols_time1 > gols_time2:
                teste1 = gols_time2 + rodadas_time2
                if gols_time1 > teste1:
                    print(f'{time1} vence a disputa de pênaltis por {gols_time1} a {gols_time2} e avança de fase!')
                    break
            elif gols_time2 > gols_time1:
                teste1 = gols_time1 + rodadas_time1
                if gols_time2 > teste1:
                    print(f'{time2} vence a disputa de pênaltis por {gols_time2} a {gols_time1} e avança de fase!')
                    break

    if i == 10:
        break
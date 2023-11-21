# Projeto de um simples jogo no Python

import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    jogadores = input('\nDigite o número de jogadores (2 a 4): ')
    if jogadores.isdigit():
        jogadores = int(jogadores)
        if 2 <= jogadores <= 4:
            break
        else:
            print('\n******************************************')
            print('Número do jogadores tem que ser de 2 a 4 !')
            print('******************************************\n')
    else:
        print('\nInválido, tente de novo !\n')
print('\n******************************************')
print(f'O número de jogadores será: {jogadores}.')
print('******************************************\n')

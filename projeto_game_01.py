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

max_score = 50
player_score = [0 for _ in range(jogadores)]

while max(player_score) < max_score:

    
    for player_idx in range(jogadores):
        print('\nJogador Número', player_idx + 1 'sua rodada iniciou!')
        print('Seu placar é:', player_score[player_idx],'\n'])
        current_score = 0

        while True:
            should_roll = input('Você gostaria de jogar o dado (s) ?')

            if should_roll.lower() != "s":
                break

            value = roll()
            if value == 1:
                print('você tirou 1, seu score zerou!')
                current_score = 0
                break
            else:
                current_score += value
                print('Você tirou:', value)
            
            print('Seu placar é: ', current_score)
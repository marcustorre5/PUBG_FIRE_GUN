#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

from time import sleep
from random import randint
from random import choice


def pubg():
    print('\033[32m PLAYERUNKNOWNS BATTLEGROUNDS FIRE GUN\033[m')

    sleep(1)

    print('caindo de paraquedas')

    sleep(3)

    print('loteando ...')

    sleep(2)

    print('...')
    sleep(1)
    print('!')
    sleep(1)

    metros = randint(0,600)

    print('inimigo a vista, há {} metros'.format(metros))

    sleep(2)

    def gun():
        print('Escolha a sua arma')
        sleep(1)

        ak47 = 1
        m16 = 2
        sks = 3
        kar98 = 4

        ininimgo = randint(1, 4)
        player = int(input('Escolha a arma para atacar o inimigo\n{} AK 47\n{} M 16\n{} SKS\n{} Kar98\n'.format(ak47,m16,sks,kar98)))

        print('o inimigo tem uma {}'.format(ininimgo))
        sleep(1)

        if player == 1 and ininimgo == 2:
            print('Venceu')
        if player == 1 and ininimgo == 1:
            print('A munição acabou')
            sleep(2)
            print('recarregando')
            sleep(1)
            print('...')
            sleep(3)
            print('voltando para lutar')
            sleep(2)
            print('procurando o inimigo ...')
            sleep(2)
            print('inimigo a vista')
            sleep(1)
            lutar = str(input('deseja abrir fogo contra o inimigo ?\n (S) para sim (N) para não\n')).upper()
            viver = 0
            morrer = 1
            batalha = [0, 1]
            endgame = choice(batalha)
            if lutar == 'S':
                print('acabou com o colete do inimigo')
                sleep(1)
                print('inimigo se escondeu')
                sleep(1)
                print('inimigo a vista ')
                print('atirando no inimigo ...')
                if endgame == viver:
                    print('winner')
                if endgame == morrer:
                    print('o jogo acabou para voce amigo ...')
                    sleep(2)
                    print('voltando para o lobby')
                    sleep(2)

        if player ==1 and ininimgo ==3:
            print('perdeu')
        if player ==1 and ininimgo ==4:
            print('pedeu feio')

        if player ==2 and ininimgo ==1:
            print('Perdeu')
        if player ==2 and ininimgo ==2:
            print('a munição acabou')
            sleep(2)
            print('recarregando')
            sleep(1)
            print('...')
            sleep(3)
            print('voltando para lutar')
            sleep(2)
            print('procurando o inimigo ...')
            sleep(2)
            print('inimigo a vista')
            sleep(1)
            lutar = str(input('deseja abrir fogo contra o inimigo ?\n (S) para sim (N) para não\n')).upper()
            viver = 0
            morrer = 1
            batalha = [0, 1]
            endgame = choice(batalha)
            if lutar == 'S':
                print('acabou com o colete do inimigo')
                sleep(1)
                print('inimigo se escondeu')
                sleep(1)
                print('inimigo a vista ')
                print('atirando no inimigo ...')
                if endgame == viver:
                    print('winner')
                if endgame == morrer:
                    print('o jogo acabou para voce amigo ...')
                    sleep(2)
                    print('voltando para o lobby')
                    sleep(2)
        if player ==2 and ininimgo ==3:
            print('perdeu')
        if player ==2 and ininimgo ==4:
            print('pedeu feio')

        if player ==3 and ininimgo ==1:
            print('perdeu')
        if player ==3 and ininimgo ==2:
            print('venceu')
        if player ==3 and ininimgo ==3:
            print('a munição acabou')
            sleep(2)
            print('recarregando')
            sleep(1)
            print('...')
            sleep(3)
            print('voltando para lutar')
            sleep(2)
            print('procurando o inimigo ...')
            sleep(2)
            print('inimigo a vista')
            sleep(1)
            lutar = str(input('deseja abrir fogo contra o inimigo ?\n (S) para sim (N) para não\n')).upper()
            viver = 0
            morrer = 1
            batalha = [0, 1]
            endgame = choice(batalha)
            if lutar == 'S':
                print('tirou o capacetodo inimigo')
                sleep(1)
                print('inimigo se escondeu')
                sleep(1)
                print('inimigo a vista ')
                print('atirando no inimigo ...')
                if endgame == viver:
                    print('winner')
                if endgame == morrer:
                    print('o jogo acabou para voce amigo ...')
                    sleep(2)
                    print('voltando para o lobby')
                    sleep(2)
        if player ==3 and ininimgo ==4:
            print('pedeu')

        if player ==4 and ininimgo ==1:
            print('venceu')
            def gas():
                sleep(2)
                print('o gas está vindo')
                sleep(1)
                print('Corra !')
            gas()
        if player ==4 and ininimgo ==2:
            print('venceu')
            def gas():
                sleep(2)
                print('o gas está vindo')
                sleep(1)
                print('Corra !')
            gas()
        if player ==4 and ininimgo ==3:
            print('perdeu')
        if player ==4 and ininimgo ==4:
            print('a munição acabou')
            sleep(2)
            print('recarregando')
            sleep(1)
            print('...')
            sleep(3)
            print('voltando para lutar')
            sleep(2)
            print('procurando o inimigo ...')
            sleep(2)
            print('inimigo a vista')
            sleep(1)
            lutar = str(input('deseja abrir fogo contra o inimigo ?\n (S) para sim (N) para não\n')).upper()
            viver = 0
            morrer = 1
            batalha = [0, 1]
            endgame = choice(batalha)
            if lutar == 'S':
                print('arrebentou o capaceto do inimigo')
                sleep(1)
                print('inimigo se escondeu')
                sleep(1)
                print('inimigo a vista ')
                print('atirando no inimigo ...')
                if endgame == viver:
                    print('winner')
                if endgame == morrer:
                    print('o jogo acabou para voce amigo ...')
                    sleep(2)
                    print('voltando para o lobby')
                    sleep(2)
    gun()

    def sair():
        sleep(2)
        print('saindo')
    sair()
pubg()

def restart():
    while True:
        quest = int(input('Deseja jogar novamente ?\n0 para recomeçar\n1 para sair\n'))
        if quest ==0:
            pubg()

        if quest ==1:
            print('saindo ...')
            sleep(2)
            break

restart()

def creditos():
    print('=-='*30)
    print('desenvolvido por marcus torres - marcustorre5')
    print('=-='*30)
creditos()


'''
TRABALHO FINAL - PYTHON3 - 2018.1
Gabriel Freire do Vale, 418788
Julia Hellen Rocha Vieira, 417425
'''

from os import system
system('clear')

from logic import *
import board

MATRIZ = [[0 for i in range(9)] for i in range(9)]

addTips('settings.txt', MATRIZ)
tips = getTips('settings.txt')
print(board.build(MATRIZ))
print(tips)

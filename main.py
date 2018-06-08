from os import system
system('clear')
from styles import *
from logic import *
import board

MATRIZ = [[0 for i in range(9)] for i in range(9)]

addTips('settings', MATRIZ)
#print(buildBoard(MATRIZ), end="\r")
cores = getColors()
print(board.build(MATRIZ))


'''
TRABALHO FINAL - PYTHON3 - 2018.1
Gabriel Freire do Vale, 418788
Julia Hellen Rocha Vieira, 417425
'''

import util
import game

util.clearConsole()
welcome = '================ SUDOKU ================\n'
welcome += 'Bem vindo! Entre o tipo de jogo:\n'
welcome += '1 - Modo interativo\n'
welcome += '2 - Modo batch'
print(welcome)
game_type = int(input())
if game_type == 1:
    game.interactive()
elif game_type == 2:
    print('Entrando no modo batch...')
    game.batch()
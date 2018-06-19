import util
import board
from logic import *


def interactive():
  '''Game interactive mode.

  Runs the full, user interactive Sudoku game,
  asking for the player input at each turn.
  '''
  matrix = [[0 for j in range(9)] for i in range(9)]
  addTips('config.txt', matrix)
  tips = getTips('config.txt')
  if validGame(matrix):
    i = 0
    msg = util.ok('Entre com sua jogada:')
    lastError = [0, 0]
    while i < (81-len(tips)):
      util.clearConsole()
      print(board.build(matrix, tips))
      print(msg)
      r, c = lastError
      if matrix[r][c] < 0:
        matrix[r][c] = 0
      user_input = formatInput(input())
      row, col, num = map(int, user_input.split(':'))
      inTips = False
      for t in tips:
        if user_input[:3] == t[:3]:
          inTips = True
      if inTips:
        msg = util.error('As dicas nao podem ser sobrescritas.')
      elif validNum(matrix, num, row, col):
        matrix[row][col] = num
        msg = util.ok('Entre com sua jogada:')
        i += 1
      else:
        if row < 9 and col >= 0 and 10 > num > 0:
          matrix[row][col] = -num
          lastError = [row, col]
        msg = util.error('Jogada invalida. Por favor, jogue novamente.')
    print(board.build(matrix, tips))
    print(util.ok('Parabens, voce concluiu o jogo!'))
    e = input('    Jogar novamente? (Y/N)\n')
    if e.lower() == 'y' or e == '':
      interactive()
  else:
    print(board.build(matrix, tips))
    print(util.error('O arquivo de configuracoes possui dicas invalidas.'))


def batch():
  '''Modo batch do jogo.'''
  matrix = [[0 for j in range(9)] for i in range(9)]
  addTips('config.txt', matrix)
  tips = getTips('config.txt')
  if validGame(matrix):
      addPlays('jogadas.txt', matrix)
      plays = getPlays('jogadas.txt')
  else:
      print('O arquivo de configuracoes possui dicas invalidas.')


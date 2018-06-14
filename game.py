import util
import board
from logic import *


def formatInput() -> str:
  '''Formats the user input to be used in the game.

  Takes the user input and formats it in a way that
  is easier to be added to the game matrix.

  Returns:
    A string with the formated input with the format 
    'row:column:number'. For example:
    'A , 3:1' becomes '2:0:1'
  '''
  columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
  user_input = input()
  result = ''
  for c in user_input:
    if c == ',' or c == ':':
      c = ' '
    result += c
  if len(result) > 4:
    col, row, num = result.split()
  else:
    col, row = result.replace('D', '').split()
    num = 0
  if col.lower() in columns:
    col = columns.index(col.lower())
  else:
    col = -1
  row = int(row)-1
  num = int(num)
  return '%d:%d:%d' % (row, col, num)


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
      print(board.build(matrix, tips))
      print(msg)
      r, c = lastError
      if matrix[r][c] < 0:
        matrix[r][c] = 0
      user_input = formatInput()
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
        if row < 9 and col > 0 and num < 10:
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


def batch(matrix):
  '''Modo batch do jogo.'''
  print('MODO BATCH')

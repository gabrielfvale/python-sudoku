import util
import board
from logic import *


def formatInput():
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
    col = 10
  row = int(row)-1
  num = int(num)
  return '%d:%d:%d' % (row, col, num)


def interactive():
  '''Modo interativo do jogo.'''
  matrix = [[0 for j in range(9)] for i in range(9)]
  addTips('config.txt', matrix)
  tips = getTips('config.txt')
  if validGame(matrix):
    i = 0
    msg = util.ok('Entre com sua jogada:')
    lastError = [0, 0]
    while i < (81-len(tips)):
      print(board.build(matrix))
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
      else:
        if row < 9 and col < 10 and num < 10:
          matrix[row][col] = -num
          lastError = [row, col]
        msg = util.error('Jogada invalida. Por favor, jogue novamente.')
      i += 1
    print('')
  else:
    print(board.build(matrix))
    print(util.error('O arquivo de configuracoes possui dicas invalidas.'))


def batch(matrix):
  '''Modo batch do jogo.'''
  print('MODO BATCH')

import util
import board
from logic import *


def formatInput():
  colunas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
  entrada = input()
  formatada = ''
  for c in entrada:
    if c == ',' or c == ':':
      c = ' '
    formatada += c
  if len(formatada) > 4:
    col, row, num = formatada.split()
  else:
    col, row = formatada.replace('D', '').split()
    num = 0
  if col.lower() in colunas:
    col = colunas.index(col.lower())
  else:
    col = 10
  row = int(row)-1
  num = int(num)
  return [row, col, num]


def interactive():
  '''Modo interativo do jogo.'''
  MATRIZ = [[0 for j in range(9)] for i in range(9)]
  addTips('settings.txt', MATRIZ)
  tips = getTips('settings.txt')
  if validGame(MATRIZ):
    i = 0
    msg = util.ok('Entre com sua jogada:')
    lastError = [0, 0]
    while i < (81-len(tips)):
      print(board.build(MATRIZ))
      print(msg)
      r, c = lastError
      if MATRIZ[r][c] < 0:
        MATRIZ[r][c] = 0
      row, col, num = formatInput()
      if validNum(MATRIZ, num, row, col):
        MATRIZ[row][col] = num
        msg = util.ok('Entre com sua jogada:')
      else:
        if col < 10:
          MATRIZ[row][col] = -num
          lastError = [row, col]
        msg = util.error('Jogada invalida. Por favor, jogue novamente.')
      i += 1
    print('')
  else:
    print(board.build(MATRIZ))
    print(util.error('O arquivo de configuracoes possui dicas invalidas.'))


def batch(MATRIZ):
  '''Modo batch do jogo.'''
  print('MODO BATCH')

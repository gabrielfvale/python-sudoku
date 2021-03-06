import util
import board
from logic import *


def interactive():
  '''Game interactive mode.

  Runs the full, user interactive Sudoku game,
  asking for the player input at each turn.
  '''
  matrix = [[0 for j in range(9)] for i in range(9)]
  tips = getFromFile('config.txt')
  addTips(tips, matrix)
  if validGame(matrix):
    i = 0
    msg = util.ok('Entre sua jogada:')
    errorcleanup = [0, 0, 0]
    while i < (81-len(tips)):
      util.clearConsole()
      print(board.build(matrix, tips))
      print(msg)
      r, c, n = errorcleanup
      if matrix[r][c] < 0:
        matrix[r][c] = n
      user_input = formatInput(input())
      row, col, num = map(int, user_input.split(':'))
      inTips = False
      for t in tips:
        if user_input[:3] == t[:3]:
          inTips = True
      if inTips:
        msg = util.error('As dicas nao podem ser sobrescritas.')
      elif validNum(matrix, num, row, col):
        msg = util.ok('Entre sua jogada:')
        if matrix[row][col] == 0 and num != 0:
          i += 1
        if matrix[row][col] != 0 and num == 0:
          i -= 1
        matrix[row][col] = num
      else:
        if row < 9 and col >= 0 and 10 > num > 0:
          errorcleanup = row, col, matrix[row][col]
          matrix[row][col] = -num
        msg = util.error('Jogada invalida. Por favor, jogue novamente.')
    util.clearConsole()
    print(board.build(matrix, tips))
    print(util.ok('Parabens, voce concluiu o jogo!'))
    e = input('    Jogar novamente? (Y/n)\n')
    if e.lower() == 'y' or e == '':
      interactive()
  else:
    util.clearConsole()
    print(board.build(matrix, tips))
    print(util.error('Arquivo de configuracoes invalido.'))


def batch():
  '''Game batch mode.

  Reads two files, one containing the tips and the other
  containing the plays. Each turn is tested, printing if
  it is valid or not. At the end, shows a message if the
  game was completed.
  '''
  matrix = [[0 for j in range(9)] for i in range(9)]
  tips = getFromFile('config.txt')
  addTips(tips, matrix)
  plays = getFromFile('plays.txt')
  columns = columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
  if validGame(matrix):
    total = 0
    for turn in plays:
      inTips = False
      for t in tips:
        if turn[:3] == t[:3]:
          inTips = True
      row, col, num = map(int, turn.split(':'))
      if inTips:
        print('A jogada (%s,%d) = %d eh invalida!' % (columns[col].upper(), row+1, num))
      elif validNum(matrix, num, row, col):
        matrix[row][col] = num
        total += 1
        print('A jogada (%s,%d) = %d eh valida!' % (columns[col].upper(), row+1, num))
      else:
        print('A jogada (%s,%d) = %d eh invalida!' % (columns[col].upper(), row+1, num))
    if len(tips)+total == 81:
      print('A grade foi preenchida com sucesso!')
    else:
      print('A grade nao foi preenchida!')
  else:
      print('Arquivo de configuracoes invalido.')

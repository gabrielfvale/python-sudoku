from os import system
from util import getColors


def build(matrix):
	'''Constroi o tabuleiro do Sudoku, limpando a instancia anterior.'''
	system('clear')
	colors = getColors()
	spacer1 = '  ++---+---+---++---+---+---++---+---+---++  \n'
	spacer2 = '  ++===+===+===++===+===+===++===+===+===++  \n'
	columns = '     A   B   C    D   E   F    G   H   I     \n'
	board = colors['PB'] + '\n' + columns + spacer1
	for i in range(9):
		line = ' {}|'.format(i+1)
		for j in range(9):
			num = matrix[i][j]
			if num == 0:
				num = ' '
			elif num < 0:
				num = colors['ERRB'] + str(-num)
			if j % 3 == 0:
				line += '| {}{}{} |'.format(colors['NUM'], num, colors['PB'])
			else:
				line += '{} {} {}|'.format(colors['NUM'], num, colors['PB'])
		line += '|{} \n'.format(i+1)
		board += line
		if i == 2 or i == 5:
			board += spacer2
		else:
			board += spacer1
	board += columns + colors['END'] + '\r'
	return board

from os import system
from styles import *

def build(matrix):
	'''Constroi o tabuleiro do Sudoku, limpando a instancia anterior.'''
	system('clear')
	CORES = getColors()
	SEPARADOR1 = '  ++---+---+---++---+---+---++---+---+---++  \n'
	SEPARADOR2 = '  ++===+===+===++===+===+===++===+===+===++  \n'
	LETRAS = '     A   B   C    D   E   F    G   H   I     \n'
	TABULEIRO = CORES['PB'] + '\n' + LETRAS + SEPARADOR1
	for i in range(9):
		linha = ' {}|'.format(i+1)
		for j in range(9):
			num = matrix[i][j]
			if num == 0:
				num = ' '
			elif num < 0:
				num = CORES['ERRB'] + str(-num)
			if j % 3 == 0:
				linha += '| {}{}{} |'.format(CORES['NUM'], num, CORES['PB'])
			else:
				linha += '{} {} {}|'.format(CORES['NUM'], num, CORES['PB'])
		linha += '|{} \n'.format(i+1)
		TABULEIRO += linha
		if i == 2 or i == 5:
			TABULEIRO += SEPARADOR2
		else:
			TABULEIRO += SEPARADOR1
	TABULEIRO += LETRAS + CORES['END'] + '\r'
	return TABULEIRO

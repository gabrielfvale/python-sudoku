from os import system
system('clear')


MATRIZ = [[' ' for i in range(9)] for i in range(9)]


def getColors():
	colors = {
		'PB': '\033[0;30;47m',
		'TIP': '\033[0;34;47m',
		'NUM': '\033[0;34;47m',
		'END': '\033[0m'
	}
	return colors


def addTips(filename, matrix):
	'''Abre o arquivo de configuracoes do Sudoku e insere as pistas.'''
	colunas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
	colors = getColors()
	with open(filename + '.txt', 'r') as settings_obj:
		for line in settings_obj:
			line = line.strip()
			row = int(line[2:3])-1
			col = colunas.index(line[:1].lower())
			num = int(line[-1])
			matrix[row][col] = num


def buildBoard(matrix):
	'''Constroi o tabuleiro do Sudoku, limpando a instancia anterior.'''
	from os import system
	system('clear')

	CORES = getColors()
	SEPARADOR1 = '  ++---+---+---++---+---+---++---+---+---++  \n'
	SEPARADOR2 = '  ++===+===+===++===+===+===++===+===+===++  \n'
	LETRAS = '     A   B   C    D   E   F    G   H   I     \n'
	TABULEIRO = CORES['PB'] + '\n' + LETRAS + SEPARADOR1

	for i in range(9):
		linha = ' {}|'.format(i+1)
		for j in range(9):
			if j % 3 == 0:
				linha += '| {}{}{} |'.format(CORES['NUM'], matrix[i][j], CORES['PB'])
			else:
				linha += '{} {} {}|'.format(CORES['NUM'], matrix[i][j], CORES['PB'])
		linha += '|{} \n'.format(i+1)
		TABULEIRO += linha
		if i == 2 or i == 5:
			TABULEIRO += SEPARADOR2
		else:
			TABULEIRO += SEPARADOR1
	TABULEIRO += LETRAS + CORES['END']

	return TABULEIRO

addTips('settings', MATRIZ)
print(buildBoard(MATRIZ))
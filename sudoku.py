from os import system
system('clear')


MATRIZ = [[0 for i in range(9)] for i in range(9)]


def getColors():
	colors = {
		'PB': '\033[0;30;47m',
		'TIP': '\033[0;34;47m',
		'NUM': '\033[0;34;47m',
		'ERR': '\033[0;31;47m',
		'END': '\033[0m'
	}
	return colors


def isNumValid(matrix, num, row, col):
	num = abs(num)
	inicio = 0
	fim = col
	starts = [0, 3, 6]
	mids = [1, 4, 7]
	ends = [2, 5, 8]
	if fim < 3:
		fim = 3
	elif fim >= 3 and fim < 6:
		inicio = 3
		fim = 6
	elif fim >= 6 and fim < 10:
		inicio = 6
		fim = 9
	section = 9*[0]
	if row in starts:
		section = matrix[row][inicio:fim]
		section += matrix[row+1][inicio:fim]
		section += matrix[row+2][inicio:fim]
	if row in mids:
		section = matrix[row-1][inicio:fim]
		section += matrix[row][inicio:fim]
		section += matrix[row+1][inicio:fim]
	if row in ends:
		section = matrix[row-2][inicio:fim]
		section += matrix[row-1][inicio:fim]
		section += matrix[row][inicio:fim]
	cont = 0
	while cont < 9:
		if matrix[row][cont] == num or matrix[cont][col] == num or section[cont] == num:
			cont = 10
		cont += 1
	if cont > 9:
		return False
	else:
		return True


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
			if isNumValid(matrix, num, row, col):
				matrix[row][col] = num
			else:
				matrix[row][col] = -num


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
			num = matrix[i][j]
			if num == 0:
				num = ' '
			elif num < 0:
				num = CORES['ERR'] + str(-num)
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
	TABULEIRO += LETRAS + CORES['END']
	return TABULEIRO


addTips('settings', MATRIZ)
print(buildBoard(MATRIZ))
status = 'OK'
for i in range(9):
	for j in range(9):
		if MATRIZ[i][j] < 0:
			status = 'ERRO'
print(status)

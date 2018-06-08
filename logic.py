def isNumValid(matrix, num, row, col):
	'''
	Checa se ha numeros repetidos na mesma linha,
	coluna ou secao da matriz do jogo.
	'''
	num = abs(num)
	inicio = 0
	fim = col
	section = 9*[0]
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
	# Constroi a secao
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
	# Por fim, checa todas as 3 condicoes de validacao
	while cont < 9:
		if matrix[row][cont] == num or matrix[cont][col] == num or section[cont] == num:
			cont = 10
		cont += 1
	if cont > 9:
		return False
	else:
		return True


def addTips(filename, matrix):
	'''Insere as pistas na matriz do Sudoku.'''
	tips = getTips(filename)
	for num in tips:
		row, col, num = map(int, num.split(':'))
		if isNumValid(matrix, num, row, col):
			matrix[row][col] = num
		else:
			matrix[row][col] = -num


def getTips(filename):
	'''
	Abre o arquivo de configuracoes, retornando 
	os valores em uma lista melhor formatada.
	'''
	tips = []
	colunas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
	with open(filename, 'r') as settings_obj:
		for line in settings_obj:
			line = line.strip()
			row = int(line[2:3])-1
			col = colunas.index(line[:1].lower())
			num = int(line[-1])
			tips.append('{}:{}:{}'.format(row, col, num))
	return tips


def catchError(matrix):
	'''Checa se há algum erro na matriz do jogo.'''
	error = False
	for i in range(9):
		for j in range(9):
			if matrix[i][j] < 0:
				error = True
	return error

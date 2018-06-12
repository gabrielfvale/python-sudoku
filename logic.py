def validNum(matrix, num, row, col):
	'''
	Checa se ha numeros repetidos na mesma linha,
	coluna ou secao da matriz do jogo.
	'''
	start = 0
	end = col
	if row > 8 or col > 9 or num > 9:
		return False
	section = 9*[0]
	starts = [0, 3, 6]
	mids = [1, 4, 7]
	ends = [2, 5, 8]
	if end < 3:
		end = 3
	elif end >= 3 and end < 6:
		start = 3
		end = 6
	elif end >= 6 and end < 10:
		start = 6
		end = 9
	# Constroi a secao
	if row in starts:
		section = matrix[row][start:end]
		section += matrix[row+1][start:end]
		section += matrix[row+2][start:end]
	if row in mids:
		section = matrix[row-1][start:end]
		section += matrix[row][start:end]
		section += matrix[row+1][start:end]
	if row in ends:
		section = matrix[row-2][start:end]
		section += matrix[row-1][start:end]
		section += matrix[row][start:end]
	cont = 0
	# Por fim, checa todas as 3 condicoes de validacao
	if num != 0:
		num = abs(num)
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
		if validNum(matrix, num, row, col):
			matrix[row][col] = num
		else:
			matrix[row][col] = -num


def getTips(filename):
	'''
	Abre o arquivo de configuracoes, retornando 
	os valores em uma lista melhor formatada.
	'''
	tips = []
	columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
	with open(filename, 'r') as settings_obj:
		for line in settings_obj:
			line = line.strip()
			row = int(line[2:3])-1
			col = columns.index(line[:1].lower())
			num = int(line[-1])
			tips.append('%d:%d:%d' % (row, col, num))
	return tips


def validGame(matrix):
	'''Dada a matriz, checa a validade do jogo.'''
	valid = True
	i = 0
	j = 0
	for i in range(9):
		for j in range(9):
			if matrix[i][j] < 0:
				valid = False
	return valid

def validNum(matrix: list, num: int, row: int, col: int) -> bool:
	'''Validates a number.

	Checks if there are non-unique numbers in the same line,
	column or section of the game matrix.

	Args:
		matrix: A 9x9 matrix of numbers for Sudoku.
		num: The number to be compared.
		row: The row of the matrix that the number is in.
		col: The column of the matrix that the number is in.

	Returns:
		A bool holding the validity of the number.
	'''
	if row > 8 or col < 0 or num > 9:
		return False
	start = 0
	section = []
	if col >= 3 and col < 6:
		start = 3
	elif col >= 6 and col < 10:
		start = 6
	end = start + 3
	# Section builder, using a constant
	const = row
	if row > 2 and row < 6:
		const = row - 3
	elif row >= 6:
		const = row - 6
	for k in range(3):
		section += matrix[row-const+k][start:end]
	# Checks all the conditions
	cont = 0
	if num != 0:
		num = abs(num)
		while cont < 9:
			if num in [matrix[row][cont], matrix[cont][col], section[cont]]:
				cont = 10
			cont += 1
	if cont > 9:
		return False
	else:
		return True


def addTips(filename: str, matrix: list):
	'''Inserts the tips in the matrix.

	Opens the configuration file and inserts every
	tip onto the Sudoku matrix.

	Args:
		filename: The file to be opened.
		matrix: The matrix that is going to be changed.
	'''
	tips = getTips(filename)
	for num in tips:
		row, col, num = map(int, num.split(':'))
		if validNum(matrix, num, row, col):
			matrix[row][col] = num
		else:
			matrix[row][col] = -num


def getTips(filename: str) -> list:
	'''Retrieves game tips from a file.

	Opens a configuration file containing the game tips,
	and returns them with an easy to use format.

	Args:
		filename: The file to be opened.
	
	Returns:
		A list of tips retrieved from the file. For example:
		['2:0:3', '0:5:3', '7:3:7']
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


def validGame(matrix: list) -> bool:
	'''Checks if a game is valid.

	Given the game matrix, checks if there are any
	numbers lower than zero, condition that makes
	the game invalid.

	Args:
		matrix: The game matrix to be tested.
	
	Returns:
		A bool that indicates if the game is valid or not.
	'''
	valid = True
	tips = 0
	for i in range(9):
		for j in range(9):
			if matrix[i][j] != 0:
				tips += 1
			if matrix[i][j] < 0:
				valid = False
	if tips < 1 or tips > 80:
		valid = False
	return valid

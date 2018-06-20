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
	if row > 8 or col < 0 or num < 0 or num > 9:
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


def addTips(tips: list, matrix: list):
	'''Inserts the tips in the matrix.

	Takes the list of tips and adds them onto the
	Sudoku matrix.

	Args:
		filename: The file to be opened.
		matrix: The matrix that is going to be changed.
	'''
	for num in tips:
		row, col, num = map(int, num.split(':'))
		if validNum(matrix, num, row, col):
			matrix[row][col] = num
		else:
			matrix[row][col] = -num



def formatInput(uinput: str) -> str:
	'''Formats the input to be used in the game.

	Takes the input and formats it in a way that
	is easier to be added to the game matrix.

	Args:
		uinput: The input that is going to be formated.

	Returns:
		A string with the format 'row:column:number'.
		For example, 'A , 3:1' becomes '2:0:1'
	'''
	columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
	result = ''
	for char in uinput:
		if char == ',' or char == ':':
			char = ' '
		result += char
	if len(result) > 4:
		col, row, num = result.split()
	else:
		col, row = result.replace('D', '').split()
		num = 0
	if col.lower() in columns:
		col = columns.index(col.lower())
	else:
		col = -1
	row = int(row)-1
	num = int(num)
	return '%d:%d:%d' % (row, col, num)


def getFromFile(filename: str) -> list:
	'''Retrieves game tips/plays from a file.

	Opens a file containing the game tips/plays,
	and returns them with an easy to use format.

	Args:
		filename: The file to be opened.
	
	Returns:
		A list retrieved from the file. For example:
		['2:0:3', '0:5:3', '7:3:7']
	'''
	formatted_list = []
	with open(filename, 'r') as settings_obj:
		for line in settings_obj:
			line = line.strip()
			formatted_list.append(formatInput(line))
	return formatted_list


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

from util import getColors


def build(matrix: list, tips: list) -> str:
	'''Builds the game board.

	Retrives the game matrix and builds a
	board that is easy for the end user to
	understand.

	Args:
		matrix: The 9x9 game matrix.
		tips: The list of tips on the board.
	
	Returns:
		A string containing the whole board.
	'''
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
			num_pos = '%d:%d' % (i, j)
			for t in tips:
				if num_pos == t[:3]:
					num = colors['TIP'] + str(num)
			if j % 3 == 0:
				line += '| %s%s%s |' % (colors['NUM'], num, colors['PB'])
			else:
				line += '%s %s %s|' % (colors['NUM'], num, colors['PB'])
		line += '|{} \n'.format(i+1)
		board += line
		if i == 2 or i == 5:
			board += spacer2
		else:
			board += spacer1
	board += columns + colors['END'] + '\r'
	return board

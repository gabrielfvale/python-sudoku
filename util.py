def getColors() -> dict:
	'''Retrives the game colors.

	Returns:
		A dict with the list of the colors
		used in the game.
	'''
	colors = {
		'PB': '\033[0;30;47m',
		'TIP': '\033[0;34;47m',
		'NUM': '\033[0;30;47m',
		'OK': '\033[0;30;42m',
		'ERR': '\033[0;37;41m',
		'ERRB': '\033[0;31;47m',
		'END': '\033[0m'
	}
	return colors


def error(msg: str) -> str:
	'''Adds ERROR status to a message.
	
	Args:
		msg: The message to be formated.
	
	Returns:
		A string with the status indicator.
	'''
	colors = getColors()
	result = colors['ERR'] + '   ' + colors['END'] + ' ' + msg
	return result


def ok(msg: str) -> str:
	'''Adds OK status to a message.

	Args:
		msg: The message to be formated.
	
	Returns:
		A string with the status indicator.
	'''
	colors = getColors()
	result = colors['OK'] + '   ' + colors['END'] + ' ' + msg
	return result

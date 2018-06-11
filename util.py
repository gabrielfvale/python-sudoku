def getColors():
	colors = {
		'PB': '\033[0;30;47m',
		'TIP': '\033[0;34;47m',
		'NUM': '\033[0;34;47m',
		'OK': '\033[0;30;42m',
		'ERR': '\033[0;37;41m',
		'ERRB': '\033[0;31;47m',
		'END': '\033[0m'
	}
	return colors


def error(msg):
  colors = getColors()
  result = colors['ERR'] + '   ' + colors['END'] + ' ' + msg
  return result


def ok(msg=''):
  colors = getColors()
  result = colors['OK'] + '   ' + colors['END'] + ' ' + msg
  return result

# helper functions are placed here, which are used in oder modules.
def load_numbers(file_name: str) -> list:
	"""
	Loads a list of integers from a file and returns a list
	containing them.
	:param file_name: path to file to load
	:return: List of numbers contained in file_name
	"""
	numbers = list()
	with open(file_name) as f:
		for line in f:
			numbers.append(int(line))
	return numbers

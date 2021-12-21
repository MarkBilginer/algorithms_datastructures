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


def verify_sorted_recursive(l: list) -> bool:
	"""
	Verify if the list is sorted.
	:param l: list to check whether it is sorted.
	:return: true if sorted, else false.
	"""
	n = len(l)
	if n == 0 or n == 1:
		return True

	# for i in range(1, n):
	# 	if l[i - 1] > l[i]:
	# 		return False
	# return True
	return l[0] < l[1] and verify_sorted_recursive(l[1:])
import time
from src.helpful_functions.load import load_numbers, verify_sorted_recursive


def selection_sort(values: list) -> list:
	"""
	An inefficient, slow, sorting algorithm. Better than bogo_sort.
	Takes O(n^2) time.
	:param values:
	:return:
	"""
	sorted_sublist = list()
	minimum = int()
	# print("%-25s %-25s" % (values, sorted_sublist))
	for i in range(len(values)):
		index_to_move = index_of_min(values)  # O(n) time
		sorted_sublist.append(values.pop(index_to_move))  # O(n) time
		# print("%-25s %-25s" % (values, sorted_sublist))
	return sorted_sublist


def index_of_min(values: list) -> int:
	"""
	Find the minimum value and returns its index.
	Takes O(n) time.
	:param values: list containing numbers.
	:return: index of lowest number
	"""
	if len(values) == 0:
		return None

	min_index = 0
	for i in range(len(values)):
		if values[min_index] > values[i]:
			min_index = i

	return min_index


def main():
	# numbers = load_numbers(sys.argv[1])
	numbers = load_numbers("../../resources/numbers_100.txt")

	print(numbers)
	print("Size of list is: %d" % len(numbers))

	t1_start = time.perf_counter()
	sorted_list = selection_sort(numbers)
	t1_stop = time.perf_counter()
	print(sorted_list)
	print(f"Time elapsed: {t1_stop - t1_start}")
	# todo maybe implement a better version of verify_sorted, which doesnt use recursion
	# you need to disable this line if list is too long.
	print(f"Is sorted? {verify_sorted_recursive(sorted_list)}")


if __name__ == "__main__":
	main()

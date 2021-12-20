import typing
import time
_length_test_list = 1000000


def linear_search(l: list, target: int) -> typing.Union[int, float, str, None]:
	"""
	Returns the index position of the target if found, else returns None
	:param l: python list
	:param target: numerical value
	:return: index position if target found else None
	"""
	# python keeps track of len(list) that's why its constant, else linear
	# the for loop goes through all elements, worst case is O(n)
	for i in range(0, len(l)):
		print(i)
		if target == l[i]:
			return i
	return None


def verify(index: int) -> None:
	if index is not None:
		print("Target found at index: ", index)
	else:
		print("Target not found in the list.")


def main():
	numbers = [i for i in range(0, _length_test_list)]
	t1_start = time.perf_counter()
	result = linear_search(numbers, _length_test_list)
	t1_stop = time.perf_counter()
	print("Elapsed Time: " + str(t1_stop-t1_start))
	verify(result)


if __name__ == '__main__':
	main()

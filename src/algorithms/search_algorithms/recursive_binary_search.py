import typing
import time

_length_test_list = 1000000


def recursive_binary_search(l: list, target: int) -> typing.Union[
	int, float, str, None]:
	if len(l) == 0:  # empty list is also the stopping condition
		return False
	else:
		# floor division is necessary, ceiling results in index error
		mid = len(l) // 2
		if target == l[mid]:  # second stopping condition.
			return True
		else:
			if target > l[mid]:
				return recursive_binary_search(l[mid + 1:], target)
			else:
				return recursive_binary_search(l[:mid], target)


def verify(index: int) -> None:
	if index is not None:
		print("Target found at index: ", index)
	else:
		print("Target not found in the list.")


def main():
	numbers = [i for i in range(0, _length_test_list)]
	t1_start = time.perf_counter()
	result = recursive_binary_search(numbers, 499999)
	t1_stop = time.perf_counter()
	print("Elapsed Time: " + str(t1_stop - t1_start))
	verify(result)


if __name__ == '__main__':
	main()


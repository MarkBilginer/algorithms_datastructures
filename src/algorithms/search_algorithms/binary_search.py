import typing
import time
import math

_length_test_list = 1000000


def binary_search(l: list, target: int) -> typing.Union[int, float, str, None]:
	# constant time both assignments
	first = 0
	last = len(l) - 1

	# the while group makes the algorithm have a logn complexity
	while first <= last: # evaluates to False when list length is 0
		mid = math.ceil((first + last) / 2)
		print(f"first:{first}\nmid:{mid}\nlast:{last}")
		# best case scenario also condition for further division
		if target == l[mid]:
			return mid
		# continue splitting the list
		elif target < l[mid]:
			last = mid - 1
		elif target > l[mid]:
			first = mid + 1
	return None


def verify(index: int) -> None:
	if index is not None:
		print("Target found at index: ", index)
	else:
		print("Target not found in the list.")


def main():
	numbers = [i for i in range(0, _length_test_list)]
	t1_start = time.perf_counter()
	result = binary_search(numbers, 499999)
	t1_stop = time.perf_counter()
	print("Elapsed Time: " + str(t1_stop - t1_start))
	verify(result)


if __name__ == '__main__':
	main()

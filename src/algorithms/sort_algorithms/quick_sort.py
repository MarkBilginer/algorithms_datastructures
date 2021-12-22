import time
from src.helpful_functions.load import load_numbers, verify_sorted_recursive


def quick_sort(values: list) -> list:
	# base case
	if len(values) <= 1:
		return values

	# split values into less than pivot and greater than pivot sublists
	less_half, greater_half = pivot_comparison_split(values)

	less_sorted = quick_sort(less_half)
	greater_sorted = quick_sort(greater_half)

	return less_sorted + greater_sorted


def pivot_comparison_split(values: list) -> tuple[list, list]:
	pivot = values[0]
	less_than_pivot = list()
	greater_than_pivot = list()

	for value in values[1:]:  # O(n) time
		if value <= pivot:
			less_than_pivot.append(value)  # amortized O(1) time
		else:
			greater_than_pivot.append(value)
	# adding the pivot to less than or equal pivot list.
	less_than_pivot.append(pivot)
	return less_than_pivot, greater_than_pivot


def main():
	# numbers = load_numbers(sys.argv[1])
	numbers = load_numbers("../../resources/numbers_10k.txt")

	print(numbers)
	print("Size of list is: %d" % len(numbers))

	t1_start = time.perf_counter()
	sorted_list = quick_sort(numbers)
	t1_stop = time.perf_counter()
	print(sorted_list)
	print(f"Time elapsed: {t1_stop - t1_start}")
	# todo maybe implement a better version of verify_sorted, which doesnt use
	#  recursion
	# you need to disable this line if list is too long.
	# print(f"Is sorted? {verify_sorted_recursive(sorted_list)}")


if __name__ == "__main__":
	main()

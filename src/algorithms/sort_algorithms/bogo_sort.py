import random
import sys
import time
from src.helpful_functions.load import load_numbers


def is_sorted(values: list) -> bool:
	"""
	Checks whether the list is sorted in ascending order.
	Takes O(n) time to run.
	:param values: a list containing numerbers
	:return: true if sorted else false
	"""
	for index in range(len(values) - 1):
		if values[index] > values[index + 1]:
			return False
	return True


def bogo_sort(values: list) -> list:
	"""
	Very inefficient sorting algorithms, educational purposes only.
	There are two ways to implement bogosort: deterministic and randomized.
	This function impements the randomized version.
	records the attempts made.

	Takes O(infinity or unbounded) time. Finds the result with pure luck,
	for a very long list, it might never find a solution.
	Takes O((n+1)!) time for deterministic model.
	Does not get closer to the solution each step.

	O(1) space complexity
	:param values: list containing numbers
	:return: sorted list
	"""
	attempts = 0
	while not is_sorted(values):
		print(f"Attempt: {attempts}")
		random.shuffle(values)
		attempts += 1
	print(f"Bogo sort took {attempts} attempt/s, to solve the problem.")
	return values


def main():
	# numbers = load_numbers(sys.argv[1])
	numbers = load_numbers("../../resources/numbers_10.txt")

	print(numbers)
	print("Size of list is: %d" % len(numbers))

	t1_start = time.perf_counter()
	sorted = bogo_sort(numbers)
	t1_stop = time.perf_counter()
	print(sorted)
	print(f"Time elapsed: {t1_stop - t1_start}")


if __name__ == "__main__":
	main()

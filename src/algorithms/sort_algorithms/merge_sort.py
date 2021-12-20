import random


def merge_sort(l: list) -> list:
	"""
	Sorts a list in ascending order.

	Divide: Find the midpoint of the list and divide into sublists
	Conquer: Recursively sort the sublists created in previous step
	Combine: Merge the sorted sublists created in previous

	O(nlogn) time complexity.
	O(n) space complexity.
	in our implementation with slice O(knlogn)
	n number of merge steps multiplied by logn number of splits.
	:param l: python list
	:return: a new sorted list
	"""
	if len(l) <= 1:
		return l
	left_half, right_half = split_sliced(l)
	left = merge_sort(left_half)
	right = merge_sort(right_half)

	return merge(left, right)


def split(l: list) -> tuple[list, list]:
	pass


def split_sliced(l: list) -> tuple[list, list]:
	"""
	Divide the unsorted list at midpoint into sublists.
	Returns two sublists - left and right.

	Takes overall O(log n) time. (in our implementation with slice:
	O(k log n)
	python subscript split, slice doesnt take constant time,
	takes O(k) time where k is the split size.
	:param l: list (array) to be split
	:return: tuple(sublist, sublist)
	"""
	mid = len(l) // 2

	left = l[:mid]
	right = l[mid:]

	return left, right


def merge(left: list, right: list) -> list:
	"""
	Merges two lists(arrays), sorting them in the process.
	Returns a new merged list.

	list of size n, needs n number of merge operations to come from one
	element list to the complete list.
	O(n) time complexity.
	:param left:
	:param right:
	:return:
	"""
	result = list()
	i = 0  # for left list
	j = 0  # for right list

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
		j += 1

	return result


def verify_sorted(l: list) -> bool:
	n = len(l)
	if n == 0 or n == 1:
		return True

	# for i in range(1, n):
	# 	if l[i - 1] > l[i]:
	# 		return False
	# return True
	return l[0] < l[1] and verify_sorted(l[1:])


if __name__ == "__main__":
	l = [i for i in range(50)]
	random.shuffle(l)
	print(l)
	print(verify_sorted(l))
	l = merge_sort(l)
	print(verify_sorted(l))

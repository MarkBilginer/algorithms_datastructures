import random
from src.data_structures.linked_list import LinkedList


def merge_sort(linked_list: LinkedList) -> LinkedList:
	"""
	Sorts a linked list in ascending order.
	-Recursively divide the linked list into sublists containing a single node.
	-Repeatedly merge the sublists to produce sorted sublists until one
	remains.
	Takes O(knlogn) time.
	:param linked_list: a linked-list
	:return: a sorted linked list.
	"""
	if linked_list.size() == 1:
		return linked_list
	elif linked_list.head is None:
		return linked_list

	left_half, right_half = split(linked_list)
	left = merge_sort(left_half)
	right = merge_sort(right_half)

	return merge(left, right)


def split(linked_list: LinkedList) -> tuple[LinkedList, LinkedList]:
	"""
	Divide the unsorted linked-list at midpoint into sublinked-lists.
	Takes O(k logn) time.
	:param linked_list:
	:return: tuple containing both sub linked-lists
	"""
	if linked_list is None or linked_list.head is None:
		left_half = linked_list
		right_half = None
		return left_half, right_half
	else:
		size = linked_list.size()
		mid_index = (size // 2) - 1
		# # linear time, linked list traversing till we find desired node
		mid_node = linked_list.node_at_index(mid_index)

		left_half = linked_list
		right_half = LinkedList()

		right_half.head = mid_node.next_node
		# left half points to node at the mid, we are making it the tail here.
		mid_node.next_node = None

		return left_half, right_half


def merge(left_half: LinkedList, right_half: LinkedList) -> LinkedList:
	"""
	Merges two linked lists, sorting by data in nodes.
	Takes O(n) time.
	:param left_half: linked list to be sorted and then merged with right_half
	:param right_half: linked list to be sorted and then merged with left_half
	:return: a new, merged linked-list
	"""
	merged = LinkedList()
	# add a fake head that is discarded later
	merged.add(0)
	current = merged.head

	left_head = left_half.head
	right_head = right_half.head
	# Iterate over left and right until we reach the tail node of either
	while left_head or right_head:
		if left_head is None:
			current.next_node = right_head
			right_head = right_head.next_node
		elif right_head is None:
			current.next_node = left_head
			left_head = left_head.next_node
		else:
			if left_head.data < right_head.data:
				current.next_node = left_head
				left_head = left_head.next_node
			else:
				current.next_node = right_head
				right_head = right_head.next_node
		current = current.next_node

		# discard fake head
	head = merged.head.next_node
	merged.head = head

	return merged


def main():
	l = LinkedList()
	test_list = [i for i in range(9)]
	random.shuffle(test_list)
	for i in test_list:
		l.add(i)
	print(l)
	sorted_linked_list = merge_sort(l)
	print(sorted_linked_list)


if __name__ == "__main__":
	main()

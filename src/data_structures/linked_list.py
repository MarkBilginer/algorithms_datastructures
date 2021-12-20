class Node:
	"""
	An object for storing a single node of a linked list.
	Models two attributes - data and the pointer to the next node in the list
	"""

	data = None
	next_node = None

	def __init__(self, data):
		self.data = data

	def __repr__(self):
		return "<Node data: %s>" % self.data


class LinkedList:
	"""
	Singly Linked List
	"""

	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head is None

	def size(self):
		"""
		Returns the number of nodes in the list
		Takes O(n) time.
		:return:
		"""
		current = self.head
		count = 0
		while current:  # while current!= None
			count += 1
			current = current.next_node
		return count

	def add(self, data):
		"""
		Adds a new node containing data at the head of the list.
		Takes O(1)
		:param data:
		:return: None
		"""
		new_node = Node(data)
		new_node.next_node = self.head
		self.head = new_node

	def insert(self, data, index):
		"""
		Inserts a new Node containing data at index position
		Insertion takes O(1) time but finding the node at the insertion
		point takes O(n) time.
		Takes overall O(n) time
		:param data: data to insert
		:param index: position of insertion
		:return: None
		"""
		if index == 0:
			self.add(data)

		if index > 0:
			new_node = Node(data)
			position = index
			current = self.head

			while position > 1:  # stops at prev_node
				current = current.next_node
				position -= 1

			prev_node = current
			next_node = current.next_node

			prev_node.next_node = new_node
			new_node.next_node = next_node

# implement remove_it where it removes node at specified index

	def remove(self, key):
		"""
		Removes node containing data that matches the key.
		O(n) time complexity due to linear search.
		:param key: value to be searched for.
		:return: deleted node if found, else None
		"""
		current = self.head
		previous = None
		found = False
		while current and not found:
			if current.data == key and current is self.head:
				found = True
				self.head = current.next_node
			elif current.data == key:
				found = True
				previous.next_node = current.next_node
			else:
				previous = current
				current = current.next_node
		return current

	def search(self, key):
		"""
		Search for the first node containing data that matches the key.
		Return the node or 'None' if not found.

		Takes O(n) time
		:param key: value to be searched for
		:return:  first element
		"""
		current = self.head

		while current:
			if current.data == key:
				return current
			else:
				current = current.next_node
		return None

	def node_at_index(self, index):
		if index == 0:
			return self.head
		else:
			position = index
			current = self.head
			for i in range(index):
				current = current.next_node
			return current

	def __repr__(self):
		"""
		Return a string representation of the list.
		Takes O(n) time
		:return: String representation.
		"""
		nodes = []
		current = self.head

		while current:
			if current is self.head:
				nodes.append("[Head: %s]" % current.data)
			elif current.next_node is None:
				nodes.append("[Tail: %s]" % current.data)
			else:
				nodes.append("[%s]" % current.data)

			current = current.next_node
		return '->'.join(nodes)


if __name__ == "__main__":
	l = LinkedList()
	print(l.size())
	N1 = Node(10)
	print(N1)
	N1.next_node = Node(100)
	print(N1)
	print(N1.next_node)
	l.head = N1
	l.add(1000)
	print(l.size())
	print(l)
	print(l.search(100))
	l.insert(33, 1)
	print(l)
	print(l.remove(33))
	print(l)
	print(l.node_at_index(1))


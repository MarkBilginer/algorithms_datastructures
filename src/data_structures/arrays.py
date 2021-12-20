def main():
	new_list = [1, 2, 3]
	result = new_list[0]

	if 1 in new_list: print(True)

	numbers = []
	print(len(numbers))
	numbers.append(2)
	print(len(numbers))

	numbers.extend([5, 6, 7, 8, 9])
	print(numbers)


if __name__ == "__main__":
	main()

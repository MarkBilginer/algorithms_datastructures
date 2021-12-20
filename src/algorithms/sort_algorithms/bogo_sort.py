import random
import sys
from src.helpful_functions.load import load_numbers


def main():
	# numbers = load_numbers(sys.argv[1])
	numbers = load_numbers("../../resources/numbers_1k.txt")

	print(numbers)
	print("Size of list is: %d" % len(numbers))


if __name__ == "__main__":
	main()
# This is a template for the exercises found in Aditya Y. Bhargava's "grokking algorithms"
# Chapter #: 1
# Exercise #: 9
# Topic: binary search

def binary_search(list, item):
	low = 0
	high = len(list)-1

	print("The list has "+str(high+1)+" items.")

	while low <= high:
		mid = (low + high) // 2
		print("The midpoint will be "+str(mid))
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

my_list = (1, 3, 5, 7, 9)

print(binary_search(my_list, 9))
print(binary_search(my_list, -1))

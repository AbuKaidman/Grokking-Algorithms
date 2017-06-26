# This is a template for the exercises found in Aditya Y. Bhargava's "grokking algorithms"
# Chapter #: 2
# Exercise #: 35
# Topic: selection sort
def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

print(selectionSort([5,3,6,2,10]))
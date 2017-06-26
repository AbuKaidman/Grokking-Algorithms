# This is a template for the exercises found in Aditya Y. Bhargava's "grokking algorithms"
# Chapter #: 2
# Exercise #: 41
# Topic: recursion

def countdown(i):
	print(i)
	if i <= 0:				# <-- Base case
		return
	else:					# <-- Recursive case
		countdown(i-1)

countdown(900)
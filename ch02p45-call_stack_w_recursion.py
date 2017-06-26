# This is a template for the exercises found in Aditya Y. Bhargava's "grokking algorithms"
# Chapter #: 2
# Exercise #: 45
# Topic: the call stack w recursion

def fact(x):
	if x == 1:
		return 1
	else:
		return x * fact(x-1)

fact(3)
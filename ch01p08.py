# This is a template for the exercises found in Aditya Y. Bhargava's "grokking algorithms"
# Chapter #1:
# Exercise #8:
# Topic: binary search
low = 0
high = len(list) -1
mid = (low + high) / 2
guess = list[mid]
if guess < item:
	low = mid + 1

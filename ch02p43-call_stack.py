# This is a template for the exercises found in Aditya Y. Bhargava's "grokking algorithms"
# Chapter #: 2
# Exercise #: 43
# Topic: the call stack

def greet(name):
	print("hello, " + name + "!")
	greet2(name)
	print("getting ready to say bye...")
	bye()

def greet2(name):
	print("how are you, " + name + "?")

def bye():
	print("ok, bye!")


greet("Tim")
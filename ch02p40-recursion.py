# This is a template for the exercises found in Aditya Y. Bhargava's "grokking algorithms"
# Chapter #: 2
# Exercise #: 40
# Topic: recursion

# Approach #1: using a -while- loop
def look_for_key(main_box):
	pile = main_box.make_a_pile_to_look_through()
	while pile is not empty:
		box = pile.grab_a_box()
		for item in box:
			if item.is_a_box():
				pile.append(item)
			elif item.is_a_key():
				print("found the key!")

# Approach #2: using recursion
def look_for_key(box):
	for item in box:
		if item.is_a_box():
			look_for_key(item)
		elif item.is_a_key():
			print("found the key!")
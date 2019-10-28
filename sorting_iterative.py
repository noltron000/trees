def is_sorted(items):
	'''
		Return a boolean indicating whether
		given items are in sorted order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# Check that all adjacent items are in order.
	for index, current_item in enumerate(items):
		if index == 0:
			pass
		else:
			previous_item = items[index - 1]
			# Return early if so.
			if not previous_item <= current_item:
				return False
	else:
		return True

def bubble_sort(items):
	'''
		Sort given items by swapping adjacent items
		that are out of order, and repeating until
		all items are in sorted order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# ==TODO==
	# Repeat until all items are in sorted order.

	# ==TODO==
	# Swap adjacent items that are out of order.

	pass


def selection_sort(items):
	'''
		Sort given items by finding minimum item,
		swapping it with first unsorted item,
		and repeating until all items are in sorted order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# ==TODO==
	# Repeat until all items are in sorted order.

	# ==TODO==
	# Find minimum item in unsorted items.

	# ==TODO==
	# Swap it with first unsorted item.

	pass


def insertion_sort(items):
	'''
		Sort given items by taking first unsorted item,
		inserting it in sorted order in front of items,
		and repeating until all items are in order.
		TODO: Running time: ??? Why and under what conditions?
		TODO: Memory usage: ??? Why and under what conditions?
	'''
	# ==TODO==
	# Repeat until all items are in sorted order.

	# ==TODO==
	# Take first unsorted item.

	# ==TODO==
	# Insert it in sorted order in front of items.

	pass

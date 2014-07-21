import sys

def Sort(inputList):
	# public function
	print 'You have ' + repr(len(inputList)) + ' items to sort.'

	# Our base case.  A list of 1 or less is considered sorted.
	if len(inputList) <= 0:
		return inputList

	# Find the mid point in the list, using int() to round in this case
	# although there is probably a better way.
	mid = int(len(inputList) / 2)
	print 'Mid is: ' + repr(mid)

	if mid < 2:
		return inputList
 
 	# Initialize our split lists
	left = []
	right = []

	# Copy the splits to their new homes.
	left = __copySubArray(inputList, 0, mid - 1)
	right = __copySubArray(inputList, mid, len(inputList))

	# Recursion!
	left = Sort(left)
	right = Sort(right)

	return __merge(left, right)

def __copySubArray(source, start, end):
	# private function
	
	# Same base case as caller, 1 or less is sorted.
	if len(source) < 2:
		return source

	destination = []

	for i in range(start, end):
		destination.append(source[i])
	return destination

def __merge(a, b):
	merged = []

	#while (len(a) > 0) or (len(b) > 0)


	return merged

def __split(a, b, start, end):
	if (end - start) < 2:
		return

	mid = int((start + end) / 2)
	print repr(mid)
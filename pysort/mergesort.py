import sys

def Sort(inputList):
	# public function

	# Our base case.  A list of 1 or less is considered sorted.
	if len(inputList) <= 1 :
		return inputList

	# Find the mid point in the list, using int() to round in this case
	# although there is probably a better way.
	mid = int(round(len(inputList) / 2))
 
 	# Initialize our split lists
	left = []
	right = []

	# Copy the splits to their new homes.
	left = __copySubArray(inputList, 0, mid )
	right = __copySubArray(inputList, mid, len(inputList))

	# Recursion!
	left = Sort(left)
	right = Sort(right)

	return __merge(left, right)

def __copySubArray(source, start, end):
	# Same base case as caller, 1 or less is sorted.
	if len(source) < 2:
		return source

	destination = []

	for i in range(start, end):
		destination.append(source[i])
	return destination

def __merge(a, b):
	merged = []

	while (len(a) > 0) or (len(b) > 0) :
		if len(a) > 0 and len(b) > 0 :
			if a[0] <= b[0] :
				merged.append(a[0])
				a = __rest(a)
			else :
				merged.append(b[0])
				b = __rest(b)
		elif len(a) > 0 :
			merged.append(a[0])
			a = __rest(a)
		elif len(b) > 0 :
			merged.append(b[0])
			b = __rest(b)

	return merged

def __rest(inputList):
	theRest = []

	for i in range(1, len(inputList)) :
		theRest.append(inputList[i])

	return theRest
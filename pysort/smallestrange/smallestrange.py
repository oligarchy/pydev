import sys

def Process(inputLists) :
	result = [0]
	filtered = []
	lastIndex = []
	smallestRange = sys.maxint

	if len(inputLists) <= 0 :
		return None

	# first we loop through all the lists in our list (yo dawg...)
	# filter out any that are empty of null
	# initialize the index holder to 0, since we haven't done a pass yet.
	for i in range(0, len(inputLists)) :
		if (inputLists[i] is None) or (len(inputLists[i]) <= 0) :
			continue

		filtered.append(inputLists[i])
		lastIndex.append(0)

	# now our setup is complete.  we iterate through, checking the range
	# and incrementing each index, storing the smallest range.
	# we use our index list to keep track of the last index on any particular list

	while True :
		
		vectorRange = 0
		vector = []

		for j in range(0, len(filtered)) :
			vector.append(filtered[j][lastIndex[j]])

		vectorRange = __findMax(vector) - __findMin(vector)
		print "Vector Range: " + repr(vectorRange)

		if vectorRange < smallestRange :
			smallestRange = vectorRange
			result = vector

		breakLoop = True

		for k in range(0, len(lastIndex)) :
			if lastIndex[k] < len(filtered[k]) - 1 :
				lastIndex[k] += 1
				breakLoop = False

		if (breakLoop) :
			break

	return result

def __findMin(values) :
	toSort = values[:]  # this allows for a shallow copy in python
	toSort.sort()
	print "Min " + repr(toSort[0])
	return toSort[0]

def __findMax(values) :
	toSort = values[:] # this allows for a shallow copy in python
	toSort.sort()
	print "Max " + repr(toSort[len(toSort) - 1])
	return toSort[len(toSort) - 1]

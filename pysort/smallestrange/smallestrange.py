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

	allVectors = []
	vector = []

	for topItemIndex in filtered[0] :

		iterationCount = 0
		for listIndex in range(1, len(filtered)) :
			for subItem in filtered[listIndex] :
				





	currentList = 0
	currentIndex = 0

	while True :
		
		print "Current List: " + repr(currentList)
		if currentList >= len(filtered) :
			break

		vectorRange = 0
		vector = []
	
		for j in range(currentList, len(filtered)) :
			vector.append(filtered[j][lastIndex[j]])
			
			if lastIndex[j] >= len(filtered[j]) - 1 :
				lastIndex[j] = 0
			else :
				lastIndex[j] += 1

		vectorRange = __findMax(vector) - __findMin(vector)
		print "Vector : " + ", ".join([str(x) for x in vector])
		print "Vector Range: " + repr(vectorRange)

		if vectorRange < smallestRange :
			smallestRange = vectorRange
			result = vector

		lastIndex[currentIndex] += 1

		if lastIndex[currentList] >= len(filtered[currentList]) :
			currentIndex = 0
			currentList += 1
		else : 
			currentIndex += 1

	return result

def __findMin(values) :
	toSort = values[:]  # this allows for a shallow copy in python
	toSort.sort()
	#print "Min " + repr(toSort[0])
	return toSort[0]

def __findMax(values) :
	toSort = values[:] # this allows for a shallow copy in python
	toSort.sort()
	#print "Max " + repr(toSort[len(toSort) - 1])
	return toSort[len(toSort) - 1]

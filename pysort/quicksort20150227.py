import sys

def Sort(input, low, high) :
	if input == None or len(input) <= 1 : 
		return input

	if low < high :
		pivot = __partition(input, low, high)
		input = Sort(input, low, pivot - 1)
		input = Sort(input, pivot + 1, high)

	return input

def __partition(input, low, high) :
	pivotIndex = __choosePivot(input, low, high)
	pivotValue = input[pivotIndex]

	input = __swap(input, pivotIndex, high)
	
	storeIndex = low

	for i in range(low, high) :
		if input[i] < pivotValue :
			input = __swap(input, i, storeIndex)
			storeIndex += 1
	
	input = __swap(input, storeIndex, high)
	return storeIndex


def __choosePivot(input, low, high) :
	pivotMean = int((low + high) / 2)
	return pivotMean

def __swap(input, first, second) :
	temp = input[first]
	input[first] = input[second]
	input[second] = temp
	
	return input
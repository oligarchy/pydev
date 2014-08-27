import sys

def Sort(input, left, right) :
	if len(input) <= 1 :
		return input

	if left < right :
		partition = __partition(input, left, right)
		input = Sort(input, left, partition - 1)
		input = Sort(input, partition + 1, right)

	return input

def __partition(input, left, right) :
	pivotIndex = __choosePivot(input, left, right)
	pivotValue = input[pivotIndex]

	input = __swap(input, pivotIndex, right)

	storeIndex = left

	for i in range(left, right) :
		if input[i] < pivotValue :
			input = __swap(input, i, storeIndex)
			storeIndex += 1

	input = __swap(input, storeIndex, right)

	return storeIndex

def __choosePivot(input, left, right) :
	mid = int((left + right) / 2)
	return mid

def __swap(input, left, right) :
	temp = input[left]
	input[left] = input[right]
	input[right] = temp

	return input
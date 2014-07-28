import sys

class QuickSort :
	"I wanted to do a simple test of making a class"

	toSort = []

	def __init__(self, inputList) :
		toSort = inputList

	def Sort(self, inputList, start, end) :
		if len(inputList) <= 1 :
			return inputList

		self.toSort = inputList
		sortedList = []

		if start < end :
			partition = self.__partition(inputList, start, end)
			sortedList = self.Sort(inputList, start, partition - 1)
			sortedList = self.Sort(inputList, partition + 1, end)

		return sortedList

	def __partition(self, inputList, start, end) :
		pivotIndex = self.__choosePivot(inputList, start, end - 1)
		pivotValue = inputList[pivotIndex]

		inputList = self.__swap(inputList, pivotIndex, end - 1)
		
		for i in range(start, end - 1) :
			if inputList[i] <= pivotValue :
				inputList = self.__swap(inputList, i, pivotIndex)
				start = start + 1

		return pivotIndex

	def __choosePivot(self, inputList, start, end) : 
		return int(len(inputList) / 2)

	def __swap(self, inputList, a, b) :
		print("Swap: " + repr(a) + ":" + repr(b))

		leftValue = inputList[a]
		inputList[a] = inputList[b]
		inputList[b] = leftValue

		return inputList

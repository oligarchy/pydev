import sys

class QuickSort :
	"I wanted to do a simple test of making a class"

	def Sort(self, inputList, start, end) :
		if len(inputList) <= 1 :
			return inputList

		if start < end :
			pivot = self.__partition(inputList, start, end)
			self.Sort(inputList, start, pivot - 1)
			self.Sort(inputList, pivot + 1, end)

		return inputList

	def __partition(self, inputList, start, end) :
		pivotIndex = inputList[start]
		
		left = start + 1
		right = end
		done = False

		while not done :
			while left <= right and inputList[left] <= pivotIndex :
				left = left + 1
			
			while inputList[right] >= pivotIndex and right >= left :
				right = right - 1
			
			if right < left :
				done = True
			else :
				temp = inputList[left]
				inputList[left] = inputList[right]
				inputList[right] = temp

		temp = inputList[start]
		inputList[start] = inputList[right]
		inputList[right] = temp

		return right
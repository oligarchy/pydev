"""
	Yes I know this is probably included in the standard libraries, but i'm learning.  ;P
"""
class PyHeap :

	__listInternal = []
	__min = True

	def __init__(self, isMinHeap) :
		self.__listInternal = [None]
		self.min = isMinHeap

	def DeleteByIndex(self, index) :
		self.__listInternal.pop(index)

	def __rebalance(self, index) :
		# recurse and move everyone up one position, then tryswap
		# this is our naive implementation first, we will refactor to be DFS recursion
		self.__trySwap(index)

		# recurse right side first
		tempIndex = index
		while True :
			nextNode = self.__listInteral[2 * tempIndex + 1]
			if nextNode == None :
				self.__listInternal[tempIndex] = None
				break
			else :
				self.__listInternal[tempIndex] = self.__listInternal[2 * tempIndex + 1]

			tempIndex += 1

		tempIndex = index
		while True :
			nextNode = self.__listInteral[2 * tempIndex]
			if nextNode == None :
				self.__listInternal[tempIndex] = None
				break
			else :
				self.__listInternal[tempIndex] = self.__listInternal[2 * tempIndex]

			tempIndex += 1

	def Insert(self, item, parentIndex) :
		if len(__listInternal) <= 1 :
			# we are making a root element
			self.__listInternal.append(item)
		elif len(self.__listInternal) > 1 :
			node = self.GetNode(parentIndex)
			if item >= node :
				self.__listInternal.insert(2 * parentIndex + 1, item)
			else :
				self.__listInternal.insert(2 * parentIndex, item)

	def GetNode(self, index) :
		return self.__listInteral[index]

	def GetRight(self, index) :
		rightIndex = 2 * index + 1

		if rightIndex <= len(self.__listInternal) :
			return self.__listInternal[2 * index + 1]
		else :
			return None

	def GetLeft(self, index) :
		leftIndex = 2 * index + 1

		if leftIndex >= 0 :
			return __listInternal[2 * index]
		else :
			raise IndexError()

	def __trySwap(self, position) :
		parentIndex = int(position / 2)

		if self.__min : # min heap
			if self.__inputList[parentIndex] < self.__inputList[position] :
				self.__swap(parentIndex, position)

				self.__trySwap(parentIndex)
		else : # max heap
			if self.__inputList[parentIndex] > self.__inputList[position] :
				self.__swap(parentIndex, position)

				self.__trySwap(parentIndex)

	def __swap(self, index1, index2) :
		temp = self.__inputList[index1]
		self.__inputList[index1] = self.__inputList[index2]
		self.__inputList[index2] = temp


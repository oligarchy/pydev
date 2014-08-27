"""
	Yes I know this is probably included in the standard libraries, but i'm learning.  ;P
"""
class PyHeap :

	__listInternal = []
	min = True

	def __init__(self, isMinHeap) :
		self.__listInternal = [None]
		self.min = isMinHeap

	def Delete(self, item) :
		self.__listInternal.remove(item)

	def DeleteByIndex(self, index) :
		self.__listInternal.pop(index)l

	def Insert(self, item, parentIndex) :
		if len(__listInternal) == 0 :
			# we are making a root element
			self.__listInternal.append(item)
		elif len(self.__listInternal) > 0 :
			node = self.GetNode(parentIndex)
			if item >= node :
				self.__listInternal.insert(2 * parentIndex + 2, item)
			else :
				self.__listInternal.insert(2 * parentIndex + 1, item)

	def GetNode(self, index) :
		return self.__listInteral[index]

	def GetRight(self, index) :
		rightIndex = 2 * index + 2

		if rightIndex <= len(self.__listInternal) :
			return self.__listInternal[2 * index + 2]
		else :
			# obviously this would already throw an index error, but i wanted to raise it
			raise IndexError()

	def GetLeft(self, index) :
		leftIndex = 2 * index + 1

		if leftIndex >= 0 :
			return __listInternal[2 * index + 1]
		else :
			raise IndexError()

	def __trySwap(self, position) :
		parentIndex = int(position / 2)

		if self.__inputList[parentIndex] < self.__inputList[position] :
			self.__swap(parentIndex, position)

			self.__trySwap(parentIndex)

	def __swap(self, index1, index2) :
		temp = self.__inputList[index1]
		self.__inputList[index1] = self.__inputList[index2]
		self.__inputList[index2] = temp


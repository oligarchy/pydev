# min heap

class MyHeap :
	
	def Parent(self, index):
		if index == 1 :
			return -1
		else :
			return int(index / 2)

	def Child(self, index) :
		return 2 * index

	def OldChild(self, index) :
		return 2 * index + 1

	listInternal = []

	def __init__(self) :
		self.listInternal = [None]

	def Insert(self, item) :
		self.listInternal.append(item)
		self.BubbleUp(len(self.listInternal) - 1)

	def BubbleUp(self, index) :
		if self.Parent(index) == -1 :
			return

		if self.listInternal[self.Parent(index)] > self.listInternal[index] :
			self.Swap(self.Parent[index], index)
			self.BubbleUp(self.Parent(index))

	def Swap(self, first, second) :
		#temp = second
		#second = first
		#first = temp

		first, second = second, first

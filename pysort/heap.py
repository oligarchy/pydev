"""
	Yes I know this is probably included in the standard libraries, but i'm learning.  ;P
"""

__listInternal = []

def Insert(item) :
	__listInternal.append(item)

def Delete(item) :
	__listInternal.remove(item)

def DeleteByIndex(index) :
	__listInternal.pop(index)l

def Add(item, parentIndex) :
	if len(__listInternal) == 0 :
		# we are making a root element
		__listInternal.append(item)
	elif len(__listInternal) > 0 :
		node = GetNode(parentIndex)
		if item >= node :
			__listInternal.insert(2 * parentIndex + 2, item)
		else :
			__listInternal.insert(2 * parentIndex + 1, item)

def GetNode(index) :
	return __listInteral[index]

def GetRight(index) :
	rightIndex = 2 * index + 2

	if rightIndex <= len(__listInternal) :
		return __listInternal[2*index+2]
	else :
		# obviously this would already throw an index error, but i wanted to raise it
		raise IndexError()

def GetLeft(index) :
	leftIndex = 2 * index + 1

	if leftIndex >= 0 :
		return __listInternal[2*index+1]
	else :
		raise IndexError()

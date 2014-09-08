import sys
import heapq

def Process(inputLists) :
	heap = []

	for i in range(0, len(inputLists)) :
		print "i: " + repr(i)

		for j in range(0, len(inputLists[i])) :
			print "j: " + repr(inputLists[i][j])
			heapq.heappush(heap, inputLists[i][j])

	print "heap count: " + repr(len(heap))
import mergesort
# import quicksort
import quicksort20150227
#import heap

words = ['zebra', 'cat', 'banana', 'sultan', 'apple', 'cat', 'aardvark', 'hippo', 'dingo']
sortedWords = []

numbers = [3, 8, 11, 7, 4, 55, 22, 99, 22, 13, 45, 31]
sortedNumbers = []

sortedWords = quicksort20150227.Sort(words, 0, len(words) - 1)
sortedNumbers = quicksort20150227.Sort(numbers, 0, len(numbers) - 1)

#print 'First we try to Quick sort numbers.'
#sortedNumbers = qsortNumbers.Sort(numbers, 0, len(numbers) - 1)


#print 'Then we try to quick sort words'
#sortedWords = qsortWords.Sort(words, 0, len(words) - 1)

#print 'First we try to Merge sort numbers.'
#sortedNumbers = mergesort.Sort(numbers)

if sortedNumbers != None and len(sortedNumbers) != 0 :
	for number in sortedNumbers:
		print(repr(number))
else :
	print("No sorted numbers.")

#print 'Then we try to Merge sort words.'
#sortedWords = mergesort.Sort(words)

if sortedWords != None and len(sortedWords) != 0 :
	for word in sortedWords:
	 	print(word)
else :
	print("No sorted words.")

# semi colons and braces are for chumps
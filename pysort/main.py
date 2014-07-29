import mergesort
import quicksort
import heap

words = ['zebra', 'cat', 'banana', 'sultan', 'apple']
sortedWords = []

numbers = [3, 8, 11, 7, 4, 55, 22, 99]
sortedNumbers = []

qsortWords = quicksort.QuickSort()
qsortNumbers = quicksort.QuickSort()

print 'First we try to Quick sort numbers.'
sortedNumbers = qsortNumbers.Sort(numbers, 0, len(numbers) - 1)


print 'Then we try to quick sort words'
sortedWords = qsortWords.Sort(words, 0, len(words) - 1)

#print 'First we try to Merge sort numbers.'
#sortedNumbers = mergesort.Sort(numbers)

for number in sortedNumbers:
	print repr(number)

#print 'Then we try to Merge sort words.'
#sortedWords = mergesort.Sort(words)

for word in sortedWords:
 	print word

# semi colons and braces are for chumps
import mergesort
words = ['zebra', 'cat', 'banana', 'sultan', 'apple']
sortedWords = []

numbers = [3, 8, 11, 7, 4, 55, 22, 99]
sortedNumbers = []

print 'First we try to sort numbers.'
sortedNumbers = mergesort.Sort(numbers)

for number in sortedNumbers:
	print repr(number)

print 'Then we try to sort words.'
sortedWords = mergesort.Sort(words)

for word in sortedWords:
	print word

# it is really hard trying to ignore the muscle memory to put semicolons at the end of each line.
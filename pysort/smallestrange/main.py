import smallestrangeheap

list1 = [4, 10, 15, 24, 26]
list2 = [0, 9, 12, 20]
list3 = [5, 18, 22, 30]

listOfLists = [list1, list2, list3]

# are the input lists always in sorted order?  		(for this test, let's assume yes)
# upper or lower bound for input list?				(for this test let's assume 0 - 500)
# max or min number or items in input lists?		(for this test let's assume min = 0, max = n)
# what about duplicates across the input lists?		(not sure)

# You have k lists of sorted integers. Find the smallest range that includes at least one number from each of the k lists.

# For example,
# List 1: [4, 10, 15, 24, 26]
# List 2: [0, 9, 12, 20]
# List 3: [5, 18, 22, 30]

# The smallest range here would be [20, 24] as it contains 24 from list 1, 20 from list 2, and 22 from list 3.

resultSet = smallestrangeheap.Process(listOfLists)

for i in range(0, len(resultSet)) :
	print resultSet[i]
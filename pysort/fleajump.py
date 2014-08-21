import sys

# D is the total distaince in mm we need to more
# T is the number of jumps forward
# B is the length of the big jump
# small jump is 1

class LongLongTripDiv2 :
	def isAble(self, D, T, B) :
		if D < 1 or D > 10000000000000000000 :
			raise ValueError('D is not within the correct bounds.')

		if T < 1 or T > 1000000000 :
			raise ValueError('T is not within the correct bounds.')

		if B < 1 or B > 1000000000 :
			raise ValueError('T is not within the correct bounds.')

		if T * B == D :
			return "Possible"
		elif D == T :
			return "Possible"
		elif self.divModDecision(D, T, B):
			return "Possible"
		else :
			return "Impossible"

	def divModDecision(self, D, T, B) :
		#dm = divmod(D, B)
		# print repr(dm[0]) + '/' + repr(dm[1])
		# loop through number of moves
		# add constant times current iteration
		# add B times that difference.  number of moves - 1 current iteration

		for i in range(1, T) :
			
			
		return True

# test cases
longTrip = LongLongTripDiv2()

# possible
result = longTrip.isAble(10, 6, 3)
print(result)

# impossible
result = longTrip.isAble(10, 5, 3)
print(result)

# impossible
result = longTrip.isAble(50, 100, 2)
print(result)

# possible
result = longTrip.isAble(10, 10, 9999)
print(result)

# possible
result = longTrip.isAble(1000, 100, 10)
print(result)

# possible
result = longTrip.isAble(1000010000100001, 1100011, 1000000000)
print(result)
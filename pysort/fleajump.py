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
		elif self.Decide(D, T, B):
			return "Possible"
		else :
			return "Impossible"

	def Decide(self, D, T, B) :
		answer = False

		for i in range(0, T) :
			prod = i + B * (T - i)

			if prod == D :
				answer = True
				break
			
		return answer

# test cases
longTrip = LongLongTripDiv2()

# possible
result = longTrip.isAble(10, 6, 3)
print("Expected: Possible  -  Actual: " + result)

# impossible
result = longTrip.isAble(10, 5, 3)
print("Expected: Impossible  -  Actual: " + result)

# impossible
result = longTrip.isAble(50, 100, 2)
print("Expected: Impossible  -  Actual: " + result)

# impossible
result = longTrip.isAble(120, 10, 11)
print("Expected: Impossible  -  Actual: " + result)

# possible
result = longTrip.isAble(10, 10, 9999)
print("Expected: Possible  -  Actual: " + result)

# possible
result = longTrip.isAble(1000, 100, 10)
print("Expected: Possible  -  Actual: " + result)

# possible
result = longTrip.isAble(1000010000100001, 1100011, 1000000000)
print("Expected: Possible  -  Actual: " + result)
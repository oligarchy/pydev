
# this will be our brute force implementation
def NaiveIsSubstring(str1, str2) :

	# base case validation.  if str1 is empty or longer, it can't be a substring

	if (str1 == None) or (len(str1) == 0) :
		return False

	if (str2 == None) or (len(str2) == 0) :
		return False

	if len(str1) > len(str2) :
		return False

	# generate permutations
	permutatations = [str1]
	for i in range(1, len(str1)) :

		head = str1[len(str1) - i:]
		tail = str1[:len(str1) - i]
		
		permutatations.append(head + tail)

	for perm in range(0, len(permutatations) - 1) :
		if (isSubstring(permutatations[perm], str2)) :
			return True

	return False

def isSubstring(str1, str2) :
	if str1 in str2 :
		return True
	else :
		return False
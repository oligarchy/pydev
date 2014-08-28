import isSubstring

str1 = "grass"
str2 = "wheatgrass"
isSub = isSubstring.NaiveIsSubstring(str1, str2)
print str1 + ":" + str2 + " - " + repr(isSub)

str1 = "basecasevalidation"
str2 = "dog"
isSub = isSubstring.NaiveIsSubstring(str1, str2)
print str1 + ":" + str2 + " - " + repr(isSub)

str1 = ""
str2 = "wheatgrass"
isSub = isSubstring.NaiveIsSubstring(str1, str2)
print str1 + ":" + str2 + " - " + repr(isSub)

str1 = "grass"
str2 = ""
isSub = isSubstring.NaiveIsSubstring(str1, str2)
print str1 + ":" + str2 + " - " + repr(isSub)

str1 = "nope"
str2 = "asdfghjkl"
isSub = isSubstring.NaiveIsSubstring(str1, str2)
print str1 + ":" + str2 + " - " + repr(isSub)

str1 = "ogd"
str2 = "dog"
isSub = isSubstring.NaiveIsSubstring(str1, str2)
print str1 + ":" + str2 + " - " + repr(isSub)

str1 = "frag"
str2 = "superkalifragilisticexpialidocious"
isSub = isSubstring.NaiveIsSubstring(str1, str2)
print str1 + ":" + str2 + " - " + repr(isSub)

str1 = "alifragilisticexpialidocioussuperk"
str2 = "superkalifragilisticexpialidocious"
isSub = isSubstring.NaiveIsSubstring(str1, str2)
print str1 + ":" + str2 + " - " + repr(isSub)
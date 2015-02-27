x = 1
y = 2

print(repr(x)) # 1
print(repr(y)) # 2

x = y

print(repr(x)) # 2
print(repr(y)) # 2

y = 3

print(repr(x)) # 2
print(repr(y)) # 3

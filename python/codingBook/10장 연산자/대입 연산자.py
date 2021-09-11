a = None
b = None
c = 5
d = None

a = b = c  # a = 5, b = 5 가 된다.

print(a)
print(b)
print(c)
print(a is c) # bool 로 반환
print(b is d) # bool로 반환
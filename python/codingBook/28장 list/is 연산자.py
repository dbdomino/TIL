a = [6, 7, 5, 7]
print(a)
a[1] = 'A' # 원하는 위치의 요소를 형태에 관계없이 대입가능
print(a)
print('--------------')
b = a
print(a is b) # bool 형식으로 반환, 같은지 다른지 비교하는건가?
c = [6, 7, 5, 7]
print(a is c) # 다르면 false 반환
d = [6, 7, 5, 7, 2]
print(a is d) # 일부만 같더라도 다르다고 판정함, false 반환


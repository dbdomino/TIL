a = [1, 2, 3, 4]
a_1 = a.pop() # a.pop()으로 a의 마지막 요소를 불러온 뒤에 a에서 마지막 요소를 삭제한다.
print(a)
a_2 = a.pop(0) # a.pop(위치)로 a의 해당위치의 요소를 불러온 뒤에 a에서 삭제한다.
print(a)
print(a_1)
print(a_2)
print('------------------')
a.clear #에러로는 안걸리는데, 아무작동도안함
print(a)
a.clear() # 리스트 초기화
print(a)

# sort 리스트에서 자동으로 정렬해줌
a = [ 7, 5, 3 ,4, 1 ,9 ,2 ]
print(a)
a.reverse() # 리스트의 순서를 역순으로 변경해줌, 매우편리
print(a)
a.sort() # 오름차순으로 정렬, 편하네이거
print(a)
a.reverse()
print(a)

b = a.copy()

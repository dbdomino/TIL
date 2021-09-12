r = 123
k = 0
print(r)
while r != 0: # r !=0 이 True 이면 반복 r == 0 이면 반복종료
    k = k*10 + r % 10
    r //= 10
print(k)
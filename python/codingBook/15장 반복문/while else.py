a = 0
while a < 5:
    print(a)
    a += 1
else: # while이 모두 끝나고 한번만 실행
    a += 1
    print('else a = ', a)
print('result = ', a)

b = 1
cnt = 0
while b <= 100:
    if b % 3 == 0:
        print(b, end=' ')
        cnt += 1
        if cnt == 10:
            cnt = 0
            print()
    b += 1

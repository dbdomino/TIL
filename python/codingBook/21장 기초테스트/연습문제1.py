# 230 페이지 연습문제
print('5번문제')
for i in range(1,6):
    print(' '*(5-i),end='')
    for j in range(1,i*2):
        print(j,end='')
    print(' ' * (5 - i), end='')
    print('')
print('6번문제')
for i in range(1,6):
    print(' '*(i-1), end='')
    for j in range(1,(6-i)*2):
        print(j,end='')
    print(' ' *(i-1), end='')
    print('')
print('7번문제')
for i in range(1,6):
    print(' '*(5-i),end='')
    for j in range((11 - i*2),10):
        print(j,end='')
    print(' ' * (5 - i), end='')
    print('')
print('8번문제')
for i in range(1,6):
    print(' '*(i-1), end='')
    for j in range(i*2-1,10):
        print(j,end='')
    print(' ' *(i-1), end='')
    print('')
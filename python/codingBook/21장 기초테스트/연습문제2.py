# print(ord('A'))
print(chr(65))
print(chr(66))
print(chr(67))
print(chr(68))
print(chr(69))
print('10번')
for i in range(1,6):
    print(' '*(5-i),end='')
    for j in range(1,i*2):
        print(chr(64+i),end='')
    print(' ' * (5 - i), end='')
    print('')
print('11번')
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end='')
    print(' ' * (5 - i), end='')
    print('')
print('12번')
for i in range(1,6):
    print(' '*(5-i),end='')
    for j in range(1,i*2):
        print(chr(63+i+j),end='')
    print(' ' * (5 - i), end='')
    print('')


a = int(input())
cnt = 0
for i in range(1, 11):
    for j in range(i+1, 11):
        for k in range(j+1, 11):
            if i+j+k == a:
                print(i,j,k)
                cnt += 1

print(cnt)
a = 5
b = 6
if not(a % 2):
    print('a 는 짝수') # a % 2 = 1, not(1) = False
else:
    print('a는 홀수')

if not(b % 2):
    print('b 는 짝수') # b % 2 = 0, not(0) = True
else:
    print('b는 홀수')

c = int(input())
if 1 <= c <= 10:
    print('1 or more and 0 or less')
else:
    print('less')
a, b = map(int, input().split())

if a>0 and b>0:
    print('a>0 and b>0')
else:
    print('a<=0 or b<=0')

if a%2 == 0 or b%2 == 0:
    print('a와 b 중 하나는 짝수')
else:
    print('a와 b는 홀수')


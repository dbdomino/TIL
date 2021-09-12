# 자연수의 제곱이되는 1^2, 2^2 3^2 4^2 같은 수를 완전제곱수 또는 정사각 수 라고한다.
import math
k = math.sqrt(2) # 제곱근 구하기
print(k)

for i in range(1, 101):
    k = int(math.sqrt(i))
    if k * k == i:
        print(i)

for i in range(1, 101):
    k = 1
    while k * k < i:
        k += 1
    if k*k == i:
        print(i)
print('--------')
a, b = 14, 1
while b * b < a:
    b += 1
if b * b == a:
    print(a)
    print(b)
else:
    print('a',a,'는 완전제곱수로 될수없다.')
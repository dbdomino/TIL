# 자연수의 제곱이되는 1^2, 2^2 3^2 4^2 같은 수를 완전제곱수 또는 정사각 수 라고한다.
import math

for i in range(1, 101):
    cnt = 0
    for j in range(1, i+1): # i에 대한 약수의 개수 구하기
        if i % j == 0:
            cnt += 1
    if cnt % 2 == 1:  # i의 약수가 홀수개이면 완전제곱수
        print(i)

for i in range(1, 101):
    k = int(math.sqrt(i))
    if k * k == i:
        print(i)
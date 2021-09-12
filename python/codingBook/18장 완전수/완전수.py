# 그 수 자신을 제외한 모든 약수의 합이 그 수 자신과 같은수를 완전수(Perfect Number)라고 한다.
sum, num = 0, 28
for i in range(1, num):
    if num % i == 0:
        sum += i
if num == sum:
    print('완전수')
if num < sum:
    print('부족수')
if num > sum:
    print('과잉수')
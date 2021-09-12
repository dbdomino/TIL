# 1부터 N까지 모두 곱한수를 N팩토리얼 이라고한다, N!

fact = 1
fact *= 1
fact *= 2
fact *= 3
fact *= 4
fact *= 5
print('5! = '+str(fact))

a = int(input())
fact = 1
sample = '1'
for i in range(1,a+1):
    fact *= i
    if i>=2:
        sample += '*'+str(i)
print(str(a)+'!=('+sample+')='+str(fact))
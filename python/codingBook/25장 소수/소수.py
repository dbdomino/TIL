print(sum(range(1, 6)))
# 소수 1보다 큰 자연수 중에서 1과 자기자신 이외의 약수를 가지지 않는 수, 즉 약수가 2개인 자연수를 소수라고 한다.
for i in range(2, 11):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        print(i)

a, b, c = map(int, input().split())
dp = []
sum = 0
for i in range(a, b+1):
    cnt = 0
    for j in range(1, i+1):
        if i  % j == 0:
            cnt += 1
    if cnt == 2:
        dp.append(i)
        sum += i
print(sum)
if c <= len(dp):
    print(dp[c-1])
else:
    print(-1)
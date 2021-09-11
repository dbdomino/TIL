# N 마리 몬스터(4≤N≤10,000) 원형들판에 살고있다.
# 원형들판의 중심에서 바깥으로 놓여있는 K(3≤K≤1,000)개의 울타리를 동일한 각도(정확하게 360 / T)로 설치하고싶다.
# 결과 몬스터는 K세트로 나뉜다.
# 몬스터위 위치는 고정되어있다. 원들판을 어떻게 회전하느냐에따라 몬스터의 마리수가 달라진다. 각도 T
# 범위 = 가장많은 몬스터가 있는 세트의 몬스터수 - 가장적은 몬스터가 있는 세트의 몬스터수
# 주어진 범위?에서 최소 범위의 값을 구하라(범위의 최소값이라...
# 조건1 세트의 몬스터수 최소값은 1



N, K = map(int, input().split())

dp1 = [] #
for i in range(N): # 몬스터위치 입력
    dp1.append(float(input()))

Angle = 360 / K
maxA = 1 # 가장많은 세트의 몬스터수
minA = 1 # 가장적은 세트의 몬스터수
tmpA = 0
tmp1 = 0.0
dp2 = [] # 범위 입력

for i in range(N): # 몬스터별 maxA, minA비교
    tmp1 = dp1[i] + Angle #각도 상위덧샘해서 세트수구하기
    for j in range(N):
        # print('dp[', j, ']=', dp[j], ' tmp1 = ', tmp1, sep='')
        if dp1[j] <= tmp1:

            tmpA += 1
    dp1[i] += 360
    dp2.append(tmpA) # 몬스터 기준 최대 세트들
    # print('tmpA',tmpA)
    if tmpA > maxA:
        maxA = tmpA
    # if tmpA < minA:
    #     minA = tmpA
    tmpA = 0
t1 = min(dp2)

for i in range(N):
    if dp2[i] == t1:
        dp2[i] = maxA
t2 = min(dp2)
# print(t1)
# print(t2)
print(t2 - t1)
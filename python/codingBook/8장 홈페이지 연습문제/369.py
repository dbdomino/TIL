#369게임이 N까지 규칙을 지키며 진행된다면 그때까지의 들은 박수의 횟수가 총 몇 번인지 궁금
#N = 14라면, 3, 6, 9, 13에서 각각 한 번의 박 수를 치게 되므로 총 4회의 박수를 듣게 될 것
#N = 36이라면 3, 6, 9, 13, 16. 19. 23. 26. 29. 30. 31. 32. 33. 34. 35, 36에서 박수를 치게 되는데
# 33, 36에서는 각 각 두 번 박수를 쳐야 하므로 총 18회가 된다.
#1이상 정수에서 369게임을 N까지 규칙을 지키며 진행된다면 박수횟수 계산하는 프로그램 작성

# 1부터 p까지 3의 배수이거나 3,6,9가 들어간 수의 개수를 구하는 방법은 다음과 같이 크게 3가지로 나누어 볼 수 있다.
#
# 1. n(3의 배수) + n(3의 배수가 아니면서 3,6,9가 들어간 수)
# 2. n(3,6,9가 들어간 수) + n(3,6,9가 들어있지 않은 3의 배수)
# 3. n(3의 배수) + n(3,6,9가 들어간 수) - n(3의 배수이고 3,6,9가 들어간 수)


# a = int(input())
# a = input()
# a = float(a)
# a = int(a)


# a = int(input())
# st = str(a)
# len = len(str(st))
#
# dp1 = {1, 3, 60, 900, 12000, 150000, 1800000}
# dp2 = {1, 10, 100, 1000, 10000, 100000, 1000000}
# total = 0
# for i in range(len, 0, -1):
#     tmp = int(st[i-1])
#     if tmp < 4:
#         total = st[i-1] * dp1[i-1]
#     else if (tmp >= 4 and tmp <= 6):
#         total = st[i-1] * dp1[i-1] + dp2[i-1] * 1
#     else if (tmp >= 7 and tmp <= 9):
#         total = st[i-1] * dp1[i-1] + dp2[i-1] * 2
#
#     if i % 3 == 0:
#         print('')
#
# print(total)


# # def cal100(a):
#     total = 0
#     for i in range(1, a+1):
#         st = str(i)
#         for j in range(len(st)):
#             if int(st[j]) % 3 == 0 and st[j] != '0':
#             if st[j] == '3' or st[j] == '6' or st[j] == '9':
#                 total +=1
#     return total
#
# a = int(input())
# print(cal100(a))
a = int(input())
total = 0
for i in range(1, a + 1):
    st = str(i)
    for j in range(len(st)):
        if int(st[j]) % 3 == 0 and st[j] != '0':
            if st[j] == '3' or st[j] == '6' or st[j] == '9':
                total += 1
print(total)

# 900 1900(4 7)
# 12000 22000(4 7)
import math

def cal100(a):
    aa = a
    st = str(a)
    st_len = len(st)
    tmp = 0
    total = 0

    for i in range(st_len):
        if int(st[st_len-1-i]) == 9:
            tmp=3
        elif int(st[st_len-1-i]) >= 6:
            tmp=2
        elif int(st[st_len-1-i]) >= 3:
            tmp=1
        else:
            if i >= 1:
                tmp=1
            else:
                tmp=0

        aa = aa//10
        if i >= 1:
            total += aa * 3 * math.pow(10, i) +  tmp * (math.pow(10, i))
        else:
            total += aa * 3 * math.pow(10, i) + tmp


        print('aa=',aa,'i = ',i, ' total=', total)


    return int(total)
# print(10//10)
# print(math.log10(10))
a = int(input())
print(cal100(a))
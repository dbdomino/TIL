a, b, c = map(int, input().split())
tmp = c-(a*b)
if tmp < 0:
    tmp *= -1
elif tmp > 0:
    tmp = 0
print(tmp)

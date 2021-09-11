# 현재시간 A시 B분
# 소요시간 C분
A, B = map(int, input().split())
C = int(input())

C_Hour = 0
C_Minute = 0
if C >= 60:
    C_Hour = C//60
    C_Minute = C%60
else:
    C_Minute = C

if (C_Minute+B) >= 60:
    A += C_Hour + (C_Minute+B) // 60
    B = (C_Minute+B) % 60
else:
    A += C_Hour
    B = C_Minute+B

if A >= 24:
    A -= 24

print(A,B)
print((A + (B+C)//60 ) %24, (B+C) % 60)
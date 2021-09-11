a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())
T = a + b + c + d
S = e + f + g + h
if T > S:
    print(T)
elif T < S:
    print(S)
else:
    print(T)
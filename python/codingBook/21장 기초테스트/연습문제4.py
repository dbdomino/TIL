b = int(input())
for i in range(1, b * 2):
    if i < b:
        for j in range(1, i + 1):
            print(j, end='')
        for k in range(1, (b - i) * 2):
            print(' ', end='')
        for j in range(i, 0, -1):
            print(j, end='')
        print()
    elif i == b:
        for j in range(1, b):
            print(j, end='')
        if b == 10:
            print(0, end='')
        else:
            print(b, end='')
        for j in range(b-1, 0, -1):
            print(j, end='')
        print()
    else:
        for j in range(1, b*2 - i + 1):
            print(j, end='')
        for k in range((i-b) * 2, 1,-1):
            print(' ', end='')
        for j in range((b*2-i), 0, -1):
            print(j, end='')
        print()
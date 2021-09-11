a = int(input())
a_1 = 0
a_2 = 0
for i in range(3, a, 3):
    a_1 += i
for i in range(5, a, 5):
    if i % 3 != 0:
        a_1 += i

print(a_1)
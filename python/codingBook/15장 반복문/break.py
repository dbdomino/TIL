for i in range(1, 11):
    print(i)
    if i >= 5:
        break
print('-------------')
for i in range(1, 6):
    for j in range(1,6):
        print(i, j)
        if i == j:
            break
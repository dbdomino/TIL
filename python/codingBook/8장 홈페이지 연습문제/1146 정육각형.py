a = int(input())
sum=1
if a == 1:
    print(sum)
else:
    for i in range(1, a):
        sum += i*6
    print(sum)
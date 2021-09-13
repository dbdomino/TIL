a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(10):
    print(a[i], end=' ')
print('')

n = int(input())
a = []
for _ in range(n):
    a.append(int(input())) # 한줄씩 리스트에 입력하기
for i in range(n):
    print(a[i], end = ' ')

n = int(input())
a = list(map(int, input().split())) # 리스트 형태로 입력하기
for i in range(n):
    print(a[i], end=' ')
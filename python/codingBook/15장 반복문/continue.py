# for에서 continue를 만나면 처음으로 돌아가 in 연산자 앞의변수에 다음 값을 대입한 후 for문 진행
# while에서 continue를 만나면 처음의 조건부로 돌아가 조건이 True이면 while문 진행한다.

for i in range(1, 11):
    if i <= 5:
        continue
    print(i)

a = 0
while a < 11:
    a += 1
    if a <= 5:
        continue
    print('while',a)
# 조건문이나 반복문에서 실행할 코드가 없을 때 사용된다.
# 조건문이나 순환문에서 어떠한 구문도 넣지 않으면 IndentationError가 발생하기 때문에 pass를 넣는다.
# 자바에선 필요없는 기능
# pass넣으면 종료시키는 기능 으로 생각하면 안됀다. 빈공간 채우는 개념으로만 생각하자.

for _ in range(100):
    pass
print('end')
for i in range(1, 10):
    print(i)
    if i > 6:
        print('pass')
        pass

print('end')
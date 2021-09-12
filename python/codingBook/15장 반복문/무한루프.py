# while True:
# while 1:

# 이는 무한루프로써 끝내려면 break 사용해야한다.
maxv = 0
while True: # 입력한 값 중에 최대값 찾기
    a = int(input())
    if a == 0:
        break
    if maxv < a:
        maxv = a
print(maxv)
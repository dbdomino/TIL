# a = input() # 입력된 데이터는 문자열로 저장된다.
# b = input()
# print (a + b)
# print(type(a))
# print(type(b))
# c = int(input()) # 정수로 저장한다.
# d = int(input())
# print(c+d)
# print(type(c))
# print(type(d))
# e = float(input()) # 실수로 저장한다.
# f = float(input())
# print(e + f)
# print(type(e))
# print(type(f))

def inputA():
    a = int(input())
    if ( a > 0 and a <= 100):
        return a
    else:
        print('1부터 100 사이의 정수를 입력하세요')
        a = int(inputA())
        return a

a = int(inputA())
b = int(inputA())
print('a + b = ', a + b)
print('a - b =', a - b)
print('a * b = ', (a * b))
print('a / b =', a / b)
print('a // b = ', (a // b))
print('a % b =', a % b)


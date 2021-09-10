a=10        #정수
b=0b11      #2진수, 대문자 B도 가능 binary
c=0o10      #8진수, 대문자 O도 가능 oxtal
d=0xA       #16진수 대문자 X도 가능 hexa
e=12.34     #부동 소수점
f=12.3e-10  #E 표기법, 대문자 E도 가능
g='EULER'   #문자열
h = 1+2j    #복수수
i = None    # 예약어
print(a, type(a)) # print와 type는 내장함수
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))
j, k = 10, 20
print(j, k)
del(j)
# print(j, k)   에러발생, del(j)로 인해 NameError: name 'j' is not defined
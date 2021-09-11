# 광고 메시지는 C(2≤C≤20) 마리의 소 각각에 공백없이 K(2≤K≤4)개의 문자로 작성하는데
# 소들에게 작성된 K개의 문자로 이루어진 문구(모든 문구는 유일하다.)가 주어지고, 광고 메시지를 만들 수 있는 사전에 있는 가능한 단어들이 주어지면,
# 여러분들은 사전에 있는 단어들로 만들 수 있는 가능한 광고 메시지가 몇 개나 되는지 구하기
# (ABCD EF와 AB CDEF는 서로 다른 광고 메시지로 취급하는 것에 주의하여라.)
# 사전에 있는 단어들은 모두 유일하며 사전에 있는 단어를 두 번 이상 사용하는 경우는 없다.
# 모든 C 마리의 소는 정확하게 한 번만 사용되었다.
# 우리가 구하는 광고 메시지에 문법적 생각은 하지 말고 또한 내용적인 의미도 두지는 말자.

# 첫째 줄에는 세 개의 정수 K, C와 D가 주어진다.(1≤D≤150, D는 사전에 있는 단어의 개수) 둘째 줄부
# D의 단어는 어떠한 단어도 10자를 넘어가지는 않는다.
# 둘째 줄부터는 각각의 소들에게 작성된 K개의 문자로 이루어진 문자열이 C개의 줄에 걸쳐서 주어진다.
# 둘째줄부터 C개, D개 만큼 앤터로 입력

# 가능한 광고 메시지 중에서 (사전순으로 가장 빠른) -> (아스키코드 값이 적은거?) 광고 메시지를 첫째 줄에 출력하여라.
# 메시지 "A B"는 사전순으로 "AB"와 같다는 것에 주의하여라.
# 둘째 줄에는 사전에 있는 단어들로 가능한 광고 메시지의 경우의 수를 출력하여라.

# 사전에 있는 단어들로 만들 수 있는 6개의 광고 메시지 :
# TEN ATTACK BARN AT, TEN BARN AT ATTACK, ATTACK TEN BARN AT, ATTACK BARN AT TEN,
# BARN AT TEN ATTACK, BARN AT ATTACK TEN

K, C, D = map(int, input().split())
Clist = []
Dlist = []
for i in range(C):
    Clist.append(input())
for i in range(D):
    Dlist.append(input())

if "ATT" in 'ATTACK':
    print("Found world")
else:
    print("Not found world")
# print(K,C,D)
# print(Clist)
# print(Dlist)


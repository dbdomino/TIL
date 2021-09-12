# for i in range(5):
#     for j in range(10):
#         print('i=',i,'  j=',j)

for i in range(1, 6):
    print(' '*(5-i)+'$'*i)

for i in range(5,0,-1):
    print(' '*(5-i)+'#'*i)
print('')
for i in range(1, 6):
    print(' '*(5-i)+'$'*i+'$'*(i-1))
for i in range(5,0,-1):
    print(' '*(5-i)+'#'*i+'#'*(i-1))
#
# 5：输出99乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'  .format(j,i,i*j),end=' ')
    print(' ')

for i in range(1,10):
    for j in range(i,10):
        print('{}*{}={}'  .format(j,i,i*j),end=' ')
    print(' ')
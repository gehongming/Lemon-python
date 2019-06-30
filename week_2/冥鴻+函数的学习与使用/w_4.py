# 4:利用Python代码画出直角三角形以及等边三角形，如下所示：
#
for i in range(6):
        print('* '*i)



for i in  range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    print('* '*i)
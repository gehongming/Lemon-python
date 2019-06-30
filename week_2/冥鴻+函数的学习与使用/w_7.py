

# 7：有1 2 3 4 这四个数字，能组成多少个互不相同且无重复数字的三位数？分别是什么？abc a!=b!=c

i=0
for x in range (1,5):
    for y in  range (1,5):
        for z in range (1,5):
            if x!=y and x!=z and y!=z:
                i+=1
                if i%3:
                    print('{}{}{}'.format(x,y,z),end=' | ')
                else:
                    print('{}{}{}'.format(x, y, z))

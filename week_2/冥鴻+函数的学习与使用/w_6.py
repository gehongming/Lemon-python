#
# 6：经典冒泡算法： 利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序： 冒泡排序：小的排前面，大的排后面。
a=[1,7,4,89,34,2]

n=len(a)
for i in range(0,n-1):
    for j in range(0, n-i-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
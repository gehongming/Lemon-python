# 请利用上课所学知识，把txt里面的两行内容，写一个函数，返回如下格式的数据：
# [{'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/register','mobile':'18688773467','pwd':'123456'},
# {'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge','mobile':'18688773467','amount':'1000'}]
# 请自行copy数据到Python里面，进行完整的分析后，再进行程序的编写！！！！
# 多思考多讨论！

file=open('ghm.txt') #打开文件
a=file.readlines()    #读取数据
g=[]   #空列表
for i in a:         #遍历所有字符
    # print(i)
    c=i.strip('\n').split('@')   #去除空格，以及对@进行切割
    # print(c)
    dict={} #定义一个空字典


    for j in c:
            # print(j)
        d=j.split(':',1) #j用 ：分割一次
            # print(d)
        dict[d[0]]=d[1]  #增加键值对到字典
    g.append(dict)
print(g)









# d={"name":'华华',
#    'hobby':'学Python',
#    'age':18,
#    'score':{'en':120,'math':99.99,'ch':'A'},
#    'friend':['bay max','小CC','如意'],
#    True:'good_man', 0.02:'python',
#    False:'这个value对应的key是布尔值',
#    (1,2,3):'我就是元组大大！！！',
#    0:'这是真爱呀', 1:'socre is 99.9'}
#
# print(d)


# 现象：key值为 True False 所对应的value值不是字典内的原有的。 key值为0 和1 没有在控制台输出
# 原因：True False为布尔值 分表为1 0 与原有的0 1 重复了。所以key为 0 1没有输出到控制台
# 因为字符串是可以修改的，所以下方的0 1 的value值覆盖了 原本 True False 的value值

# 3：拓展：利用input函数（自行去拓展该函数的用法），获取一个日期，
# 日期格式如下所示：20190216，然后针对输入的这个日期，进行一些处理后，输出：2019年2月16日   这个字符串到控制台
# year=input('请输入年份：')
# month=input('请输入月份:',)
# day=input('请输入日期：')
# print('{}年{}月{}日'.format(year,month,day))
# print('%s年%s月%s日'%(year,month,day))
#print(year+'年'+month+'月'+day+'日')

# data=input('请输入日期：')
# print('{}年{}月{}日'.format(data[0:4:1],data[5:6:1],data[6::]))
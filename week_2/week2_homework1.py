# 1.根据你输入的数据，来进行判断学生的成绩。输入数据函数：input()
# score=int(input('请输入学生成绩:'))
# if score>=90:
#     print('A')
# elif score>=80:
#     print('B')
# elif score>=70:
#     print('C')
# elif score>=60:
#     print('D')
# else:
#     print('E')

# 2、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
# 如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格
# money=int(input('请输入购买的商品金额：'))
# if money<50 :
#     print('至少再够买',100-int(money),'元,方可优惠,您需付款',money,'元')
# elif money<=100:
#     print('亲爱的顾客您可享受优惠优惠10%,您需付款为:',int(money)*0.8,'元')
# else:
#     print('亲爱的顾客您可享受商品优惠20%,您需付款为:',int(money)*0.9,'元')


# 3、输入一个数，判断一个数n能同时被3和5整除

# a=int(input('请输入整数：'))
# if int(a)%5==0 and int(a)%3==0:
#     print('恭喜你中奖了')
# else:
#     print('请继续努力')
# 4、输入一个年份，输出是否为闰年，闰年条件：能被4整除但不能被100整除，或者能被400整除的年份都是闰年

# year=int(input('请输入一个年份：'))
# if int(year)%4==0 and int(year)%100!=0:
#     print('您输入的是闰年')
# elif int(year)%400==0:
#     print('您输入的是闰年')
# else:
#     print('您输入的是平年')


# 5、一个 5 位数，判断它是不是回文数。即 12321 是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息。01210

# x = input('请输入一个5位数：')
# if x[0]=='0':
#     print('请输入正确的五位数')
# elif len(x)!=5 :
#     print('请输入正确的五位数')
# else  x[0] == x[4] and x[1] == x[3]:
#     print(x,'是个回文数')


# 6、利用random函数生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则打印bigger。小了，则打印less。如果相等，则打印equal

# import random
# d=random.randint(1, 9)
#
# f=int(input('请输入一个整数:'))
# if int(f)>d:
#     print('bigger')
# elif  int(f)==d:
#     print('equal')
# else:
#     print('less')




# 拓展题：
# 登录功能：用户名和密码存在{'name':'huahua','pwd':'123456'}字典中，通过控制台输入用户名和密码判读是否正确，然后给出对应的提示消息：登录成功 OR 用户名或密码错误

p={'name':'huahua','pwd':'123456'}

a=input('请输入用户名：')
b=input('请输入密码：')

if a==p['name'] and b==p['pwd']:
    print('登陆成功')
elif a!=p['name'] and b==p['pwd']:
    print('用户名错误')
elif a==p['name'] and b!=p['pwd']:
    print('密码错误')
else:
    print('账号不存在')
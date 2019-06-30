#__author__="G"
#date: 2019/3/9

# 2:写一个子类，继承1 这个父类，且添加函数：discount 打折扣用的
# pay_money 支付餐费用，重写 open_restaurant() ，并完成子类完成调用
# 至于怎么做？可以自由发散，另0307的第一题不用做了，做这一题就OK！

from  w_1 import Reataurnt  #调用
class Reataurnt_1(Reataurnt): #创建子类
    def discount(self):        #打折
        print('新店大促销：满100-20，满200-50。欢迎来{}品尝'.format(self.restaurrnt_name))
    def pay_money(self,money):
        # self.money=money
        if money<100 :
            print('至少再够买',100-int(money),'元,方可优惠,您需付款',money,'元')
        elif money<=200:
            print('亲爱的顾客您可享受优惠优惠满200-20,您需付款为:',int(money)-20,'元')
        else:
            print('亲爱的顾客您可享受商品优惠满200-50,您需付款为:',int(money)-50,'元')
    def open_restaurant(self):
        print('欢迎光临，',self.restaurrnt_name,'本店正在营业')

if __name__=='__main__':
    WOP=Reataurnt_1('小福贵菜馆','满汉全席')
    WOP.describe_restaurant()
    WOP.open_restaurant()
    WOP.discount()
    WOP.pay_money(400)







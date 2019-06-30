#__author__="G"
#date: 2019/3/9、

# 1：创建一个名为 Restaurant 的类，其方法 init ()设置两个属性：
# restaurant_name 和 cooking_type。创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，
# 其中前者打印前述两项信息，而后者打印一条消息， 指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

class Reataurnt:

    def __init__(self,restaurrnt_name,cooking_type):
        self.restaurrnt_name=restaurrnt_name
        self.cooking_type=cooking_type

    def describe_restaurant(self):
        print(self.restaurrnt_name,self.cooking_type)


    def open_restaurant(self):
        print(self.restaurrnt_name,'is opening')

if __name__=='__main__':
    restaurant=Reataurnt('小福贵菜馆','满汉全席')
    # restaurant.init('小福贵菜馆','满汉全席')
    print(restaurant.restaurrnt_name)
    print(restaurant.cooking_type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
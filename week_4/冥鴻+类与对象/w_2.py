# 2:建一个名为 User 的类，
# 其中包含属性 first_name 和 last_name，
# 还有用户简介通常会存储的其他几个属性。
# 在类 User 中定义一个名为 describe_user()的方法，
# 它打印用户信息摘要；再定义一个名为 greet_user()的方法，它向用户发出个性化的问候。
#
#
# class User:
#     first_name='冥'
#     last_name='鴻'
#     sex='man'
#     height='170'
#     weight='120'
#
#     def describe_user(self):
#         print(''' first_name:{},
#                 last_name:{},
#                 sex:{}
#                 weigt:{}，
#                 height:{}，'''.format(self.first_name,self.last_name,self.sex,self.height,self.weight))
#     def greet_user(self):
#         print('伟大的魔王,{}{}sama,欢迎您的到来!!!!!!'.format(self.first_name,self.last_name))
#
# x=User()
# x.describe_user()
# x.greet_user()


#
class User:
    # first_name='冥'
    # last_name='鴻'
    # sex='man'
    # height='170'
    # weight='120'
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print('无奈黑暗大帝{}{}，君临天下，无人能及，宇宙的毁灭者'.format(self.first_name,self.last_name,))
    def greet_user(self):
        print('伟大的魔王,{}{}sama,欢迎您的到来!!!!!!'.format(self.first_name,self.last_name))

x=User('冥','鸿')
x.describe_user()
x.greet_user()
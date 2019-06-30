# 如题。利用configParser类来实现自己的功能封装。
# 可参考课堂上的类定义。也可以再扩展。
from configparser import ConfigParser
class w_1:

    def __init__(self,conf_filePath,encoding='utf-8'):
        self.cf=ConfigParser()
        self.cf.read(conf_filePath,encoding)
    #获取整数
    def get_intvalue(self,section,option):
        return self.cf.getint(section,option)
    #获取字符串
    def get_value(self,section,option):
        return self.cf.get(section,option)
    #获取字符串
    def get_floatvalue(self,section,option):
        return self.cf.getfloat(section,option)
    #获取布尔值
    def get_boolvalue(self,section,option):
        return self.cf.getboolean(section,option)
    #获取section
    def get_sections(self):
        return self.cf.sections()
    #获取option
    def get_option(self,section):
        return self.cf.options(section)

if __name__=='__main__':
    a=w_1('mh.cfg')
    q=a.get_sections()
    print(q)
    e=a.get_option('sds')
    print(e)
    f=a.get_value('sds','sds_sex')
    print(f)


#写一个日志类
#结合配置文件 完成 输出的格式  输出的级别的配置


import  logging
# from configparser import ConfigParser
from config import w_1
class w_logging:
    def __init__(self,file_name,log_name):
        self.file_name=file_name
        self.log_name=log_name
        #新建收集器
    def shouji(self):
        # cf = ConfigParser()
        # cf.read('w_1.cfg', encoding='utf-8')
        # level = cf.get('GS','Level')
        # a = cf.get('GS', 'asctime')
        # f= cf.get('GS', 'filename')
        # l= cf.get('GS', 'levelname')
        # m= cf.get('GS', 'message')
        level=w_1('w_1.cfg').get_value('GS','Level')
        a=w_1('w_1.cfg').get_value('GS','asctime')
        f=w_1('w_1.cfg').get_value('GS','filename')
        l=w_1('w_1.cfg').get_value('GS','levelname')
        m=w_1('w_1.cfg').get_value('GS','message')
        my_logger=logging.getLogger(self.log_name) #定义日志收集器
        my_logger.setLevel(level)#d定义收集的级别
        #指定格式
        fmt=logging.Formatter('%({})s-%({})s-%({})s-日志信息:%({})s'.format(a,f,l,m))
        #新建指定的输出渠道
        ch=logging.StreamHandler()#输出到控制台
        ch.setLevel(level)#定义输出信息的级别
        ch.setFormatter(fmt)#输出格式
        #新建指定的文本输出渠道
        file_handle=logging.FileHandler(self.log_name,encoding='utf-8')#输出到指定文件
        file_handle.setLevel(level)
        file_handle.setFormatter(fmt)
        my_logger.addHandler(ch)
        my_logger.addHandler(file_handle)
        #s收集日志
        my_logger.debug('hahah')
        my_logger.info('haha')
        my_logger.warning('hahaa')
        my_logger.error('ahaha')
        my_logger.critical('ahahahaa')
if __name__=='__main__':
    a=w_logging('py15','py15.log')

    a.shouji()




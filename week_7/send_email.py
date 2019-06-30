import smtplib
from conf import emailname, emailpwd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication #发送附件

class SendEmail():
    def __init__(self,sendemail,sendfile,raw):
        self.sendemaile=sendemail
        self.sendfile=sendfile
        self.raw=raw

    def E_maile (self):   # 总的邮件内容，分为不同的模块
        msg_total = MIMEMultipart()
        msg_total['Subject'] = 'hello'

        # 正文模块
        msg_raw = '<p style="color:red">{}</p>'  .format(self.raw)

        msg = MIMEText(msg_raw, 'html')
        msg_total.attach(msg)

        # 附件模块
        mfile = MIMEApplication(open(self.sendfile, 'rb').read())
        # 添加附件的头信息
        mfile.add_header('Content-Disposition', 'attachment', filename=self.sendfile)
        # 附件摸快添加到总的里面
        msg_total.attach(mfile)

        with smtplib.SMTP_SSL('smtp.163.com', 465) as server:
            # 登录
            try:
                server.login(emailname, emailpwd)
                msg = '''\\
                From: yuze
                Subject: test()
            
                This is a test'''

                # 发送邮件
                server.sendmail(emailname,self.sendemaile, msg_total.as_string())
            except Exception:
                print('发送失败')

if __name__ == '__main__':
    a=SendEmail('17625188013@163.com','test3.html','你好，葛红明，你会走好运的，会找到另一半的，完成了')
    a.E_maile()
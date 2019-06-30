import ssl
from smtplib import SMTP, SMTP_SSL

from conf import emailname, emailpwd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# 配置各种邮件服务
email_servers = {
    "163.com": {"smtp": {"host": "smtp.163.com", "port": 25, "ssl_port": 465}},
    "qq.com":{}
}

# 创建 ssl context 用于加密
context = ssl.create_default_context()


def parse_mail(mailname):
    """解析邮件名，返回对应的邮件服务商"""
    server_name = mailname.split('@')
    # wayug2163.com
    if len(server_name) == 1:
        raise TypeError('email format error')

    # email: wag@yuze@163.com
    server_name = server_name[-1]

    if server_name not in list(email_servers.keys()):
        raise NameError('No this email server')

    server = email_servers.get(server_name, '')
    return server


class MyMail:
    def __init__(self, mailname, pwd, ssl=True):

        self.mailname = mailname
        server = parse_mail(mailname).get('smtp', '')

        self.server = SMTP(server.get('host'), server.get('port'))

        if ssl == True:

            # TODO SSL
            self.server = SMTP_SSL(server.get('host'), server.get('ssl_port'), context=context)
        else:
            self.server = SMTP(server.get('host'), server.get('port'))

        self.server.login(mailname, pwd)


    def mail_msg(self, msg, type='html', subject=""):
        """组装邮件正文"""
        msg = MIMEText(msg, type)
        msg['Subject'] = subject
        return msg

    def send_mail(self, to, msg, files=None, type='plain', subject=''):
        """发送邮件的主函数。

        :param to : 发送目的地；
        :param msg: 原始邮件数据
        :param files: 发送的附件文件路径
        :param type: 格式类型
        :param subject: 标题
        """
        total = MIMEMultipart()
        total["Subject"] = subject

        body = self.mail_msg(msg, type=type, subject=subject)
        total.attach(body)

        # 这个 files 是一个不为空的列表
        # 判断这个 files 首先不能为空， 不为空的列表
        if files and isinstance(files, list):
            for filename in files:
                file = MIMEApplication(open(filename, 'rb').read())
                file.add_header('Content-Disposition', 'attachment', filename=filename)
                # 附件摸快添加到总的里面
                total.attach(file)

        return self.server.sendmail(self.mailname, to, total.as_string())


if __name__ == '__main__':

    msg = """
    测试为空，
    原因不多讲了。
    你看着办吧。
    """

    mail = MyMail(emailname, emailpwd)
    mail.send_mail('17625188013@163.com', msg, ['demo.txt'], subject="给你小心心")
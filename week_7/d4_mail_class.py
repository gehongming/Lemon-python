import ssl
from smtplib import SMTP, SMTP_SSL

from conf import emailname, emailpwd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 配置各种邮件服务
email_servers = {
    "163.com": {"smtp": {"host": "smtp.163.com", "port": 25, "ssl_port": 465}},
}

# 创建 ssl context 用于加密
context = ssl.create_default_context()


def parse_mail(mailname):
    """解析邮件名，返回对应的邮件服务商"""
    server_name = mailname.split('@')

    if len(server_name) == 1:
        raise TypeError('email format error')

    server_name = server_name[-1]

    if server_name not in list(email_servers.keys()):
        raise NameError('No this email server')

    server = email_servers.get(server_name, '')
    return server


class MyMail(SMTP):
    """邮件处理类"""

    def __init__(self, mailname, pwd):
        self.mailname = mailname
        self.server = parse_mail(mailname).get('smtp', '')
        # 阶级知识
        super().__init__(self.server.get('host'), self.server.get('port'))
        #
        self.login(emailname, pwd)

    # def send_text_mail(self, to, msg, subject=""):
    #     """发送text邮件"""
    #     msg = self.mailname(msg, type='plain', subject=subject)
    #     return self.sendmail(self.mailname, to, msg)
    #
    # def send_html_mail(self, to, html_msg, subject=""):
    #     """发送html邮件"""
    #     msg = self.mailname(html_msg, type='html', subject=subject)
    #     return self.sendmail(self.mailname, to, msg.as_string())

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

        if files and isinstance(files, list):
            for filename in files:
                file = MIMEApplication(open(filename, 'rb').read())
                file.add_header('Content-Disposition', 'attachment', filename=filename)
                # 附件摸快添加到总的里面
                total.attach(file)
        # SMTP
        return self.sendmail(self.mailname, to, total.as_string())


class MyMailSSL(SMTP_SSL, MyMail):
    """SSL的邮件发送"""

    def __init__(self, mail_name, pwd):
        self.mailname = mail_name
        server = parse_mail(mail_name).get('smtp', '')

        # 要使用 SMTP_SSL，而不是 MyMail
        super().__init__(server.get('host'), server.get('ssl_port'))
        super().login(mail_name, pwd)



if __name__ == '__main__':
    #MIMEText
    msg = """
        测试为空，
        原因不多讲了。
        你看着办吧。
        结合一些信息
        """

    with MyMail(emailname, emailpwd) as mail:
        mail.send_mail('17625188013@163.com', msg, ['demo.txt'], subject="测试")



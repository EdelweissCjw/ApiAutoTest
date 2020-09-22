"""sent email"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class SendEmail(object):
    def __init__(self):
        """初始化数据信息"""
        self.sender = '1026221520@qq.com'
        self.pwd = 'ijfhtpxogdxdbfic'
        self.user = 'CJW4818@163.com'
        self.subject = '小程序接口测试运行结果'
        self.content = '接口测试结果查看附件'


    def Email(self):

        msg = MIMEMultipart()   # 初始化发送信息

        # 配置发送人，接收人邮箱地址
        msg['From'] = self.sender
        msg['To'] = self.user
        msg['Subject'] = self.subject

        # 发送信息文本内容
        textApart = MIMEText(self.content)

        # 将测试结果HTML文件添加为邮件附件
        htmlFile = 'ExampleReport.html'
        htmlApart = MIMEApplication(open(htmlFile, 'rb').read())
        htmlApart.add_header('Content-Disposition', 'attachment', filename=htmlFile)

        # 文本内容、附件内容添加到邮件msg中
        msg.attach(textApart)
        msg.attach(htmlApart)

        # 登录发件人邮箱并发送邮件
        try:
            server = smtplib.SMTP_SSL('smtp.qq.com', 465)
            server.login(self.sender, self.pwd)
            server.sendmail(self.sender, self.user, msg.as_string())
            print('报告发送成功')
            server.quit()

        except smtplib.SMTPException as e:
            print('error', e)

    @staticmethod
    def runEmail():
        #  运行发送邮件模块方法
        instance = SendEmail()
        instance.Email()




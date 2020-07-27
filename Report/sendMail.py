"""sent email"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class SendEmail(object):
    def __init__(self):
        self.sender = '1026221520@qq.com'
        self.pwd = 'ijfhtpxogdxdbfic'
        self.user = 'CJW4818@163.com'
        self.subject = '小程序接口测试运行结果'
        self.content = '接口测试结果查看附件'


    def Email(self):

        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = self.user
        msg['Subject'] = self.subject

        textApart = MIMEText(self.content)

        htmlFile = 'ExampleReport.html'
        htmlApart = MIMEApplication(open(htmlFile, 'rb').read())
        htmlApart.add_header('Content-Disposition', 'attachment', filename=htmlFile)

        msg.attach(textApart)
        msg.attach(htmlApart)


        try:
            server = smtplib.SMTP_SSL('smtp.qq.com', 465)
            server.login(self.sender, self.pwd)
            server.sendmail(self.sender, self.user, msg.as_string())
            print('发送成功')
            server.quit()

        except smtplib.SMTPException as e:
            print('error', e)

    @staticmethod
    def runEmail():

        instance = SendEmail()
        instance.Email()




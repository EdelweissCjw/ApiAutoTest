"""Run Project"""

from Report import runTestcase, sendMail


# 运行项目
if __name__ == '__main__':
    runTestcase.RunSuite.RunClass()    # 运行测试用例
    sendMail.SendEmail.runEmail()    # 发送结果
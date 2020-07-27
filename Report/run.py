"""Run Project"""

from Report import runTestcase, sendMail



if __name__ == '__main__':
    runTestcase.RunSuite.RunClass()
    sendMail.SendEmail.runEmail()
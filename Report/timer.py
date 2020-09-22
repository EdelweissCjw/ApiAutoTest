"""定时任务"""
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from Report import runTestcase, sendEmail


def time():
    """
    执行测试用例，发送测试结果
    :return: null
    """
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    runTestcase.RunSuite.RunClass()  # 运行测试用例
    sendEmail.SendEmail.runEmail()  # 发送用例执行结果


scheduler = BlockingScheduler()  # 定时任务方法
scheduler.add_job(time, 'cron', day_of_week='1-5', hour=15, minute=17)   # 执行时间配置
scheduler.start()   # 运行定时任务
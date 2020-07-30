"""定时任务"""
# import sched
# import time
# from datetime import datetime
#
#
# schedule = sched.scheduler(time.time, time.sleep)
#
# def printTime(inc):

#     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     schedule.enter(inc, 0, printTime, (inc,))
#
# def main(inc=60):
#     schedule.enter(0, 0, printTime, (inc,))
#     schedule.run()
#
#
# if __name__ == '__main__':
#     main(10)


from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from Report import runTestcase, sendMail


def time():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    runTestcase.RunSuite.RunClass()  # 运行测试用例
    sendMail.SendEmail.runEmail()  # 发送结果


scheduler = BlockingScheduler()
scheduler.add_job(time, 'cron', day_of_week='1-5', hour=15, minute=17)
scheduler.start()
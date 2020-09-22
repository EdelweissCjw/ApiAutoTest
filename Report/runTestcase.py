"""运行所有的testCase"""
import unittest
import os
from HTMLTestRunner import HTMLTestRunner


class RunSuite(object):

    #初始化参数
    def __init__(self):
        self.suite = unittest.TestSuite()    #初始化测试用例执行集合方法
        self.loader = unittest.TestLoader()   #初始化读取测试用例方法
        self.report = {
            'report_title': 'Example用例执行报告',
            'desc': 'HTMLTestRunner',
            'test_report_path': os.getcwd() + "\ExampleReport.html",    #拼接测试报告地址
            'case_dirs': os.path.abspath(os.path.dirname(os.getcwd())) + '\\testCase'  # 拼接测试用例目录地址
        }



    def Runsuite(self):
        # 通过路径获取所有测试用例集合并加入addtest
        self.suite.addTest(self.loader.discover(self.report['case_dirs']))

        try:

            # 测试结果写入报告模板
            with open(self.report['test_report_path'], "wb") as report:
                runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=self.report['report_title'],
                                                       description=self.report['desc'])
                runner.run(self.suite)  #执行测试用例

        except BaseException as error:
            print(error)


    @staticmethod
    def RunClass():
        """
        调用执行用例方法
        """
        instance = RunSuite()
        instance.Runsuite()


"""getScoreRank接口测试用例"""
import unittest
from Common.baseRequest import ClientApiRequest
import Setting


class GetScoreRank(unittest.TestCase):


    def setUp(self):
        self.module = Setting.module
        self.realName = Setting.realName
        self.content = Setting.content
        self.apiName = 'getScoreRank'
        self.privateData = {'score': '600', 'provinceId': '3'}

    def tearDown(self) -> None:
        pass


    def test_getScoreRank(self):

        result = ClientApiRequest.Request(self, apiName=self.apiName, privateData=self.privateData)
        final = ClientApiRequest.Result(url=result['url'], respon=result['respon'])  # 判断接口请求结果

        if final:
            self.assertNotEqual(final, '数据为空')
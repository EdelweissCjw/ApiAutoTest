"""getBatchByProvinceId"""
import unittest
from Common.baseRequest import ClientApiRequest
import Setting


class GetBatchByProvinceId(unittest.TestCase):


    def setUp(self):
        self.module = Setting.module
        self.realName = Setting.realName
        self.content = Setting.content
        self.apiName = 'province/batch/config/getBatchByProvinceId'
        self.privateData = {'provinceId': '3'}

    def tearDown(self) -> None:
        pass


    def test_getBatchByProvinceId(self):

        result = ClientApiRequest.Request(self, apiName=self.apiName, privateData=self.privateData)
        final = ClientApiRequest.Result(url=result['url'], respon=result['respon'])  # 判断接口请求结果

        if final:
            self.assertNotEqual(final, '数据为空')
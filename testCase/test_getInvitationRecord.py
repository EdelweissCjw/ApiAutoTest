"""getInvitationRecord"""
import unittest
from Apitest.Common.baseRequest import ClientApiRequest
from Apitest import Setting


class GetInvitationRecord(unittest.TestCase):


    def setUp(self):
        self.module = Setting.module
        self.realName = Setting.realName
        self.content = Setting.content
        self.apiName = 'getInvitationRecord'
        self.privateData = {}

    def tearDown(self) -> None:
        pass


    def test_getInvitationRecord(self):

        result = ClientApiRequest.Request(self, apiName=self.apiName, privateData=self.privateData)
        final = ClientApiRequest.Result(url=result['url'], respon=result['respon'])  # 判断接口请求结果

        if final:
            self.assertNotEqual(final, '数据为空')
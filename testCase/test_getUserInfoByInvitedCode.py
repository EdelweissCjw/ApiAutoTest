"""getUserInfoByInvitedCode接口测试用例"""
import unittest
from Common.baseRequest import ClientApiRequest
import Setting


class GetUserInfoByInvitedCode(unittest.TestCase):

    def setUp(self):
        self.module = Setting.module
        self.realName = Setting.realName
        self.content = Setting.content
        self.apiName = 'getUserInfoByInvitedCode'
        self.privateData = {'invitedCode': '12060342'}

    def tearDown(self) -> None:
        pass

    def test_getUserInfoByInvited(self):

        result = ClientApiRequest.Request(self, apiName=self.apiName, privateData=self.privateData)
        final = ClientApiRequest.Result(url=result['url'], respon=result['respon'])  # 判断接口请求结果


        if final:
            self.assertNotEqual(final, '数据为空')
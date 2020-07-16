"""Requests请求封装"""
from urllib import request, parse, error
import json




class ClientApiRequest(object):

    def __init__(self, module, realName, content):
        self.module = module
        self.realName = realName
        self.content = content


    def Request(self, apiName, privateData):
        """
        :param apiName:Api name
        :param privateData:another data
        :return:True or False

        """
        url = self.realName + self.module + "/v1/rest/user/" + apiName

        # 判断接口私有参数
        if privateData:
            self.content.update(privateData)
        data = self.content
        # 参数编码
        data = bytes(parse.urlencode(data), encoding='utf-8')

        # 请求URL
        try:
            respon = request.urlopen(url=url, data=data)

        except error:
            print(error)

        # 接口返回数据格式处理
        respon = respon.read().decode('utf-8')
        respon = json.loads(respon)
        # print(respon)
        result = {
            'respon': respon,
            'url': url
        }
        return result

    # 判断接口请求结果
    @staticmethod   #静态函数标识
    def Result(url, respon):
        if respon['status'] == 200:
            if respon['data']:
                print(url, '请求成功')
            else:
                return '数据为空'
        else:
            print(url, 'errorMessage:'.format(respon['errorMessage']), 'responData:'.format(respon['data']))






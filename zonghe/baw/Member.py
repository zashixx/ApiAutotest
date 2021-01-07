'''
用户模块的接口 ，按模块管理
'''

def register(url,baserequests,data):
    '''
    注册接口
    :param url: 环境数据，比如https：//jy001:8081/
    :param baserequests: BaseRequests 的实例
    :param data: 注册的数据
    :return: 响应
    '''
    url = url +"/futureloan/mvc/api/member/register"
    return baserequests.post(url,data=data)

def list(url,baserequests):
    '''

    :param url:
    :param baserequests:
    :return:
    '''
    url = url+"/futureloan/mvc/api/member/list"
    return baserequests.post(url)


def login(url,baserequests,data):
    url = url + "/futureloan/mvc/api/member/login"
    return baserequests.post(url,data=data)
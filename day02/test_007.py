import requests
import pytest

@pytest.fixture(params=[{"mobilephone":12416237429,"pwd":123456,"regname": ""},
                        {"mobilephone":15232607129,"pwd":123456789112345678,"regname": ""},
                        {"mobilephone":13234452339,"pwd":'',"regname": ""}
                        ,{"mobilephone": "","pwd":85846215,"regname": ""}])

def login_data(request):  #request 是pytest中的关键字 固定写法
    return request.param #通过request.param 返回每一组数据 固定写法
def test_login(login_data):
    url = ("http://192.168.150.222:8081/futureloan/mvc/api/member/register")
    print(f"注册功能，测试数据为：{login_data}")
    r = requests.post(url, data= login_data )
    print(r.text)







# # 验证用户使用合法的手机号、密码，昵称为空，注册成功
# url = ("http://192.168.150.222:8081/futureloan/mvc/api/member/register")
# cs = {"mobilephone": "15006007429", "pwd": "123456", "regname": ""}
# r = requests.post(url, data=cs)
# print(r.text)
# assert r.json()['code'] == '10001'
#
# # 验证用户使用合法的手机号、密码、昵称，注册成功
#
# url = ("http://192.168.150.222:8081/futureloan/mvc/api/member/register")
# cs = {"mobilephone": "15006007129", "pwd": "123456789112345678", "regname": ""}
# r = requests.post(url, data=cs)
# print(r.text)
# assert r.json()['code'] == '10001'
#
# # 验证用户使用合法的手机号码，昵称、密码为空，注册失败
# url = ("http://192.168.150.222:8081/futureloan/mvc/api/member/register")
# cs = {"mobilephone": "15006007439", "pwd": "", "regname": ""}
# r = requests.post(url, data=cs)
# print(r.text)
# assert r.json()['code'] == '20103'
#
# # 验证用户手机号码、昵称为空，密码合法，注册失败
# url = ("http://192.168.150.222:8081/futureloan/mvc/api/member/register")
# cs = {"mobilephone": "", "pwd": "85846215", "regname": ""}
# r = requests.post(url, data=cs)
# print(r.text)
# assert r.json()['code'] == '20103'
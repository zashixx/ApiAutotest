'''
1 文件以test_开头
2 测试类以Test开头
3 测试函数
'''

import requests

url = ("http://192.168.150.222:8081/futureloan/mvc/api/member/register")

def test_regsiter_001():
    cs = {"mobilephone": "15006107429", "pwd": "123456"}
    r = requests.post(url, data=cs)
    print(r.text)
    assert r.json()['code'] == '20110'

def test_regsiter_002():
    cs = {"mobilephone": "15006327429", "pwd": "12345"}
    r = requests.post(url, data=cs)
    print(r.text)
    assert r.json()['msg'] == '密码长度必须为6~18'

def test_regsiter_003():
    cs = {"mobilephone": "15002307429"}
    r = requests.post(url, data=cs)
    print(r.text)
    assert r.json()['msg'] == '密码不能为空'

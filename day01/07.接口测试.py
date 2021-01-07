import requests

# 验证用户使用合法的手机号、密码，昵称为空，注册成功
url = ("http://192.168.150.222:8081/futureloan/mvc/api/member/register")
cs = {"mobilephone": "15006007429", "pwd": "123456", "regname": ""}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['code'] == '10001'

# 验证用户使用合法的手机号、密码、昵称，注册成功

url = ("http://192.168.150.222:8081/futureloan/mvc/api/member/register")
cs = {"mobilephone": "15006007129", "pwd": "123456789112345678", "regname": ""}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['code'] == '10001'

# 验证用户使用合法的手机号码，昵称、密码为空，注册失败
url = ("http://192.168.150.222:8081/futureloan/mvc/api/member/register")
cs = {"mobilephone": "15006007439", "pwd": "", "regname": ""}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['code'] == '20103'

# 验证用户手机号码、昵称为空，密码合法，注册失败
url = ("http://192.168.150.222:8081/futureloan/mvc/api/member/register")
cs = {"mobilephone": "", "pwd": "85846215", "regname": ""}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['code'] == '20103'
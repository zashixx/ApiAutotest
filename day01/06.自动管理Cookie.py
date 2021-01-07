'''
自动管理Cookie
requests中的Session类，能够自动获取和管理cookie
'''
import requests
# 新建一个session
s = requests.session()



# 登录接口 login
# 使用 session 发送请求
loginData = {"account":"2780487875@qq.com","password":"qq2780487875"}
r = s.post("https://www.bagevent.com/user/login",data=loginData)
print(r.text)

# dashboard 接口
r = s.get("https://www.bagevent.com/account/dashboard")
print(r.text)

# 退出登录 logout
r = s.get("https://www.bagevent.com/user/login_out")
print(r.text)

print("退出登录之后的Cookie：",s.cookies)

#RequestsCookieJar转成字典
d = requests.utils.dict_from_cookiejar(s.cookies)
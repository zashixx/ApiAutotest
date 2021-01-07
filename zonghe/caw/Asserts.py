'''
断言
'''
import pytest_check as ck

def check(r_json,expect,keys):
    '''
    效验 r_json与expect中，相应的key对应的value是否相同
    :param r_json: 实际的响应结果 r.json()
    :param expect:预期结果
    :param keys: 效验的key列表 ，用逗号分隔：code,msg,status
    :return:
    '''
    ks = keys.split(",")
    for k in ks:  #遍历key
        real = r_json[k]  #根据key 取r_jsin中的value
        exp = expect[k]  #根据key 器expect中的value
        try:
            # assert str(real) == str(exp)
            ck.equal(str(real),str(exp))

        except Exception as e:
            print(f"响应信息：{r_json}，预期结果：{expect}，效验{k}失败")
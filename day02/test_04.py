'''
测试前置 和后置：fixture 的方式（用的比较多的方式）
1 命名比较灵活，不用setup、teardown 这种固定命名
2 使用方便 跨文件使用时 不用import
'''
import pytest

#在普通的函数上增加fixture的注解表示是测试前置
@pytest.fixture()
def login():
    print("登陆系统")
    yield  #yield 之前的是前置 之后的是后置
    print("退出登陆")

#autouse=True 测试用例自动使用。
@pytest.fixture(autouse=True)
def data():
    print("准备测试数据")

def test_query():
    print("测试查询功能，不需要用户登陆")

def test_add(login): #作为参数使用
    print("测试添加的功能，需要登陆")

@pytest.mark.usefixtures('login')#在需要使用前置的地方，使用usefixtures注解。
def test_delete():
    print("测试删除的功能，需要登陆")
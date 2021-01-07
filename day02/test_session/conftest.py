'''
fixture 作用域为session 级别时 ，
1 公共的方法放到conftest.py文件中
2 “pytest” 是根据文件名字找到这些方法的，不需要import。
3 整个执行过程 测试前置和后置执行一次
4 conftest.py 一个工程可以存多个，对所在目录及子目录生效
'''

import pytest
#测试前置和后置
@pytest.fixture(scope='session')
def login():
    print("登陆系统")
    yield
    print("退出系统")
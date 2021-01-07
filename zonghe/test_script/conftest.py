'''
脚本层的一些公共方法
######################################################
'''

'''
python 导入包的规则：
1 从安装目录找包
2 如果使用IDE，从IDE工程的根目录找包，向下搜索

3 命令行执行的时候 没有工程的概念，
所以会以当前执行的py文件开始 向下搜索包
解决办法：把工程路径放到 sys.path中
'''
import pytest
import sys
import os
from zonghe.caw import DataRead
from zonghe.caw.BaseRequests import BaseRequests
########################################################################
print(sys.path)
cp = os.path.realpath(__file__)
cd = os.path.realpath(cp)
cd = os.path.realpath(cd)
cd = os.path.realpath(cd)
sys.path.append(cd)
print(cd)
###########################################################

env_path = r"data_env\env.ini"

@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini(env_path,"url")

@pytest.fixture(scope='session')
def db():
    return eval(DataRead.read_ini(env_path,"db"))

#创建一个BaseRequests的实例 设置session级别的 整个执行过程只有一个实例，自动管理Cookies
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()
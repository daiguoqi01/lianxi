import pytest
@pytest.fixture(scope="module",autouse=True)
def start(request):
    print("开始执行module")
    #print("module  :%s" %request.module._name_)
    print("启动浏览器")
    yield
    print("结束测试")

@pytest.fixture(scope="function",autouse=True)
def open_home(request):
    #print("function  :%s\n返回首页" % request.function._name_)
    print("lele")


class Test_aa:
    def test1(self):
        print("用例1")

    def test2(self):
        print("用例2")


'''设置autouse=True
autouse设置为True，自动调用fixture功能
●start设置scope为module级别，在当前.py用例模块只执行一次，autouse=True自动使用
●open_home设置scope为function级别，每个用例前都调用一次，自动使用'''
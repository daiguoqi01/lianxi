import pytest

@pytest.fixture()       #如果fixture传参scope="module，则相当于setup_module,只会所有用例开始前只执行一次，前提只每个模块都调用了login
def login():            #如果fixture未传参，则相当于setup_function,每个用例开始之前都会执行
    print("输入账号和密码登录")

def test_01():
    print("登录后的其他操作1")


def test_02(login):
    print("登录后的其他操作2")

def test_03(login):
    print("登录后的其他操作3")


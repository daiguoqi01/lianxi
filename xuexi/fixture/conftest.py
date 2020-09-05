import pytest




'''@pytest.fixture()是装饰login的，以方便其他py文件中的函数调用,
但前提是被调用py文件必须命名为conftest,且要运行的用例要在同一个pakage里边'''
@pytest.fixture()     #如果fixture传参scope="module"，则相当于setup_module,只会所有用例开始前只执行一次，前提只每个模块都调用了login
def login():         #如果fixture未传参，则相当于setup_function,每个用例开始之前都会执行
    print("输入账号和密码进行登录")


'''如果在fixture里边断言失败了就是error,如果实在test的用例里边断言失败了就是failed(失败的用例)'''

@pytest.fixture(scope="module")
def user():
    print("用户名")
    a="guoqi"
    #assert a=="guo"
    return a

def test_1(user):
    assert user=="guoq"




import pytest


@pytest.fixture(scope="module")   #如果fixture传参scope="module，则相当于setup_module,只会所有用例开始前只执行一次，前提只每个模块都调用了login
def login():                        #如果fixture未传参，则相当于setup_function,每个用例开始之前都会执行
    print("登录打开浏览器")

    yield                          #yield 相当于teardwon，如果其中一个用例出现异常，不影响yield后面的teardwon执行，并且全部用例执行完毕后yield 呼唤teardown
    print("执行teardwon！")
    print("退出出浏览器")

def test_01(login):
    print("输出第一条用例")



def test_02(login):
    print("输出第二条用例")


def test_03(login):
    print("第三条用例")




if __name__ == '__main__':
    pytest.main("-s","fixture2.py")


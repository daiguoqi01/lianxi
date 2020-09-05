import pytest

@pytest.fixture()
def user():
    print("用户名")
    a = "guoqi"
    pwd="小明"
    # assert a=="guo"
    return a,pwd

def test_1(user):
    u=user[0]
    p=user[1]
    print(u,p)
    assert p=="小明"





@pytest.fixture()
def usr():
    c="honghong"
    return c

@pytest.fixture()
def pwd():
    p=123456
    return p

def test2(usr,pwd):
    zhanghu=usr
    mima=pwd

    print(zhanghu,mima)



@pytest.fixture()
def farss():
    d="记事本"

    return d

@pytest.fixture()
def two(farss):
    f=farss
    e=123456
    return f,e

def test_4(two):
    print("测试账号：%s 密码：%s"  % (two[0],two[1]))


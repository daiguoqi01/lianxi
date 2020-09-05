import pytest
import requests

test_user=["yujiao@mmears.com","bonny@mmears.com"]
test_pwd=["eXVqaWFvMTIzNDU2","bW1lYXJzMjAxNg=="]
test_code=["123456"]

@pytest.fixture(scope="module")
def input_user(request):
    user=request.param
    print("登录账户: %s" %user)
    return user

@pytest.fixture(scope="module")
def input_pwd(request):
    pwd = request.param
    print("登录密码：%s" %pwd)
    return pwd

@pytest.fixture(scope="module")
def input_code(request):
    code = request.param
    print("登录密码：%s" % code)
    return code

@pytest.mark.parametrize("input_user",test_user,indirect=True)
@pytest.mark.parametrize("input_pwd",test_pwd,indirect=True)
@pytest.mark.parametrize("input_code",test_code,indirect=True)
def test_login(input_user,input_pwd,input_code):
    url="https://apistaging.mmears.com/auth/login"
    data={
        "code": input_code,
        "email": input_user,
        "password": input_pwd
    }

    res=requests.post(url=url,data=data).json()
    print(res)
    #assert res["code"]=="OK","正确的值应该是:%s"%res
    print(res)
    #assert res

import pytest
import requests

canshu=[{"user":"yujiao@mmears.com","password":"eXVqaWFvMTIzNDU2","code":111111},
        {"user":"bonny@mmears.com","password":"bW1lYXJzMjAxNg==","code":111111}
        ]

canshu1=[("yujiao@mmears.com","eXVqaWFvMTIzNDU2",111111),
        ("bonny@mmears.com","bW1lYXJzMjAxNg==",111111)

        ]
@pytest.fixture(scope="function")
def login(request):
    user=request.param["user"]
    password=request.param["password"]
    code=request.param["code"]
    print("正在登录，账号%s,密码%s,验证码%s:"%(user,password,code))
    url = "https://apistaging.mmears.com/auth/login"
    data = {
        "code": code,
        "email": user,
        "password": password
    }
    res = requests.post(url=url, data=data).json()
    print(res)
    return res



@pytest.mark.parametrize("login", canshu, indirect=True)  # indirect=True声名login为函数
class Test_XX():

    def test1(self,login):
      a=login
      #assert a,"验证码错误"
      assert a["code"]=="OK","正确的值应该是:%s" % a["code"]

    def test2(self,login):
      a = login
      # assert a,"验证码错误"
      assert a["code"] == "OK", "正确的值应该是:%s" % a["code"]






        # result=login
        # print("用例1 %s"%result)
        # assert result==True



    # def test2(self,login):
    #     result=login
    #     print("用例2 %s"%result)
    #     if not result:
    #         pytest.xfail("登录不成功")
    #     assert 1==1
    #
    #
    # def test3(self,login):
    #     result=login
    #     print("用例3 %s"%result)
    #     if not result:
    #         pytest.xfail("登录不成功")    #pytest.xfail用例a(这里的a依赖用例）不成功则跳过b和c
    #     assert 1==1



if __name__ == '__main__':
    pytest.main(["-s","login_test.py"])








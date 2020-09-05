import pytest,requests


canshu=[("yujiao@mmears.com","eXVqaWFvMTIzNDU2",111111),
        ("bonny@mmears.com","bW1lYXJzMjAxNg==",111111)

        ]
@pytest.mark.parametrize("user,pwd,code",canshu)
def test_login(user,pwd,code):
    url = "https://apistaging.mmears.com/auth/login"
    data = {
        "email": user,
        "password": pwd,
        "code": code
    }
    res = requests.post(url=url, data=data).json()
    print(res)
    return res


@pytest.mark.parametrize("user,pwd,code",canshu)
def test_login1(user,pwd,code):
    a=test_login(user,pwd,code)


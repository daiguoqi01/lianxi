import requests,pytest,json
import random,base64

s=requests.session()

@pytest.fixture(scope="module",autouse=True)   #如果autouse=True，则test用例不用传header，autouse=True默认test开头的用例都会传header
def header():
    url = "https://apistaging.mmears.com/auth/login"
    pwd = "yujiao123456"

    '''将密码转码并加密'''
    pw = pwd.encode()
    password = base64.b64encode(pw)
    print(password)

    poday = {
        "email": "shuyonghao@mmears.com",
        "password": password,
        "code": 123456,
    }

    # '''登录并获取token'''
    res = s.post(url=url, data=poday).json()
    token = res["data"]["token"]
    print(token)

    # '''将token写入到header中'''
    h = {
        "x-app-id": "1",
        "x-auth-token": token
    }
    # g=s.token=token
    # print(g)
    '''保存token到session会话，并更新headers并保持会话'''
    s.headers.update(h)



def chuangjian(**kwargs):
    url="https://apistaging.mmears.com/customer/studentocean/savestudent"
    body={
        **kwargs
    }

    # header = {
    #     "x-app-id": "1",
    #     "x-auth-token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI4OTkiLCJuYW1lIjoi5p2f5rC46LGqIiwic3VwcG9ydElkIjpudWxsLCJleHAiOjE1OTIxMTgyMDAsImlhdCI6MTU5MjAzMTgwMCwiZW1haWwiOiJzaHV5b25naGFvQG1tZWFycy5jb20ifQ.NLJkXReGxU63fsctmnapF-ZdNFJJImzT5NOaALZo7006DHsO0cC_I_j6NlfJqmiB-hrZGc5QAJh5AlNu407mkQ",
    #
    # }

    response = s.post(url=url, json=body).json()
    print(response)
    return response

def test_01():
    # res=chuangjian(gender="UNKNOWN",password="973267",contactPhone="16736973268",nickName="lio",age=6,
    #                month=0,birthDate="2014-05-31T16:00:00.000Z",level=1,unit=201,specialLevel=1,ccId=839,
    #                birthYear="2014",birthMonth="06")
    #a=res["msg"]=="手机号已存在"
    res=chuangjian(**{"gender":"UNKNOWN","password":"973267","contactPhone":"16736973268","nickName":"lio","age":6,
                     "month":0,"birthDate":"2014-05-31T16:00:00.000Z","level":1,"unit":201,"specialLevel":1,"ccId":839,
                    "birthYear":"2014","birthMonth":"06"})
    assert  res["msg"]=="手机号已存在"

def test_02():
    ''' random生成随机手机号'''
    pre_lst = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150",
               "151", "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]
    phone=random.choice(pre_lst) + ''.join(random.sample("0123456789", 8))

    res=chuangjian(gender="UNKNOWN",password="973267",contactPhone=phone,nickName="lio",age=6,month=0,
                   birthDate="2014-05-31T16:00:00.000Z",level=1,unit=201,specialLevel=1,ccId=839,
                   birthYear="2014",birthMonth="06")
    assert res["msg"] ==''

    #assert '手机号已存在' in response
def test_03():
     print("dijf")



def test_04():
    '''水仙花'''
    for i in range(100,1000):
        m = i // 100    #整除获得百位数
        n = (i % 100) // 10        #十位数
        k = i % 10       #个位数
        if m**3 + n ** 3 + k ** 3 == i:
            print(i)


def test_05():
    for i in range(100,1000):
        m=i//100
        #print(m)
        n=(i % 100)//10
        #print(n)
        k=i%10
        #print(k)
        if m**3+n**3+k**3==i:
            print(i)

def test_06():
    a=1
    b=2
    a,b=b,a
    print(a,b)







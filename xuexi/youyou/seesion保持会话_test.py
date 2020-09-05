import requests,base64,random
import pytest

s = requests.session()

url="https://apistaging.mmears.com/auth/login"
pwd="yujiao123456"

'''将密码转码并加密'''
pw=pwd.encode()
password=base64.b64encode(pw)
print(password)

poday={
"email":"shuyonghao@mmears.com",
"password":password,
"code":123456,
}

#'''登录并获取token'''
res=s.post(url=url,data=poday).json()
token=res["data"]["token"]
print(token)

#'''将token写入到header中'''
h={
    "x-app-id": "1",
    "x-auth-token":token
}
#g=s.token=token
#print(g)
'''保存token到session会话，并更新headers并保持会话'''
s.headers.update(h)
print(res)
print(s.headers)


#'''这是session已保持会话，无需再传token'''
pre_lst = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150",
           "151", "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]
phone = random.choice(pre_lst) + ''.join(random.sample("0123456789", 8))

url1="https://apistaging.mmears.com/customer/studentocean/savestudent"
boday1={"gender":"UNKNOWN",
      "password":"973267",
      "contactPhone":phone,
       "nickName":"lio","age":6,
      "month":0,
      "birthDate":"2014-05-31T16:00:00.000Z",
       "level":1,
      "unit":201,
      "specialLevel":1,
      "ccId":839,
      "birthYear":"2014",
      "birthMonth":"06"}
res1=s.post(url=url1,json=boday1).text
print(res1)


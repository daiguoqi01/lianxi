
'''content-type: multipart/form-data; boundary=----WebKitFormBoundary7Q5DU2ybcBiPGPpC'''
import requests,re
'''需先安装pip install requests-toolbelt'''
from requests_toolbelt import MultipartEncoder

from requests_toolbelt import MultipartEncoder
s = requests.session()
#login_xadmin(s)
# 前面先登录
url2 = "http://49.235.92.12:8020/xadmin/hello/teacherman/add/"
r3 = s.get(url2)
# print(r3.text)
token2 = re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r3.text)
print(token2[0])
# multipart/form-data  类型post请求
m = MultipartEncoder(fields=[("csrfmiddlewaretoken", token2[0]),
                             ("csrfmiddlewaretoken", token2[0]),
                             ("teacher_name", "xx44"),
                             ("tel", "xx12"),
                            ("mail", "xx"),
                             ("sex", "M"),
                             ("_save", "xx"),],)
r4 = s.post(url2,data=m,headers={'Content-Type': m.content_type})
print(r4.text)



from requests_toolbelt import MultipartEncoder
m=MultipartEncoder(
                        fields={'field0': 'value',
                       'field1': 'value',
                       'field2': ('filename', open('file.py', 'rb'), 'text/plain')})
r = requests.post('http://httpbin.org/post',data=m,headers={'Content-Type': m.content_type})



from requests_toolbelt import MultipartEncoder
# 先登录
url2 = "http://47.104.190.48:8000/xadmin/hello/fileimage/add/"
r3 = s.get(url2)
# re 知道前面和后面，取中间值
token2 = re.findall('name="csrfmiddlewaretoken" value="(.+?)"', r3.text)
print(token2[0])
# multipart/form-data  类型post请求
m = MultipartEncoder(
        fields=[("csrfmiddlewaretoken", token2[0]),
                ("csrfmiddlewaretoken", token2[0]),
                ("title", "tu2"),
                ("_save", ""),
                ("image", ("tu2.png", open("E:\\test.png", "rb"), "image/png")),
                ("fiels", "")],
                    )
r4 = s.post(url2,data=m,headers={'Content-Type': m.content_type})

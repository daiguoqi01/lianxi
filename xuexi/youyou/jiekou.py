import requests,json,re

url="https://apistaging.mmears.com/customer/studentocean/savestudent"
body={"gender":"UNKNOWN",
      "password":"973267",
      "contactPhone":"16736973268",
       "nickName":"lio","age":6,
      "month":0,
      "birthDate":"2014-05-31T16:00:00.000Z",
       "level":1,
      "unit":201,
      "specialLevel":1,
      "ccId":839,
      "birthYear":"2014",
      "birthMonth":"06"}
# r1=requests.post(url)
# re.findall("'chdhvufd ' valu='(.+?)'",r1.text)    正则表达取某一值
header={
"x-app-id": "1",
"x-auth-token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI4MzkiLCJuYW1lIjoi5YiY6LaFIiwic3VwcG9ydElkIjpudWxsLCJleHAiOjE1OTE4MDMwMjQsImlhdCI6MTU5MTcxNjYyNCwiZW1haWwiOiJsaXVjaGFvQG1tZWFycy5jb20ifQ.OByFlLSOY2USCJOUcln4xGWfYymme0Jo51gLEjrdBldL7cKOTtAk3GAWd87e9if6Vic5qTzUHl6ckh9XkVh4lw"

}


#params=body   当为get请求时参数在urr里边,这时用params=body
'''
另外一部分在body里面

1.第一种：application/json： {“key1“:”value1”,“keyt2":“value2"}
json=
 
2.第二种：application/x-www-form-urlencoded：name1= value1&name2=value2
data=
 
3.第三种：multipart/form-data:这一种是表单格式的
（文件上传 file=，图片上传等混合式）
data=

4. Content-Type:octets/stream
（文件下载） 
data=

5.text/xml
data=
'''

response=requests.post(url=url,json=body,headers=header).text
assert '手机号已存在'  in response
print(response)


res=requests.post(url=url,json=body,headers=header)
json.dumps(res,indent=4,ensure_ascii=False)         #indent=4   是输出的时候容易看，也就是标准的json格式输出，如果没有indent输出的时候看起来是长长的
                                                        #ensure_ascii=False 是将返回的中文（这是的中文为加密的）部分禁止加密
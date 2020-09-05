# import jsonpath,json
# import re,requests
#
# def test1():
#     plody={
#         "code":0,
#         "data":[
#             {"name":"xiaoming",
#              "age":5},
#             {"name":"xiaohei",
#             "age":7 }
#         ]
#     }
#
#     # nam=plody["data"][1]['name']
#     # print(nam)
#     c=json.dumps(plody)          #将返回值转换成json格式
#     #print(c)
#     name=re.findall('"name": "(.+?)"',c)    #正则表达取值
#     #assert name in c
#     print(name)
#
#     b=jsonpath.jsonpath(plody,"$..name")   #jsonpath取值，$..代表的是根目录，也就是相当于 plody中的data，nana是要取的值
#     print(b)
#     #assert b in plody






    # url = "http://web.juhe.cn:8080/constellation/getAll"
    # data = {"key":"cde5e16435cd0217f505a88898b60707",
    #         "consName": "水瓶座,处女座",
    #         "type":" today"}
    # res = requests.get(url,params=data).json()
    # print(res)




import requests,base64,random
import pytest,json,re,jsonpath

def test1():
    s = requests.session()
    url="https://apistaging.mmears.com/auth/login"
    pwd="yujiao123456"

    '''将密码转码并加密'''
    pw=pwd.encode()
    password=base64.b64encode(pw)
    poday={
    "email":"shuyonghao@mmears.com",
    "password":password,
    "code":123456,
    }

    '''登录并获取token'''
    res=s.post(url=url,data=poday).json()
    respones=s.post(url=url,data=poday).json()
    print(respones)


    name=respones["data"]["name"]
    print(name)


    c=json.dumps(res,ensure_ascii=False)          #将返回值转换成json格式

    name=re.findall('"name": "(.+?)"',c)[0]  #正则表达取值
    assert name =="束永豪"
    print(name)

    b=jsonpath.jsonpath(respones,"$..name")[0]   #jsonpath取值，$..代表的是根目录，也就是相当于 respones中的data，name是要取的值
    print(b)
    assert b =="束永豪"



def test2():

    # '''python作业6 - 如何判断一个数组是对称数组：要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对称数组
    # 用Python代码判断，是对称数组打印True，不是打印False, 如：
    # x = [1, "a", 0, "2", 0, "a", 1]'''

    x = [1, "a", 0, "2", 0, "a", 1]
    if x==x[::-1]:                        #将整个列表反转过来看是否相当
        print(True)
    else:
        print(False)


def test3():
    '''python作业5：如果有一个列表a=[1,3,5,7,11],问题：1如何让它反转成[11,7,5,3,1]   2.取到奇数位值的数字，如[1,5,11]'''
    a = [1, 3, 5, 7, 11]
    b=a[::-1]
    c=a[::2]
    print(b)
    print(c)

def test_04():
    '''水仙花'''
    for i in range(100,1000):
        m = i // 100    #整除获得百位数
        n = (i % 100) // 10        #十位数
        k = i % 10       #个位数
        if m**3 + n ** 3 + k ** 3 == i:
            print(i)


def test5():
    '''python作业7-如果一个正整数等于除它本身之外其他所有除数之和，就称之为完全数。
    例如：6是完全数，* 因为6 = 1+2+3；下一个完全数是28 = 14+7+4+2+1。 求1000以下的完全数'''
    for i in range(1,1001):
        s = 0
        for k in range(1,i):
            if i % k == 0:
                s = s + k
        if i == s:
            print(i)



def test6():
    '''python作业8：
    有一个数据list
    of
    dict如下
    a = [
        {"yoyo1": "123456"},
        {"yoyo2": "123456"},
        {"yoyo3": "123456"},
    ]
    写入到本地一个txt文件，内容格式如下：
    yoyo1, 123456
    yoyo2, 123456
    yoyo3, 123456'''
    a = [
        {"yoyo1": "123456"},
        {"yoyo2": "123456"},
        {"yoyo3": "123456"},
    ]
    for i in a:
        for j,k in i.items():      #此时的i为字典
            with open('N_a.txt','a') as fs:   #a是逐行去添加，而不会把之前写入的给清除掉
                fs.write("%s,%s\n"%(j,k))


def test7():
    '''去重并排序'''
    a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
    c = list(set(a))
    c.sort()

    print(c)


def test8():
    '''9x9乘法表'''
    for i in range(1,10):
        for j in range(1,i+1):
            #print(j)
            print(f"{j}*{i}={i*j}",end="\t")     #这一部没整明白，format函数不熟悉
        print("")

def test9():
  a= '{:.2}'.format(1.7878)
  print(a)


def test10():
    '''python作业9：
    已知一个队列, 如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到： [3, 5, 1, 7]'''
    a = [1, 3, 5, 7]

    # insert 插入数据
    a.insert(3, a[0])
    print(a[1:])


def test11():
    '''python作业10：
        已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从 3 开始的每一项都 等于其前两项的和，
        这是斐波那契数列。求满足规律的 100 以内的所以数据'''

    q= 0
    b = 1
    while b < 100:
        print(b, end=",")
        q, b = b, q + b


def test12():
    '''python作业11：
    已知一个字符串为“hello_world_yoyo”, 如何得到一个队列["hello", "world", "yoyo"] '''
    a="hello_world_yoyo"
    c=a.split("_")
    print(c)


def test13():
    '''python作业12：
    统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]'''

    a=[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

    # '''大于0'''
    # for i in a:
    #     if i>0:
    #         print(i)
    #
    # '''小于0'''
    # for i in a:
    #     if i<0:
    #         print(i)

    b = [i for i in a if i > 0]
    print("大于 0 的个数：%s" % len(b))

    b = [i for i in a if i < 0]
    print("小于 0 的个数：%s" % len(b))


'''写一个小程序：控制台输入邮箱地址（格式为 username@companyname.com）， 程序识别用户名和公司名后，将用户名和公司名输出到控制台。 
要求： 
1. 校验输入内容是否符合规范（xx@yy.com）, 如是进入下一步，如否则抛出提 示"incorrect email format"。注意必须以.com 结尾 
2. 可以循环“输入--输出判断结果”这整个过程 
3. 按字母 Q（不区分大小写）退出循环，结束程序 '''
def test14():
    a="username@companyname@com"
    while 1:
        email=input("请输入您的邮箱地址：")
        if email=="Q" or email=="q":
            exit()
        elif re.match(r'[0-9a-zA-Z\_]*@[0-9a-zA-Z]+(\.com)$',email):
            username=re.findall('(.+?)\.com',email)[0]
            company=re.findall('@(.+?)\.com',email)[0]
            print("用户名：%s"%username)
            print("公司名: %s"%company)

        else:
            print("incorrect email format")


def test15():
    '''python作业14：列表生成式
使用列表生成式，将列表中[1, 3, -3, 4, -2, 8, -7, 6],
找出大于0的数，重新生成一个新的列表'''
    s=[]
    a=[1, 3, -3, 4, -2, 8, -7, 6]
    t=[i for i in a if i>0]
    print(t)

def test16():
    '''python面试题14
    L = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
    如何用一行代码得出[11, 1, 2, 3, 5]
    L = [1, 2, 3, 4, 5] ,L[10:]结果是多少?'''
    L = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
    c=L[1:]
    b=set(L)
    print(b)
    print(c)


def test17():
    '''python经典面试题：
给定一个整数数组A及它的大小n，同时给定要查找的元素val，请返回它在数组中的位置(从0开始)，若不存在该元素，返回-1。若该元素出现多次请返回第一个找到的位置'''
    c=[1,2,4,5,6,7,4,1]
    a=9
    if a in c:
        print(c.index(a))
    else:
        print(-1)


def test18():
    '''python经典面试题
两数之和
给定一个整数数组nums 和一个目标值target ，请你在该数组中找出和为目标值的那两个整数，并返回他
们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定nums=[2，7，11，15]，target=9
因为nums[0] + nums[1] =2+7 = 9
所以返回[0， 1]'''

    f=3
    nums = [2,7,11,15]
    target = 9
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j]==target:
                if f==3:
                    f=4
                    print(i,j)




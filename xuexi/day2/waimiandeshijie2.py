import json
from xlutils.copy import copy
f=open("../day2/geci.txt","r+",encoding="utf-8")    #r+既读又能写    w+是写读，不过写读会把之前的内容给清理掉后在写入，而r+不会
#print(f.readline())
f.write("我是大哥""\n")

f.close()


# f2 = open("../day2/geci", "rb")                                              # '''rb是以二进制的方式读'''
# print(f2.readline())
#



f3=open("../day2/geci.json","wb")   #wb是以2进制形式写入
s=json.dumps('我是中国人',ensure_ascii=False)     #ensure_ascii=False 是将中文（这是的中文为二进制）部分禁止加密
f3.write((s).encode())


f3.close()



# f.write("\n""----------of-------------")
#
# f.close()
#


# f=open("../day2/geci","r+",encoding="utf-8")    #r+既读又能写    w+是写读，不过写读会把之前的内容给清理掉后在写入，而r+不会
# print(f.readline())

# f2 = open("../day2/geci", "rb")                                              # '''rb是以二进制的方式读'''
# print(f2.readline())
#
# f3=open("../day2/geci","wb")   #wb是以2进制形式写入
# f3.write("我爱北京填满们".encode())


# f.write('\n'"----------of-------------")
# f.close()

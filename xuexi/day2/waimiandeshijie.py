#coding utf-8
f=open("../day2/geci","r",encoding="utf-8")
print(f.read())
#with open("../day2/geci","r",encoding="utf-8") as fs:
    #print(fs.read())
count=0
for line in f:
    #print(f.read())
    if count==6:
        continue      #跳过本次循环  break终止循环
        #count +=1
    print(line)
    count +=1
print(f.flush())             #flush是刷新




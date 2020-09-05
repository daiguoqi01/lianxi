

names=['xiaohong','xiaoming','xiaoling','xiaoling','wanger']
names.append("zhangsan")      #append是追加的意思，追加的位置在末尾
names.insert(1,'zhangmazi')     #插入数据
names[2]="sorrt"              #改数据
#names.remove('xiaoliang') #删除数据
del names[1]              #删除数据
names.reverse()      #reveres是反转的意思
names.sort()  #排序



print(names.index("wanger"))  #index查找具体位置
print(names[0:3])  #切片
print(names[-2:])  #从右向左切到
print(names[2])
print(names)
print(names[1:5:-1])  #将列表反转
print(names.count('xiaoling'))   #查个数



name2=[1,2,3,4]
names.extend(name2)   #并购,讲name2合并到names上
#a=names+name2
#print(a)
#del name2
print(names)


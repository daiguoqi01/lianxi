import pytest


list1=[1,3,3,4,7,8,6,6,5,4,]
list1=set(list1)               #set集合，集合是去重的

print(list1)             #集合和字典都是无序的

list2=[3,6,8,4]
a=list1.intersection(list2)   #取交际
print(a)
print(list1.union(list2))  #取并集
print(list1.difference(list2))    #差集







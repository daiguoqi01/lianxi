#模拟每个数加前门面几个数的和）（计算列表的和）
a=[1,5,3,6,5,6,7,8,9]
sum=0       #初始值
for i in a:
    sum=sum+i
    print("第%s次循环" % i)
    print(sum)

print('-------------')



#计算所有奇数的和
sum=0
for i in list(range(100)):
    if i % 2:             #  %2 相当于有余数的值只取整数，且为真
        sum=sum+i    #类同于sum +=i
        # if sum>1000:
        #     break

        print(sum)
        #print(sum)


# s=0
# for i in list(range(1,10,2)):
#     s=s+i
#     print(s)
#     #print(i)






# a=len(a)           #len是计算字符串的长度
# print(a)
#
#
#
#
# c=1.7777
# b=2
# d=c+b
#
# print(int(c+b))  #int是取整数
# print(format(d,'.3f'))        #3f 中的3是小数点中的位数
# # c=str(d)
# # print(c[0:3])
#
# print(round(d,2))       #    2是小数点的前两位
#
#
# a=10
# for i in range(2,a):
#     print(i)
#


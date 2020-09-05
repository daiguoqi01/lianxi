#
# for i in range(1,10,2): #2代表隔两个数打印一次
#     print("loop:",i)

# odld=56
# for i in range(3):
#     guess_age=int(input("guess_age:"))
#     if odld==guess_age:
#         print("你猜正确了")
#         break                  #猜对了就破坏这个循环
#     elif guess_age<odld:
#         print("你猜小了")
#     else:
#         print("你猜大了")
# else:
#     print("你只有三次机会")


'''break是结束循环，continue是跳出这个循环继续进行下次循环'''
#
# for j in range(0,10):
#     if j<3:
#         print("loop:",j)
#     else:
#         continue
#     print("hehe..")



a=[2,3,5,4,8]
for i in a[0:-1:2]:
    print(i)
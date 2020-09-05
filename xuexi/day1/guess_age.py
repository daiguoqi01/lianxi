#
#"""while循环"""
# count=0
# while True:
#     print("count:",count)
#     count=count +1
#     if count==1000:
#         break         #破坏循环跳出






odld=56
count=0
# while True:
#     if count==3:        此处的三句话和while count<3一样
#         break
while count<3:
    guess_age = int(input("guess_age:"))
    if odld==guess_age:
        print("你猜正确了")
        break                  #猜对了就破坏这个循环
    elif guess_age<odld:
        print("你猜小了")
    else:
        print("你猜大了")
    count +=1
    if count==3:
        continue_confirm = input("do you want to keep guess..?")
        if continue_confirm != 'n':
            count=0
else:
    print("你只有三次机会")





# odld = 56
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









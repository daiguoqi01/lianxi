
# a=0
# while 1:
#     a=a+1
#     if a>10:
#         break
#     print(a)
#
#
#
# #求100内的奇数的和，当和大于1000时终止循环
# s=0
# i=1
# while i<100:
#     if i % 2:
#         s=s+i
#         #print(s)
#         if s>1000:
#             break
#         print(s)
#     i=i+1            #从1开始循环
#
# print("uuuuuu")
#
# #print(s)
#
# sum=0
# for j in range(100):
#     if j % 2:
#         sum=sum+j
#         if sum>1000:
#             break
#         print(sum)



# def numbers(number):
#     sum=0
#     d=list()
#     for i in range(1,number):#range(1,6)
#         if number%i==0:
#             d.append(i)
#         else:
#             continue
#     for i in d:
#         sum+=i
#     if sum==number:
#         print(number)
#
# for i in range(6,10001):
#     numbers(i)


def numbers(number):
    sum=0
    d=list()
    for i in range(1,number):#range(1,6)
        if number%i==0:
            d.append(i)
        else:
            continue
    for i in d:
        sum+=i
    if sum==number:
        print(number)

for i in range(6,10001):
    numbers(i)

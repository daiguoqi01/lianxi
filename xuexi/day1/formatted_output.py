import getpass
#格式化输出训练



name=input("name:")
age=int(input("age:"))
job=input("job:")
Salary=input("Salary:")



'''fangfa1'''
#%d为整数    %f为浮点型   %s表示格式化一个对象为字符
'''下面的内容是格式化输出的代码'''
info = '''
-----------------info of %s  --------------
name:%s
age:%d                               
job:%s
Salary:%s                                      

''' %(name,name,age,job,Salary)   #第一个name相当于info of %s 中的占位符%s


print(info)


'''fangfa2'''

info1 = '''
-----------------info of {name}  --------------
name:{name}
age:{age}                              
job:{job}
Salary:{Salary}                                     

''' .format(name=name,
           age=age,
           job=job,
           Salary=Salary)

print(info1)


#print(name,age,job,Salary)
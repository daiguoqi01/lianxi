def test(*args):    #*args可以同时传多个参数,转换成元组
    print(args)

test(1,2,3,4,5,6)
test(*[1,2,3,4,5])

def test2(a,*args):
    print(a)
    print(args)
test(1,2,3,4,5,6,7,"小明")



def test3(**kwargs):       #**kwargs是将n个关键字参数转换成字典的方式
    print(kwargs)
    print(kwargs['name'])
test3(name="xiaoming",age=8,xingbie="男")
test3(**{"name":"小明","age":8})


def test4(name,age=18,**kwargs):
    print(name,age,kwargs)

test4(1,xianmging="xiaoliang")
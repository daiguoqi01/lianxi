

'''学过unittest的都知道里面用前置和后置setup和teardown非常好用，在每次用例开始前和结束后都去执行一次。
当然还有更高级一点的setupClass和teardownClass，需配合@classmethod装饰器一起使用，在做selenium自动化的时候，它的效率尤为突出，可以只启动一次浏览器执行多个用例。
pytest框架也有类似于setup和teardown的语法，并且还不止这四个'''

'''用例运行级别
模块级（setup_module/teardown_module）开始于模块始末，全局的

函数级（setup_function/teardown_function）只对函数用例生效（不在类中）

类级（setup_class/teardown_class）只在类中前后运行一次(在类中)

方法级（setup_method/teardown_method）开始于方法始末（在类中）

类里面的（setup/teardown）运行在调用方法的前后

函数式
setup_function/teardown_function
1.pytest框架支持函数和类两种用例方式，先看函数里面的前置与后置用法：

setup_function/teardown_function 每个用例开始和结束调用一次'''

# test_fixt.py

# coding:utf-8
import pytest
# 函数式


def setup_function():
    print("setup_function：每个用例开始前都会执行")

def teardown_function():
    print("teardown_function：每个用例结束后都会执行")

def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x

def test_two():
    print("正在执行----test_two")
    x = "hello"
    assert hasattr(x, 'check')

def test_three():
    print("正在执行----test_three")
    a = "hello"
    b = "hello world"
    assert a in b

# if __name__ == "__main__":
'''pytest.main(["-s", "test_fixt.py"])
运行结果：

============================= test session starts =============================
platform win32 -- Python 3.6.0, pytest-3.6.3, py-1.5.4, pluggy-0.6.0
rootdir: E:\YOYO, inifile:
collected 3 items

test_fixt.py setup_function：每个用例开始前都会执行
正在执行----test_one
.teardown_function：每个用例结束后都会执行
setup_function：每个用例开始前都会执行
正在执行----test_two
Fteardown_function：每个用例结束后都会执行
setup_function：每个用例开始前都会执行
正在执行----test_three
.teardown_function：每个用例结束后都会执行


================================== FAILURES ===================================
__________________________________ test_two ___________________________________

    def test_two():
        print("正在执行----test_two")
        x = "hello"
>       assert hasattr(x, 'check')
E       AssertionError: assert False
E        +  where False = hasattr('hello', 'check')

test_fixt.py:19: AssertionError
===================== 1 failed, 2 passed in 0.03 seconds ======================
2.从结果可以看出用例执行顺序：setup_function》用例1》teardown_function， setup_function》用例2》teardown_function， setup_function》用例3》teardown_function

备注：-s参数是为了显示用例的打印信息。 -q参数只显示结果，不显示过程

setup_module/teardown_module
1.setup_module是所有用例开始前只执行一次，teardown_module是所有用例结束后只执行一次

# test_fixt.py
'''






# coding:utf-8
import pytest
# 函数式

def setup_module():
    print("setup_module：整个.py模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")

def teardown_module():
    print("teardown_module：整个.py模块只执行一次")
    print("比如：所有用例结束只最后关闭浏览器")

def setup_function():
    print("setup_function：每个用例开始前都会执行")

def teardown_function():
    print("teardown_function：每个用例结束前都会执行")

def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x

def test_two():
    print("正在执行----test_two")
    x = "hello"
    assert hasattr(x, 'check')

def test_three():
    print("正在执行----test_three")
    a = "hello"
    b = "hello world"
    assert a in b

# if __name__ == "__main__":
    '''pytest.main(["-s", "test_fixt.py"])
2.从运行结果可以看到setup_module和teardown_module只执行了一次

test_fixt.py setup_module：整个.py模块只执行一次
比如：所有用例开始前只打开一次浏览器
setup_function：每个用例开始前都会执行
正在执行----test_one
.teardown_function：每个用例结束前都会执行
setup_function：每个用例开始前都会执行
正在执行----test_two
Fteardown_function：每个用例结束前都会执行
setup_function：每个用例开始前都会执行
正在执行----test_three
.teardown_function：每个用例结束前都会执行
teardown_module：整个.py模块只执行一次
比如：所有用例结束只最好关闭浏览器
备注：setup_function/teardown_function和setup_module/teardown_module这四种方法是可以任意组合的，用一个和多个都可以
'''





'''类和方法
1.setup/teardown和unittest里面的setup/teardown是一样的功能，setup_class和teardown_class等价于unittest里面的setupClass和teardownClass'''

#test_fixtclass.py

# coding:utf-8
import pytest
# 类和方法

class TestCase():

    def setup(self):
        print("setup: 每个用例开始前执行")

    def teardown(self):
        print("teardown: 每个用例结束后执行")

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之前")

    def setup_method(self):
        print("setup_method:  每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method:  每个用例结束后执行")

    def test_one(self):
        print("正在执行----test_one")
        x = "this"
        assert 'h' in x

    def test_two(self):
        print("正在执行----test_two")
        x = "hello"
        assert hasattr(x, 'check')

    def test_three(self):
        print("正在执行----test_three")
        a = "hello"
        b = "hello world"
        assert a in b

# if __name__ == "__main__":

'''pytest.main(["-s", "test_fixtclass.py"])
运行结果

test_fixtclass.py 

setup_class：所有用例执行之前
setup_method:  每个用例开始前执行
setup: 每个用例开始前执行
正在执行----test_one
.teardown: 每个用例结束后执行
teardown_method:  每个用例结束后执行
setup_method:  每个用例开始前执行
setup: 每个用例开始前执行
正在执行----test_two
Fteardown: 每个用例结束后执行
teardown_method:  每个用例结束后执行
setup_method:  每个用例开始前执行
setup: 每个用例开始前执行
正在执行----test_three
.teardown: 每个用例结束后执行
teardown_method:  每个用例结束后执行
teardown_class：所有用例执行之前

2.从结果看出，运行的优先级：setup_class》setup_method》setup 》用例》teardown》teardown_method》teardown_class
备注：这里setup_method和teardown_method的功能和setup/teardown功能是一样的，一般二者用其中一个即可'''




'''函数和类混合
1.如果一个.py的文件里面既有函数用例又有类和方法用例，运行顺序又是怎样的呢？'''

# coding:utf-8
import pytest
# 类和方法

def setup_module():
    print("setup_module：整个.py模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")

def teardown_module():
    print("teardown_module：整个.py模块只执行一次")
    print("比如：所有用例结束只最后关闭浏览器")

def setup_function():
    print("setup_function：每个用例开始前都会执行")

def teardown_function():
    print("teardown_function：每个用例结束前都会执行")

def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x

def test_two():
    print("正在执行----test_two")
    x = "hello"
    assert hasattr(x, 'check')

class TestCase():

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之前")

    def test_three(self):
        print("正在执行----test_three")
        x = "this"
        assert 'h' in x

    def test_four(self):
        print("正在执行----test_four")
        x = "hello"
        assert hasattr(x, 'check')

# if __name__ == "__main__":

'''pytest.main(["-s", "test_fixtclass.py"])
运行结果：

test_fixtclass.py

setup_module：整个.py模块只执行一次
比如：所有用例开始前只打开一次浏览器
setup_function：每个用例开始前都会执行
正在执行----test_one
.teardown_function：每个用例结束前都会执行
setup_function：每个用例开始前都会执行
正在执行----test_two
Fteardown_function：每个用例结束前都会执行
setup_class：所有用例执行之前
正在执行----test_three
.正在执行----test_four
Fteardown_class：所有用例执行之前
teardown_module：整个.py模块只执行一次
比如：所有用例结束只最后关闭浏览器'''



'''2.从运行结果看出，setup_module/teardown_module的优先级是最大的，然后函数里面用到的
setup_function/teardown_function与类里面的setup_class/teardown_class互不干涉'''
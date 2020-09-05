import pytest

''''这里的所有都是函数，（有类的情况下叫def方法，没类的情况下叫函数）'''
def setup_module():     #'所有用例开始前只执行一次，比如所有用例开始之前只打开一次浏览器
    print('所有用例开始前只执行一次')
    print("比如所有用例开始之前只打开一次浏览器")

def teardown_module():    #所有用例结束后只执行一次，比如所有用例结束后关闭浏览器
    print('所有用例结束后只执行一次')
    print("比如所有用例结束后关闭浏览器")


'''setup_function和teardwon_function只对函数用例生效（不在类中生效）'''
def setup_function():   #每个用例开始之前都会执行
    print('开始')

def teardown_function():  #每个用例结束后都会执行
    print("结束")


def test_1():
    print("第一条用例")

def test_2():
    print("第二天用例")

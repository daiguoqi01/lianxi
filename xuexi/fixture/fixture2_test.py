import pytest



@pytest.fixture(scope="class")
def user():
    print('你好')
    a="用户名"
    return a


def test_pwd():
    print("还哈皮")
    d="hollo"
    return d


'''scope="class"
fixture为class级别的时候，如果一个class里面有多个用例，都调用了此fixture，那么此fixture只在该class里所有用例开始前执行一次'''

'''scope="module"
fixture为module级别时，在当前.py脚本里面所有用例开始前只执行一次'''
class Test_class():
    def test1(self,user):
        print(user)


    def test2(self,user):
        print(user)
       # assert user=="用户名"

    def test3(self,user):
        print(user)







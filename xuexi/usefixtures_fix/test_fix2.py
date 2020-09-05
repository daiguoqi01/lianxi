import pytest


@pytest.fixture(scope="function")
def start(request):
    print("\n---开始执行fonction---")

@pytest.fixture(scope="function")
def test_b():
    print("---用例b执行---")

@pytest.mark.usefixtures("start")
def test_a():
    print('---用例a执行---')

'''如果class用例需要同时调用多个fixture，可以使用@pytest.mark.usefixtures()叠加。注意叠加顺序，先执行的放底层，后执行的放上层'''
@pytest.mark.usefixtures("test_b")
@pytest.mark.usefixtures("start")
class Test_aa():
    def test_1(self):
        print("用例1")

    def test_2(self):
        print("用例2")

if __name__ == '__main__':
    pytest.main(["-s","test_fix2.py"])


    '''usefixtures与传fixture区别
通过上面2个案例，对usefixtures使用基本方法已经掌握了，但是你会发现，我上面给的2个案例的fixture是没有返回值的。如果fixture有返回值，
那么usefixtures就无法获取到返回值了，这个是它与用例直接传fixture参数的区别。
也就是说当fixture用return值需要使用时，只能在用例里面传fixture参数了。
当fixture没有return值的时候，两种方法都可以。'''


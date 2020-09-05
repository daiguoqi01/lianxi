import pytest


@pytest.fixture(scope="function")
def start(request):
    print("\n---开始执行fonction---")


def test_a(start):
    print('---用例a执行---')


class Test_aa():
    def test_1(self,start):
        print("用例1")

    def test_2(self,start):
        print("用例2")

if __name__ == '__main__':
    pytest.main(["-s","test_fix.py"])


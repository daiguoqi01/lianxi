import pytest

#xfail_strict=True可以让标记为@pytest.mark.xfail但实际通过的测试用例被报告为失败

def test_hellow():
    print("hello word")
    assert 1

@pytest.mark.xfail()
def test_youyou1():
    a='hello'
    b='hello word'
    assert a==b



@pytest.mark.xfail()
def test_youyou2():
    a = 'hello'
    b = 'hello word'
    assert b!=a


if __name__ == '__main__':
    pytest.main(["-v","test_xpass.py"])
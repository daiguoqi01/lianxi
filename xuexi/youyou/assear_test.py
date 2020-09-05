import pytest
def fun():
    return 3


def test_fun():
    a=fun()

    assert a % 2 == 0 ,"判断a为偶数，当前a的值为：%s"%a


# def test_zero_division():
#     with pytest.raises(ZeroDivisionError):
#         1/0
#
#     assert excinfo.type==ZeroDivisionError
#     assert "division by zero" in str(excinof.value)



def test_1():
    '''用例描述'''
    a=1
    b=2
    assert a!=b



def test2():
    a="hellow_word"
    b="hellow"
    c="hellow"

    assert b in a
    assert b==c
    assert b !=c ,"若不等则输出b的值为：%s "%b
import pytest

@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+4",6),("6*9",53)])
def test_eval(test_input,expected):
    assert eval(test_input)==expected




@pytest.mark.parametrize("a,b",[("3+5",8),("2+4",6),("6*9",54)])
def test_eval1(a,b):
    assert eval(a)==b




@pytest.mark.parametrize("x",(0,1))
@pytest.mark.parametrize("y",(2,3))
def test_oo(x,y):
    print("测试数据组合:x->%s,y->%s" % (x,y))


def test_9():

    test_data = [("M", {"message": "update some data!", "code": 0}),
                 ("F", {"message": "update some data!", "code": 0})]

    print(test_data[0][1]["message"])





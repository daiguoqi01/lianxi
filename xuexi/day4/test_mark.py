import pytest



@pytest.mark.webtest
def test_send_http():
    print("mark_web_test")

def test_something_quit():
    pass

def test_another():
    pass


@pytest.mark.hello
class Test_class:
    def test_01(self):
        print("hello")

    def test_02(self):
        print("hellow_work")

if __name__ == '__main__':
    pytest.main(["-v","test_mark.py","-m=hello"])
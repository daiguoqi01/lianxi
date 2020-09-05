import pytest

# @pytest.fixture(scope="session")
# def user():
#     print("用户名")
#     a="中国人"
#     return a


'''scope="session"
fixture为session级别是可以跨.py模块调用的,也就是当我们有多个.py文件的用例时候，如果多个用例只需调用一次fixture，那就可以设置为scope="session"，
并且写到conftest.py文件里
conftest.py文件名称是固定的，pytest会自动识别该文件。放到工程的根目录下，就可以全局调用了，如果放到某个package包下，那就只在该package内有效'''
@pytest.fixture(scope="session")
def user():

    test_data = [("M", {"message": "update some data!", "code": 0}),
                 ("F", {"message": "update some data!", "code": 0})]

    a=(test_data[0][1]["message"])
    print("yonghu")
    return a



'''如果想同时运行test_fixture11.py和test_fixture12.py，在cmd执行
>pytest -s test_one.py test_two.py'''
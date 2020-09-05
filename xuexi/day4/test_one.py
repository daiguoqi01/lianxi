import pytest

def test1(user):
    print(user)
    #assert user=="update some data!"

def test2(user):
    print(user)



def baogao():
    #第一种报告
 '''pytest --html=report.html --self-contained-html ''' #报告命令    安装时输入pip install  pytest-html

    #第二种报告
'''pytest --pytest_report Pytest_Report.html'''   #报告命令     安装时输入 pip install PytestReport

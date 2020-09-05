import pymysql

def test_mysql():
    db=pymysql.connect(host="",
                       port="",
                       user="",
                       passwd="root",
                       db="test"
                       )

    curt=db.cursor()
    sql="updata 表名 set 字段名=" " where 要改的字段 "
    aql2="insert into 表名（表头）values(插入的字段)"
    curt.execute(sql)    #执行sql
    data=curt.fetchall()     #使用fetchall() 获取查询结果
    print(data)
    db.commit()           #提交sql，当为查询sql语句时不需要提交就可以
    db.close()

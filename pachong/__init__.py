import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","123456","finance_lender_test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "select count(*) from user"
try:
    # 执行sql语句
    cursor.execute(sql)
    results = cursor.fetchall()

    print(type(results))

    # for row in results:
    #     id = row[0]
    #     lname = row[1]
    #     age = row[2]
    #     # 打印结果
    #     print ("id=%d,lname=%s,age=%s" % \
    #            (id, lname, age))
    #     if id == 1:
    #         sql2 = "insert into user(username,cus) values ('%s','%s')"%('d','6')
    #         cursor.execute(sql2)
    #         db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()
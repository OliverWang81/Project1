import pymysql

# 打开数据库连接
db = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="world",
    charset="utf8mb4",
    autocommit=True
)

# 获取游标对象
cursor = db.cursor()

# 执行SQL查询
cursor.execute("SELECT VERSION()")

# 获取一条查询结果
data = cursor.fetchone()

# 输出查询结果
print("Database version : %s " % data)

# 关闭数据库连接
db.close()
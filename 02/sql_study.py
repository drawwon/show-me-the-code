import MySQLdb
import pprint
conn = MySQLdb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'runoob',
    charset = 'utf8'
)


cursor = conn.cursor()
sql = "select * from websites"
sql_insert = "insert into websites (name,alexa) VALUES ('drawon','50')"
sql_update = "update websites set name='drawwon' WHERE alexa=50"
sql_delete = "delete from websites WHERE alezxa>100"
try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount
    conn.commit()
except Exception as e:
    print e
    conn.rollback()
# m = cursor.execute(sql)
# a = cursor.fetchall()
# des = cursor.description
# des_name = []
# for i in range(len(des)):
#     des_name.append(des[i][0])
# print des_name
# for row in a:
#     print "id=%d,name=%s,address=%s, ranked=%d,country=%s"%row

cursor.close()
conn.close()


# cursor = conn.cursor()
# cursor.execute(sql)
# rs = cursor.fetchone()
# print rs
# rs = cursor.fetchmany(3)
# pprint.pprint(rs)
# rs = cursor.fetchall()
# print rs
# print conn
# print cursor
# cursor.close()
# conn.close()
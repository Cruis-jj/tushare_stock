import  pymysql

#连接mysql
db = pymysql.connect(host='localhost',user='root',password='',databbase='stock',port=3306,charset='utf-8')
cursor = db.cursor()
cursor.execute('')
cursor.close()
cursor.commit()
print(cursor.fetchall())
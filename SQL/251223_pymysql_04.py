import pymysql


db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password='1q2w3e4r!!', database="ecommerce", charset="utf8")

print(db)

cursor=db.cursor()


sql = "SELECT * FROM product2"
cursor.execute(sql)
    
result = cursor.fetchone() # 현재 커서를 다음 레코드로 이동시키고 해당 레코드를 반환
print(result)
    
    
result=cursor.fetchall()
print(result)
    
    
db.close()
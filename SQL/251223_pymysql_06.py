import pymysql


db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password='1q2w3e4r!!', database="ecommerce", charset="utf8")

print(db)

cursor=db.cursor()


sql = "DELETE FROM product2 WHERE product_code = '216573151';"
cursor.execute(sql)
db.commit()
db.close()
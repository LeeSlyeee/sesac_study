import pymysql


db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password='1q2w3e4r!!', database="ecommerce", charset="utf8")

print(db)

cursor=db.cursor()


for index in range(10):
    product_code = 216573150 + index + 1
    sql = """INSERT INTO product2 VALUES(
          '""" + str(product_code)+  """', '스위트바니 여름신상5900원~롱원피스티셔츠/긴팔/반팔', 23000, 6900, 70, 'F'); """
    print (sql)
    cursor.execute(sql)
    
db.commit()
db.close()
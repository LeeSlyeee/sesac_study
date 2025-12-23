import pymysql


db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password='1q2w3e4r!!', database="ecommerce", charset="utf8")

print(db)

cursor=db.cursor()


sql = """
    UPDATE product2 SET 
    TITLE='하늘하늘 원피스 썸머 스페셜 가디건',
    ORI_PRICE=33000,
    DISCOUNT_PRICE=9900,
    DISCOUNT_PERCENT=70
    WHERE PRODUCT_CODE='216573151';
"""

cursor.execute(sql)


db.commit()


sql = "select * from product2 where product_code='216573151';"
cursor.execute(sql)
result = cursor.fetchone()
print(result)


db.close()
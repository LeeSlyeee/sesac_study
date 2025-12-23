import pymysql


db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password='1q2w3e4r!!', charset="utf8")

print(db)

cursor=db.cursor()


sql = "CREATE DATABASE IF NOT EXISTS ecommerce"
cursor.execute(sql)

sql = "SHOW DATABASES"
cursor.execute(sql)
result = cursor.fetchall()
print(result)


sql = "USE ecommerce"
cursor.execute(sql)


sql = "SELECT DATABASE()"
cursor.execute(sql)
result = cursor.fetchall()
print(">>>", result)


print(cursor)


sql = """
CREATE TABLE IF NOT EXISTS product (
    PRODUCT_CODE VARCHAR(20) NOT NULL,
    TITLE VARCHAR(200) NOT NULL,
    ORI_PRICE INT,
    DISCOUNT_PRICE INT,
    DISCOUNT_PERCENT INT,
    DELIVERY VARCHAR(2),
    PRIMARY KEY(PRODUCT_CODE)
);
"""
cursor.execute(sql)

sql = "SHOW TABLES"
cursor.execute(sql)
result = cursor.fetchall()
print("+++", result)


db.commit()
db.close()








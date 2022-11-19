#!/usr/bin/python3
from dbConfig import conn, cur
def delStock(id):
    sql = "DELETE FROM `product` WHERE `product`.`id` = %s"
    cur.execute(sql,(id,))
    conn.commit()
def addProduct(name, price, amount):
    if(name == None or price == None or amount == None):
        return False
    sql = "insert into product (Name, Stock, Price) values (%s,%s,%s);"
    cur.execute(sql,(name, amount, price))
    conn.commit()
    return True
def changeName(name, id):
    if(name == None):
        return
    else:
        sql = "update product set Name=%s where id=%s;"
        cur.execute(sql,(name, id))
        conn.commit()
def changePrice(price, id):
    if(price == None):
        return
    else:
        sql = "update product set Price=%s where id=%s;"
        cur.execute(sql,(price, id))
        conn.commit()
def changeStock(amount, id):
    if(amount == None):
        return
    elif(amount == '0'):
        sql = "DELETE FROM `product` WHERE `product`.`id` = %s;"
        cur.execute(sql,(id,))
        conn.commit()
    else:
        sql = "update product set Stock=%s where id=%s;"
        cur.execute(sql,(amount, id))
        conn.commit()
    return True
def decrease(id, amount):
    sql = "update product set Stock=Stock-%s where id=%s;"
    cur.execute(sql,(amount, id))
    conn.commit()
def getList():
    #查詢
    sql="select id, Name,Stock, Price from product where Stock>0 ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
def searchProduct(id):
    sql = "select id, Name, Stock, Price from product where id = %s;"
    cur.execute(sql,(id,))
    records = cur.fetchall()
    return records[0][1], records[0][3], records[0][2]


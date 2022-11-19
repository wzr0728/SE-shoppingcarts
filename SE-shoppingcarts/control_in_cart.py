#!/usr/bin/python3
import control_in_stock
from dbConfig import conn, cur

def changeCart(amount, id):
    if(amount == '0'):
        sql = "DELETE FROM `Usercart` WHERE `Usercart`.`id` = %s;"
        cur.execute(sql,(id,))
        conn.commit()
    
    sql = "update Usercart set amount=%s where id=%s;"
    cur.execute(sql,(amount,id))
    conn.commit()
    return True

def purchase():
    sql = "select id, PiD,UiD, amount from Usercart where amount>0;"
    cur.execute(sql)
    records = cur.fetchall()
    money = 0
    flag = True #是不是第一次跑
    for (id, PiD,UiD, amount) in records:
        name, price, stock = control_in_stock.searchProduct(PiD)
        sql2 = "select id, Stock from product where id = %s;"
        cur.execute(sql2,(PiD,))
        records = cur.fetchall()
        if(stock < amount):
            return False
        money += (price*amount)
        sql = "select OiD from orderlist"
        cur.execute(sql)
        records = cur.fetchall()
        if(records == []):
            OiD = 1
            flag = False
        if(flag == False):
            pass
        else:
            OiD = records[len(records)-1][0] + 1
            flag = False
        sql = "insert into orderlist (OiD, PiD, UiD, amount, status) values (%s, %s,%s,%s, 'Preparing');"
        cur.execute(sql,(OiD, PiD, UiD, amount))
        conn.commit()
        control_in_stock.decrease(PiD, amount)
        changeCart('0', id)
    return money

def getList():
    #查詢
    sql="select id, PiD,UiD, amount from Usercart where amount>0;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
def exist(id):
    sql = "select PiD,amount from Usercart where PiD = %s;"
    cur.execute(sql,(id,))
    records = cur.fetchall()
    return records
def addcart(amount, id):
    if(amount == '0' or amount == None):
        return
    if exist(id) == []:
        
        sql = "select id, Stock from product where id = %s;"
        cur.execute(sql,(id,))
        records = cur.fetchall()
        stock = records[0][1]
        
        sql2="insert into Usercart (PiD, UiD, amount) values (%s,'user1',%s);"
        cur.execute(sql2,(id,amount))
        conn.commit()
    else:
        sql = "select id, Stock from product where id = %s;"
        cur.execute(sql,(id,))
        records = cur.fetchall()
        stock = records[0][1]
        if(str(stock) < amount):
            return False
        sql="update Usercart set amount=amount+%s where id=%s;"
        cur.execute(sql,(amount,id))
        conn.commit()
    return True
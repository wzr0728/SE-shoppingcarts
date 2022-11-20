#!/usr/bin/python3
from dbConfig import conn, cur
def getList():
    #查詢
    sql="select OiD, UiD, PiD, amount, status from orderlist ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
def shipping(id):
    sql = "select OiD, status from orderlist where OiD=%s ;"
    cur.execute(sql,(id,))
    records = cur.fetchall()
    if(records == []):
        return "無此訂單"
    if(records[0][1] != "Preparing"):
        return "Error, 可能已出貨"
    sql = "update orderlist set status = 'Shipping/Arrived' where OiD=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return "成功出貨"
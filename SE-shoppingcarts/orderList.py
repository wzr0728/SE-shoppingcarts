#!/usr/bin/python3
import codecs,sys
import cgi
import control_order, control_in_stock

print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()

goodsList = control_in_stock.getList()
ordersList = control_order.getList()
pos = 0
allPrice = 0
msg = """<form name="表單" method="post" action="shipping.py"> </p>"""
for (OiD, UiD, PiD, amount, status) in ordersList:
    if(pos == 0):
        pos = OiD
        msg += f"以下為{OiD}, {UiD} 的訂單</p>"
    elif(pos != OiD):
        msg += f"訂單總價{allPrice}</p>"
        allPrice = 0
        msg+="--------------------------------</p>"
        pos = OiD
        msg += f"以下為{OiD}號, {UiD} 的訂單</p>"
    name, price, stock = control_in_stock.searchProduct(PiD)
    allPrice+=price*amount
    msg = msg + f"商品 : {name} 數量 : {amount} 單項總價 : {price*amount} 狀態 : {status}</p>" 
    
msg += f"訂單總價{allPrice}</p>"
msg+="--------------------------------</p>"
msg+=f"""<input placeholder="輸入欲出貨的訂單編號" name="OiD"></p>"""
msg += """ <input type="submit" value="出貨去"></form>"""

with open("orderList.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"###msg###",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()
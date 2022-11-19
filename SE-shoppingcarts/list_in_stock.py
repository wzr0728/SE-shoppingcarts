#!/usr/bin/python3
import codecs,sys
import cgi
import control_in_stock

print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()

goodsList = control_in_stock.getList()

msg = """<form name="表單" method="post" action="add_cart.py">"""
for (id,goods_name, stock, price ) in goodsList:
    msg = msg + f"商品 : {goods_name} 商品價格 : {price} 庫存 : {stock} " 
    msg += f"""<select name="amount_{id}">
    <option value="0">0</option>"""
    for i in range(stock):
        i += 1
        msg += f"""<option value="{i}">{i}</option>"""
    
    msg += """</select></p>""" 

msg += """ <input type="submit" value="加入購物車"></form>"""

with open("list_in_stock.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"###msg###",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()
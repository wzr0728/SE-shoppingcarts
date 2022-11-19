#!/usr/bin/python3
import codecs,sys
import cgi
import control_in_cart, control_in_stock



print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()

cartList = control_in_cart.getList()
msg = """<form name="表單" method="post" action="del_cart.py">"""
allPrice = 0
for (id, PiD,UiD, amount) in cartList:
    name, price, stock = control_in_stock.searchProduct(PiD)
    msg = msg + f"商品 : {name} 單價 : {price} 購買數量 : {amount}" 
    msg += f"""<select name="amount_{id}">
    <option value="0">0</option>"""
    for i in range(stock):
        i += 1
        msg += f"""<option value="{i}">{i}</option>"""
    allPrice += (price*amount)
    msg += """</select></p>""" 

msg += f""" <input type="submit" value="修改購物車">
    <p>總計：{allPrice}</p>
    </form>"""

with open("list_cart.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"###cart_msg###",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()
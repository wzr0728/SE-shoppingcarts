#!/usr/bin/python3
import codecs,sys
import cgi
import control_in_stock

print("Content-type:text/html; charset;utf-8\n")
sys.stdout.flush()

goodsList = control_in_stock.getList()

msg = """<form name="表單" method="post" action="change_stock.py">
不輸入即為不更改</p>"""
for (id,goods_name, stock, price ) in goodsList:
    msg = msg + f"編號 : {id} 商品 : {goods_name} 商品價格 : {price} 庫存 : {stock} " 
    msg+=f"""<input placeholder="更改名稱" name="name_{id}">"""
    msg+=f"""<input placeholder="更改商品價格" name="price_{id}">"""
    msg+=f"""<input placeholder="更改數量" name="amount_{id}"></p>"""

msg += """ <input type="submit" value="修改存貨"></form></p>"""

msg += """<form method="post" action="del_stock.py">
輸入要刪除的訂單編號: <input type='text' name='i'><input type='submit'>
</form> <br>"""
with open("root.html","rb") as fp:
    st = fp.read()
    st = st.replace(b"###msg###",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()
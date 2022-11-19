#!/usr/bin/python3
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import control_in_stock, control_in_cart

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>add_cart</title>
</head>
<body>
""")
goodsList = control_in_stock.getList()
form = cgi.FieldStorage()
for i in goodsList:
    id = i[0]
    id_amount = form.getvalue(f'amount_{id}')
    status = control_in_cart.addcart(id_amount, id)
    if(status == False):
        print(f"編號：{id}存貨不足 或是發生錯誤")
    
    
print("添加完成")
print("<br><a href='list_cart.py'>查看購物車</a>")
print("<br><a href='list_in_stock.py'>查看首頁</a>")
print("</body></html>")

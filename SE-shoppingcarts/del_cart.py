#!/usr/bin/python3
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import control_in_cart

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
goodsList = control_in_cart.getList()
form = cgi.FieldStorage()
for i in range(goodsList[len(goodsList)-1][0]):
    i += 1
    id_amount = form.getvalue(f'amount_{i}')
    status = control_in_cart.changeCart(id_amount, i)
    if(status == False):
        print(f"編號：{i}修改失敗")
    
    
print("修改完成")
print("<br><a href='list_cart.py'>查看購物車</a>")
print("<br><a href='list_in_stock.py'>查看首頁</a>")
print("</body></html>")

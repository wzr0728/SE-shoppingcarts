#!/usr/bin/python3
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import control_in_cart, control_in_stock

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>del</title>
</head>
<body>
""")

money = control_in_cart.purchase()

print("總共是",money,"元")
print("結帳完成!")

print("<br><a href='list_cart.py'>查看購物車</a>")
print("<br><a href='list_in_stock.py'>查看首頁</a>")
print("</body></html>")


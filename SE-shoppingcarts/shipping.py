#!/usr/bin/python3
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import control_order

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
form = cgi.FieldStorage()
id = form.getvalue('OiD')
status = control_order.shipping(id)

print(status)

print("<br><a href='root.py'>查看管理頁面</a>")
print("<br><a href='orderList.py'>查看訂單</a>")
print("</body></html>")


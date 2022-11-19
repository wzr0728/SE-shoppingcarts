#import mariadb
import mysql.connector 

try:
 	#conn = mariadb.connect(
	conn = mysql.connector.connect(
		user="root",
		password="root",
		host="127.0.0.1",
		port=8889,
		db="shoppingcart"
	)
except: #mariadb.Error as e:
	print("Error connecting to DB")
	exit(1)
cur=conn.cursor()

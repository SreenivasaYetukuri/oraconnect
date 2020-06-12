# query.py

import cx_Oracle

connection = cx_Oracle.connect("cj", "welcome", "myhost.example.com/orclpdb1")

cursor = connection.cursor()
cursor.execute("select systimestamp from dual")
r, = cursor.fetchone()
print(r)

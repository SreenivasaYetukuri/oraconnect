# query.py
import cx_Oracle
import os

un=os.environ.get('APP_USER')
pw=os.environ.get('APP_PASSWORD')
cs=os.environ.get('APP_CONNECTIONSTRING') 

connection = cx_Oracle.connect(un, pw, cs)
cursor=connection.cursor()
cursor.execute("SELECT SYSTIMESTAMP FROM DUAL")
r, =cursor.fetchone()
print(r)


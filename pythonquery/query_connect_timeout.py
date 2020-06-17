# query.py
import cx_Oracle

connection = cx_Oracle.connect("sreeni","oracle","(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = 192.168.1.74)(PORT = 1521)) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = SONY)))")
cursor=connection.cursor()
cursor.execute("SELECT SYSTIMESTAMP FROM DUAL")
r, =cursor.fetchone()
print(r)


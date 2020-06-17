# query.py
import cx_Oracle

connection = cx_Oracle.connect("sreeni","oracle","tcps://192.168.1.74:1521/SONY?ssl_server_dn_match=off&connect_timeout=180&transport_connect_timeout=60&retry_count=3")
cursor=connection.cursor()
cursor.execute("SELECT SYSTIMESTAMP FROM DUAL")
r, =cursor.fetchone()
print(r)


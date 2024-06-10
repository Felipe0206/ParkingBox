import mysql.connector


    
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="parkingbox"
)

conexion= connection.cursor() 

conexion.execute("show table")

resultado=conexion.fetchall()

for fila in resultado:
    print(fila)
resultado.close()


import mysql.connector

# Establecer la conexión con el servidor MySQL
connection = mysql.connector.connect(
    host="localhost",  # Solo la dirección del host
    port=3306,  # El puerto se especifica por separado
    user="root",
    password="Andres.0206",  # Asegúrate de que esta contraseña sea correcta
    database="parkingbox"
)

# Crear un cursor
conexion = connection.cursor()

# Ejecutar la consulta para mostrar las tablas
conexion.execute("SHOW TABLES")

# Obtener todos los resultados de la consulta
resultado = conexion.fetchall()

# Imprimir cada fila del resultado
for fila in resultado:
    print(fila)

# Cerrar el cursor y la conexión
conexion.close()
connection.close()

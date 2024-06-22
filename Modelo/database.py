import mysql.connector

# Establecer la conexión con el servidor MySQL
connection = mysql.connector.connect(
    host="localhost",  # Solo la dirección del host
    port=3306,  # El puerto se especifica por separado
    user="root",
    password="Andres.0206",  # Asegúrate de que esta contraseña sea correcta
    database="parqueadero"
)


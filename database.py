import mysql.connector

def get_db_connection():
    """Establece y retorna una conexión a la base de datos MySQL."""
    connection = mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )
    return connection

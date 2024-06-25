# Importar el módulo mysql.connector
import mysql.connector

# Configurar los parámetros de conexión
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'Andres.0206',
    'database': 'parqueadero',
    'raise_on_warnings': True
}

# Establecer la conexión
try:
    db = mysql.connector.connect(**config)
    print("Conexión establecida correctamente.")
except mysql.connector.Error as err:
    print(f"Error de conexión: {err}")

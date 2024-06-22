# main.py

import mysql.connector
from database import connection

# Crear un cursor para ejecutar consultas SQL
cursor = connection.cursor()

# Definición de las clases para representar las tablas de la base de datos
class Tarifa:
    def __init__(self, id_tarifa, minutos, mensualidad, plena, perdidatk):
        self.id_tarifa = id_tarifa
        self.minutos = minutos
        self.mensualidad = mensualidad
        self.plena = plena
        self.perdidatk = perdidatk

    def __repr__(self):
        return f"Tarifa(id_tarifa={self.id_tarifa}, minutos={self.minutos}, mensualidad={self.mensualidad}, " \
               f"plena={self.plena}, perdidatk={self.perdidatk})"

class TipoVehiculo:
    def __init__(self, id_tipo_vh, nom_tipo_vh, tarifa_id_tarifa):
        self.id_tipo_vh = id_tipo_vh
        self.nom_tipo_vh = nom_tipo_vh
        self.tarifa_id_tarifa = tarifa_id_tarifa

    def __repr__(self):
        return f"TipoVehiculo(id_tipo_vh={self.id_tipo_vh}, nom_tipo_vh={self.nom_tipo_vh}, " \
               f"tarifa_id_tarifa={self.tarifa_id_tarifa})"

class Vehiculo:
    def __init__(self, id_placa, descri_vh, tipo_vehiculo_id, tarifa_id):
        self.id_placa = id_placa
        self.descri_vh = descri_vh
        self.tipo_vehiculo_id = tipo_vehiculo_id
        self.tarifa_id = tarifa_id

    def __repr__(self):
        return f"Vehiculo(id_placa={self.id_placa}, descri_vh={self.descri_vh}, " \
               f"tipo_vehiculo_id={self.tipo_vehiculo_id}, tarifa_id={self.tarifa_id})"

class Parqueadero:
    def __init__(self, id_parq, nombre_parq, direccion_parq):
        self.id_parq = id_parq
        self.nombre_parq = nombre_parq
        self.direccion_parq = direccion_parq

    def __repr__(self):
        return f"Parqueadero(id_parq={self.id_parq}, nombre_parq={self.nombre_parq}, " \
               f"direccion_parq={self.direccion_parq})"

class Funcionario:
    def __init__(self, id_funcionario, nom_fun, apes_fun, correo, contrasena, parqueadero_id):
        self.id_funcionario = id_funcionario
        self.nom_fun = nom_fun
        self.apes_fun = apes_fun
        self.correo = correo
        self.contrasena = contrasena
        self.parqueadero_id = parqueadero_id

    def __repr__(self):
        return f"Funcionario(id_funcionario={self.id_funcionario}, nom_fun={self.nom_fun}, " \
               f"apes_fun={self.apes_fun}, correo={self.correo}, contrasena={self.contrasena}, " \
               f"parqueadero_id={self.parqueadero_id})"

class Bahia:
    def __init__(self, id_bh, nom_tipo_bh, cantidad_bh, estado_bh, parqueadero_id):
        self.id_bh = id_bh
        self.nom_tipo_bh = nom_tipo_bh
        self.cantidad_bh = cantidad_bh
        self.estado_bh = estado_bh
        self.parqueadero_id = parqueadero_id

    def __repr__(self):
        return f"Bahia(id_bh={self.id_bh}, nom_tipo_bh={self.nom_tipo_bh}, cantidad_bh={self.cantidad_bh}, " \
               f"estado_bh={self.estado_bh}, parqueadero_id={self.parqueadero_id})"

class GeneradorFac:
    def __init__(self, id_num_factura, totalizado_tarifa, iva_aplicado, total_servicio, condiciones_ser):
        self.id_num_factura = id_num_factura
        self.totalizado_tarifa = totalizado_tarifa
        self.iva_aplicado = iva_aplicado
        self.total_servicio = total_servicio
        self.condiciones_ser = condiciones_ser

    def __repr__(self):
        return f"GeneradorFac(id_num_factura={self.id_num_factura}, totalizado_tarifa={self.totalizado_tarifa}, " \
               f"iva_aplicado={self.iva_aplicado}, total_servicio={self.total_servicio}, " \
               f"condiciones_ser={self.condiciones_ser})"

class Registro:
    def __init__(self, id_registro, fecha_entradayhora, fecha_salidayhora, vehiculo_id_placa, 
                 parqueadero_id_parq, generadorfac_id_num_factura):
        self.id_registro = id_registro
        self.fecha_entradayhora = fecha_entradayhora
        self.fecha_salidayhora = fecha_salidayhora
        self.vehiculo_id_placa = vehiculo_id_placa
        self.parqueadero_id_parq = parqueadero_id_parq
        self.generadorfac_id_num_factura = generadorfac_id_num_factura

    def __repr__(self):
        return f"Registro(id_registro={self.id_registro}, fecha_entradayhora={self.fecha_entradayhora}, " \
               f"fecha_salidayhora={self.fecha_salidayhora}, vehiculo_id_placa={self.vehiculo_id_placa}, " \
               f"parqueadero_id_parq={self.parqueadero_id_parq}, " \
               f"generadorfac_id_num_factura={self.generadorfac_id_num_factura})"

class Rol:
    def __init__(self, id_rol, nom_rol):
        self.id_rol = id_rol
        self.nom_rol = nom_rol

    def __repr__(self):
        return f"Rol(id_rol={self.id_rol}, nom_rol={self.nom_rol})"

class FuncionarioRol:
    def __init__(self, funcionario_id_funcionario, rol_id_rol):
        self.funcionario_id_funcionario = funcionario_id_funcionario
        self.rol_id_rol = rol_id_rol

    def __repr__(self):
        return f"FuncionarioRol(funcionario_id_funcionario={self.funcionario_id_funcionario}, " \
               f"rol_id_rol={self.rol_id_rol})"

# Ejemplo de consulta para obtener todas las tablas de la base de datos
try:
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])

    # Ejemplo de consulta para obtener todos los registros de la tabla Tarifa
    cursor.execute("SELECT * FROM TARIFA")
    tarifas = cursor.fetchall()
    for tarifa in tarifas:
        id_tarifa, minutos, mensualidad, plena, perdidatk = tarifa
        tarifa_obj = Tarifa(id_tarifa, minutos, mensualidad, plena, perdidatk)
        print(tarifa_obj)

    # Ejemplo de consulta para obtener todos los registros de la tabla TipoVehiculo
    cursor.execute("SELECT * FROM TIPO_VEHICULO")
    tipos_vehiculo = cursor.fetchall()
    for tipo in tipos_vehiculo:
        id_tipo_vh, nom_tipo_vh, tarifa_id_tarifa = tipo
        tipo_vehiculo_obj = TipoVehiculo(id_tipo_vh, nom_tipo_vh, tarifa_id_tarifa)
        print(tipo_vehiculo_obj)

    # Puedes continuar agregando consultas para las otras tablas de la base de datos

except mysql.connector.Error as error:
    print("Error al ejecutar la consulta:", error)

finally:
    # Cerrar el cursor y la conexión
    if cursor:
        cursor.close()
    if connection:
        connection.close()

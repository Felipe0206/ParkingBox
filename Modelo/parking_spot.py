class Vehiculo:
    def __init__(self, id_p, placa, descri_vh):
        self.id_p = id_p
        self.placa = placa
        self.descri_vh = descri_vh

class TipoVehiculo:
    def __init__(self, id_tipo_vh, nom_tipo_vh, id_tarifa):
        self.id_tipo_vh = id_tipo_vh
        self.nom_tipo_vh = nom_tipo_vh
        self.id_tarifa = id_tarifa

class Tarifa:
    def __init__(self, id_tarifa, minutos, dia, mensualidad, plena, perdidatk):
        self.id_tarifa = id_tarifa
        self.minutos = minutos
        self.dia = dia
        self.mensualidad = mensualidad
        self.plena = plena
        self.perdidatk = perdidatk

class Conductor:
    def __init__(self, id_conductor, cedula, nom_cond, ape1_cond, ape2_cond):
        self.id_conductor = id_conductor
        self.cedula = cedula
        self.nom_cond = nom_cond
        self.ape1_cond = ape1_cond
        self.ape2_cond = ape2_cond

class Parqueadero:
    def __init__(self, id_parq, direccion_parq):
        self.id_parq = id_parq
        self.direccion_parq = direccion_parq

class Funcionario:
    def __init__(self, id_funcionario, nom_fun, ape1_fun, ape2_fun, id_rol, contrasena, user):
        self.id_funcionario = id_funcionario
        self.nom_fun = nom_fun
        self.ape1_fun = ape1_fun
        self.ape2_fun = ape2_fun
        self.id_rol = id_rol
        self.contrasena = contrasena
        self.user = user

class Bahia:
    def __init__(self, id_bh, nom_tipo_bh, id_parq):
        self.id_bh = id_bh
        self.nom_tipo_bh = nom_tipo_bh
        self.id_parq = id_parq

class Estado:
    def __init__(self, id_estado, nom_estado):
        self.id_estado = id_estado
        self.nom_estado = nom_estado

class Registro:
    def __init__(self, id_registro, fecha_entradayhora, fecha_salidayhora, id_parq, id_p):
        self.id_registro = id_registro
        self.fecha_entradayhora = fecha_entradayhora
        self.fecha_salidayhora = fecha_salidayhora
        self.id_parq = id_parq
        self.id_p = id_p

class Facturador:
    def __init__(self, id_num_factura, totalizado_horaminseg, iva_aplicado, total_monetizado, id_registro):
        self.id_num_factura = id_num_factura
        self.totalizado_horaminseg = totalizado_horaminseg
        self.iva_aplicado = iva_aplicado
        self.total_monetizado = total_monetizado
        self.id_registro = id_registro

class VehiculoConductorTipo:
    def __init__(self, id_veconti, id_placa, id_conductor, id_tipo_vh):
        self.id_veconti = id_veconti
        self.id_placa = id_placa
        self.id_conductor = id_conductor
        self.id_tipo_vh = id_tipo_vh

class BahiaEstado:
    def __init__(self, id_bh, id_estado):
        self.id_bh = id_bh
        self.id_estado = id_estado

class Rol:
    def __init__(self, id_rol, nom_rol):
        self.id_rol = id_rol
        self.nom_rol = nom_rol

class ParqueaderoFuncionario:
    def __init__(self, id_parq, id_funcionario):
        self.id_parq = id_parq
        self.id_funcionario = id_funcionario

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tarifa(db.Model):
    __tablename__ = 'tarifa'

    id_tarifa = db.Column(db.Integer, primary_key=True)
    minutos = db.Column(db.Integer)
    mensualidad = db.Column(db.Float)
    plena = db.Column(db.Float)
    perdidatk = db.Column(db.Float)

    def __repr__(self):
        return f"Tarifa(id_tarifa={self.id_tarifa}, minutos={self.minutos}, mensualidad={self.mensualidad}, " \
               f"plena={self.plena}, perdidatk={self.perdidatk})"

class TipoVehiculo(db.Model):
    __tablename__ = 'tipo_vehiculo'

    id_tipo_vh = db.Column(db.Integer, primary_key=True)
    nom_tipo_vh = db.Column(db.String(50))
    tarifa_id_tarifa = db.Column(db.Integer, db.ForeignKey('tarifa.id_tarifa'))

    def __repr__(self):
        return f"TipoVehiculo(id_tipo_vh={self.id_tipo_vh}, nom_tipo_vh={self.nom_tipo_vh}, " \
               f"tarifa_id_tarifa={self.tarifa_id_tarifa})"

class Vehiculo(db.Model):
    __tablename__ = 'vehiculo'

    id_placa = db.Column(db.String(10), primary_key=True)
    descri_vh = db.Column(db.String(100))
    tipo_vehiculo_id = db.Column(db.Integer, db.ForeignKey('tipo_vehiculo.id_tipo_vh'))
    tarifa_id = db.Column(db.Integer, db.ForeignKey('tarifa.id_tarifa'))

    def __repr__(self):
        return f"Vehiculo(id_placa={self.id_placa}, descri_vh={self.descri_vh}, " \
               f"tipo_vehiculo_id={self.tipo_vehiculo_id}, tarifa_id={self.tarifa_id})"

class Parqueadero(db.Model):
    __tablename__ = 'parqueadero'

    id_parq = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_parq = db.Column(db.String(100))
    direccion_parq = db.Column(db.String(200))

    def __repr__(self):
        return f"Parqueadero(id_parq={self.id_parq}, nombre_parq={self.nombre_parq}, " \
               f"direccion_parq={self.direccion_parq})"

class Funcionario(db.Model):
    __tablename__ = 'funcionario'

    id_funcionario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_fun = db.Column(db.String(50))
    apes_fun = db.Column(db.String(50))
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(50), nullable=False)
    parqueadero_id = db.Column(db.Integer, db.ForeignKey('parqueadero.id_parq'))

    def __repr__(self):
        return f"Funcionario(id_funcionario={self.id_funcionario}, nom_fun={self.nom_fun}, " \
               f"apes_fun={self.apes_fun}, correo={self.correo}, contrasena={self.contrasena}, " \
               f"parqueadero_id={self.parqueadero_id})"


class Bahia(db.Model):
    __tablename__ = 'bahia'

    id_bh = db.Column(db.Integer, primary_key=True)
    nom_tipo_bh = db.Column(db.String(50))
    cantidad_bh = db.Column(db.Integer)
    estado_bh = db.Column(db.String(20))
    parqueadero_id = db.Column(db.Integer, db.ForeignKey('parqueadero.id_parq'))

    def __repr__(self):
        return f"Bahia(id_bh={self.id_bh}, nom_tipo_bh={self.nom_tipo_bh}, cantidad_bh={self.cantidad_bh}, " \
               f"estado_bh={self.estado_bh}, parqueadero_id={self.parqueadero_id})"

class GeneradorFac(db.Model):
    __tablename__ = 'generadorfac'

    id_num_factura = db.Column(db.Integer, primary_key=True)
    totalizado_tarifa = db.Column(db.Float)
    iva_aplicado = db.Column(db.Float)
    total_servicio = db.Column(db.Float)
    condiciones_ser = db.Column(db.String(200))

    def __repr__(self):
        return f"GeneradorFac(id_num_factura={self.id_num_factura}, totalizado_tarifa={self.totalizado_tarifa}, " \
               f"iva_aplicado={self.iva_aplicado}, total_servicio={self.total_servicio}, " \
               f"condiciones_ser={self.condiciones_ser})"

class Registro(db.Model):
    __tablename__ = 'registro'

    id_registro = db.Column(db.Integer, primary_key=True)
    fecha_entradayhora = db.Column(db.DateTime)
    fecha_salidayhora = db.Column(db.DateTime)
    vehiculo_id_placa = db.Column(db.String(10), db.ForeignKey('vehiculo.id_placa'))
    parqueadero_id_parq = db.Column(db.Integer, db.ForeignKey('parqueadero.id_parq'))
    generadorfac_id_num_factura = db.Column(db.Integer, db.ForeignKey('generadorfac.id_num_factura'))

    def __repr__(self):
        return f"Registro(id_registro={self.id_registro}, fecha_entradayhora={self.fecha_entradayhora}, " \
               f"fecha_salidayhora={self.fecha_salidayhora}, vehiculo_id_placa={self.vehiculo_id_placa}, " \
               f"parqueadero_id_parq={self.parqueadero_id_parq}, " \
               f"generadorfac_id_num_factura={self.generadorfac_id_num_factura})"

class Rol(db.Model):
    __tablename__ = 'rol'

    id_rol = db.Column(db.Integer, primary_key=True)
    nom_rol = db.Column(db.String(50))

    def __repr__(self):
        return f"Rol(id_rol={self.id_rol}, nom_rol={self.nom_rol})"

class FuncionarioRol(db.Model):
    __tablename__ = 'funcionario_has_rol'

    funcionario_id_funcionario = db.Column(db.Integer, db.ForeignKey('funcionario.id_funcionario'), primary_key=True)
    rol_id_rol = db.Column(db.Integer, db.ForeignKey('rol.id_rol'), primary_key=True)

    def __repr__(self):
        return f"FuncionarioRol(funcionario_id_funcionario={self.funcionario_id_funcionario}, " \
               f"rol_id_rol={self.rol_id_rol})"

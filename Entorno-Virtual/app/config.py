# config.py

class Config:
    SECRET_KEY = 'tu_clave_secreta'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Andres.0206@localhost/parqueadero'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deshabilita el seguimiento de modificaciones

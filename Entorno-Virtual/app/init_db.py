from app import app, db
from modelos import Funcionario, Parqueadero
from datetime import datetime

# Crear todas las tablas según los modelos definidos en SQLAlchemy
with app.app_context():
    db.create_all()

    # Agregar datos de prueba
    try:
        # Crear un nuevo funcionario
        nuevo_funcionario = Funcionario(
            id_funcionario=1,  # Aquí se especifica el ID del funcionario
            nom_fun='Juan',
            apes_fun='Pérez',
            correo='juan.perez@example.com',
            contrasena='123456'
        )

        # Obtener un parqueadero existente (supongamos que tiene id_parq=1)
        parqueadero = Parqueadero.query.filter_by(id_parq=1).first()

        # Asignar el parqueadero al funcionario
        if parqueadero:
            nuevo_funcionario.parqueadero_id = parqueadero.id_parq

        db.session.add(nuevo_funcionario)
        db.session.commit()

        print(f"Funcionario creado exitosamente con id {nuevo_funcionario.id_funcionario}.")

    except Exception as e:
        db.session.rollback()
        print(f"Error al crear funcionario: {str(e)}")

    finally:
        db.session.close()

from flask import Blueprint, jsonify, request
from modelos import Funcionario, Parqueadero, db  # Importa los modelos y la instancia de SQLAlchemy

# Crea un Blueprint para los controladores relacionados con funcionarios
funcionarios_bp = Blueprint('funcionarios', __name__, url_prefix='/funcionarios')

# Controlador para obtener todos los funcionarios
@funcionarios_bp.route('', methods=['GET'])
def get_funcionarios():
    funcionarios = Funcionario.query.all()
    return jsonify([funcionario.__dict__ for funcionario in funcionarios]), 200

# Controlador para obtener un funcionario por su ID
@funcionarios_bp.route('/<int:id>', methods=['GET'])
def get_funcionario_by_id(id):
    funcionario = Funcionario.query.get_or_404(id)
    return jsonify(funcionario.__dict__), 200

# Controlador para crear un nuevo funcionario
@funcionarios_bp.route('', methods=['POST'])
def create_funcionario():
    data = request.json
    nuevo_funcionario = Funcionario(
        nom_fun=data['nom_fun'],
        apes_fun=data['apes_fun'],
        correo=data['correo'],
        contrasena=data['contrasena'],
        parqueadero_id=data['parqueadero_id']
    )
    db.session.add(nuevo_funcionario)
    db.session.commit()
    return jsonify({'message': 'Funcionario creado correctamente', 'estado': True}), 201

# Controlador para actualizar un funcionario existente por su ID
@funcionarios_bp.route('/<int:id>', methods=['PUT'])
def update_funcionario(id):
    funcionario = Funcionario.query.get_or_404(id)
    data = request.json
    funcionario.nom_fun = data.get('nom_fun', funcionario.nom_fun)
    funcionario.apes_fun = data.get('apes_fun', funcionario.apes_fun)
    funcionario.correo = data.get('correo', funcionario.correo)
    funcionario.contrasena = data.get('contrasena', funcionario.contrasena)
    funcionario.parqueadero_id = data.get('parqueadero_id', funcionario.parqueadero_id)
    db.session.commit()
    return jsonify({'message': 'Funcionario actualizado correctamente', 'estado': True}), 200

# Controlador para eliminar un funcionario por su ID
@funcionarios_bp.route('/<int:id>', methods=['DELETE'])
def delete_funcionario(id):
    funcionario = Funcionario.query.get_or_404(id)
    db.session.delete(funcionario)
    db.session.commit()
    return jsonify({'message': 'Funcionario eliminado correctamente', 'estado': True}), 200

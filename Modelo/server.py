from flask import Flask, request, jsonify
from controllers.parking_controller import list_parking_spots, create_parking_spot, update_parking_spot, delete_parking_spot

app = Flask(__name__)

@app.route('/api/spots', methods=['GET'])
def get_spots():
    # Obtiene todos los espacios de parqueo y los devuelve como JSON
    spots = list_parking_spots()
    spots_dict = [spot.__dict__ for spot in spots]
    return jsonify(spots_dict)

@app.route('/api/spots', methods=['POST'])
def add_spot():
    # Crea un nuevo espacio de parqueo utilizando los datos proporcionados en el cuerpo de la solicitud JSON
    data = request.get_json()
    number = data['number']
    is_occupied = data['is_occupied']
    create_parking_spot(number, is_occupied)
    return jsonify({'message': 'Spot created successfully'}), 201

@app.route('/api/spots/<int:spot_id>', methods=['PUT'])
def edit_spot(spot_id):
    # Actualiza un espacio de parqueo existente utilizando los datos proporcionados en el cuerpo de la solicitud JSON
    data = request.get_json()
    number = data['number']
    is_occupied = data['is_occupied']
    update_parking_spot(spot_id, number, is_occupied)
    return jsonify({'message': 'Spot updated successfully'})

@app.route('/api/spots/<int:spot_id>', methods=['DELETE'])
def remove_spot(spot_id):
    # Elimina un espacio de parqueo existente según el ID proporcionado
    delete_parking_spot(spot_id)
    return jsonify({'message': 'Spot deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)

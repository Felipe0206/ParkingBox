from flask import request, jsonify
from models import Tarifa

def calcular_costo_estacionamiento():
    """
    Controlador para calcular el costo de estacionamiento basado en los minutos estacionados.
    """
    minutos_estacionados = request.args.get('minutos_estacionados')
    time=int
    try:
        # Calcular el costo de estacionamiento en el modelo
        costo = Tarifa.calcular_costo_estacionamiento(int(minutos_estacionados)*time)
        return jsonify({'costo': costo}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400



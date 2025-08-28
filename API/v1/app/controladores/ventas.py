from flask import Blueprint, request, jsonify
from ..modelos.ventas import VentaModel

ventas_endpoints = Blueprint('ventas_endpoints', __name__)

@ventas_endpoints.route('/ventas', methods=['GET'])
def obtener_ventas():
    id_venta = request.args.get('id')

    if id_venta:
        venta = VentaModel.obtener_por_id(id_venta)
        if venta:
            return jsonify(venta), 200
        return jsonify({"error": "Venta no encontrada"}), 404

    ventas = VentaModel.obtener_todos()
    return jsonify(ventas), 200

@ventas_endpoints.route('/ventas', methods=['POST'])
def crear_venta():
    venta_data = request.json
    venta_id = VentaModel.crear(venta_data)
    return jsonify({"mensaje": "Venta creada", "id": venta_id}), 201

@ventas_endpoints.route('/ventas', methods=['PUT'])
def actualizar_venta():
    id_venta = request.args.get('id')
    datos_actualizados = request.json

    if VentaModel.actualizar(id_venta, datos_actualizados):
        return jsonify({"mensaje": "Venta actualizada"}), 200
    return jsonify({"error": "No se pudo actualizar la venta"}), 400

@ventas_endpoints.route('/ventas', methods=['DELETE'])
def eliminar_venta():
    id_venta = request.args.get('id')

    if VentaModel.eliminar(id_venta):
        return jsonify({"mensaje": "Venta eliminada"}), 200
    return jsonify({"error": "No se pudo eliminar la venta"}), 400

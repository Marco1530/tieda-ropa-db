from flask import Blueprint, request, jsonify
from ..modelos.prendas  import PrendaModel

prendas_endpoints = Blueprint('prendas_endpoints', __name__)

@prendas_endpoints.route('/prendas', methods=['GET'])
def obtener_prendas():
    id_prenda = request.args.get('id')

    if id_prenda:
        prenda = PrendaModel.obtener_por_id(id_prenda)
        if prenda:
            return jsonify(prenda), 200
        return jsonify({"error": "Prenda no encontrada"}), 404

    prendas = PrendaModel.obtener_todos()
    return jsonify(prendas), 200

@prendas_endpoints.route('/prendas', methods=['POST'])
def crear_prenda():
    prenda_data = request.json
    prenda_id = PrendaModel.crear(prenda_data)
    return jsonify({"mensaje": "Prenda creada", "id": prenda_id}), 201

@prendas_endpoints.route('/prendas', methods=['PUT'])
def actualizar_prenda():
    id_prenda = request.args.get('id')
    datos_actualizados = request.json

    if PrendaModel.actualizar(id_prenda, datos_actualizados):
        return jsonify({"mensaje": "Prenda actualizada"}), 200
    return jsonify({"error": "No se pudo actualizar la prenda"}), 400

@prendas_endpoints.route('/prendas', methods=['DELETE'])
def eliminar_prenda():
    id_prenda = request.args.get('id')

    if PrendaModel.eliminar(id_prenda):
        return jsonify({"mensaje": "Prenda eliminada"}), 200
    return jsonify({"error": "No se pudo eliminar la prenda"}), 400

from flask import Flask, jsonify, request
from flask_cors import CORS
from config.db import prendas_collection
from bson import ObjectId

app = Flask(__name__)
CORS(app)

# Obtener todas las prendas
@app.route('/api/prendas', methods=['GET'])
def obtener_prendas():
    prendas = list(prendas_collection.find({}, {'_id': 0}))
    return jsonify(prendas)

# Obtener una prenda por ID
@app.route('/api/prendas/<id>', methods=['GET'])
def obtener_prenda_por_id(id):
    try:
        prenda = prendas_collection.find_one({'_id': ObjectId(id)}, {'_id': 0})
        if prenda:
            return jsonify(prenda)
        return jsonify({'error': 'Prenda no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Insertar una nueva prenda
@app.route('/api/prendas', methods=['POST'])
def insertar_prenda():
    data = request.json
    nueva_prenda = {
        "nombre": data.get("nombre"),
        "marca": data.get("marca"),
        "precio": data.get("precio"),
        "stock": data.get("stock")
    }
    resultado = prendas_collection.insert_one(nueva_prenda)
    return jsonify({"mensaje": "Prenda insertada exitosamente", "id": str(resultado.inserted_id)}), 201

# Actualizar una prenda por ID
@app.route('/api/prendas/<id>', methods=['PUT'])
def actualizar_prenda(id):
    data = request.json
    nueva_data = {
        "nombre": data.get("nombre"),
        "marca": data.get("marca"),
        "precio": data.get("precio"),
        "stock": data.get("stock")
    }
    resultado = prendas_collection.update_one({'_id': ObjectId(id)}, {"$set": nueva_data})
    if resultado.matched_count == 0:
        return jsonify({"error": "Prenda no encontrada"}), 404
    return jsonify({"mensaje": "Prenda actualizada exitosamente"})

# Eliminar una prenda por ID
@app.route('/api/prendas/<id>', methods=['DELETE'])
def eliminar_prenda(id):
    resultado = prendas_collection.delete_one({'_id': ObjectId(id)})
    if resultado.deleted_count == 0:
        return jsonify({"error": "Prenda no encontrada"}), 404
    return jsonify({"mensaje": "Prenda eliminada exitosamente"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

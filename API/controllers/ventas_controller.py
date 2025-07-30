from flask import request, jsonify
from bson import ObjectId
from config.db import db
from models.venta_model import serialize_venta

#collection = db.ventas

def get_ventas():
    collection = db.prendas
    ventas = collection.find()
    return jsonify([serialize_venta(v) for v in ventas])

def get_venta(id):
    collection = db.prendas
    venta = collection.find_one({"_id": ObjectId(id)})
    return jsonify(serialize_venta(venta)) if venta else ("No encontrada", 404)

def create_venta():
    collection = db.prendas
    data = request.json
    result = collection.insert_one(data)
    return jsonify({"id": str(result.inserted_id)})

def update_venta(id):
    collection = db.prendas
    data = request.json
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return ("Actualizada", 200) if result.modified_count else ("No modificada", 404)

def delete_venta(id):
    collection = db.prendas
    result = collection.delete_one({"_id": ObjectId(id)})
    return ("Eliminada", 200) if result.deleted_count else ("No encontrada", 404)
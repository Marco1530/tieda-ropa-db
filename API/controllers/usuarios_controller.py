from flask import request, jsonify
from bson import ObjectId
from config.db import db
from models.usuario_model import serialize_usuario

#collection = db.usuarios

def get_usuarios():
    collection = db.prendas
    usuarios = collection.find()
    return jsonify([serialize_usuario(u) for u in usuarios])

def get_usuario(id):
    collection = db.prendas
    usuario = collection.find_one({"_id": ObjectId(id)})
    return jsonify(serialize_usuario(usuario)) if usuario else ("No encontrado", 404)

def create_usuario():
    collection = db.prendas
    data = request.json
    result = collection.insert_one(data)
    return jsonify({"id": str(result.inserted_id)})

def update_usuario(id):
    collection = db.prendas
    data = request.json
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return ("Actualizado", 200) if result.modified_count else ("No modificado", 404)

def delete_usuario(id):
    collection = db.prendas
    result = collection.delete_one({"_id": ObjectId(id)})
    return ("Eliminado", 200) if result.deleted_count else ("No encontrado", 404)
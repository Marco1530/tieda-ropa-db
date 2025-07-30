from flask import request, jsonify
from bson import ObjectId
from config.db import db
from models.prenda_model import serialize_prenda

#collection = db.prendas

def get_prendas():
    collection = db.prendas
    prendas = collection.find()
    return jsonify([serialize_prenda(p) for p in prendas])

def get_prenda(id):
    collection = db.prendas
    prenda = collection.find_one({"_id": ObjectId(id)})
    return jsonify(serialize_prenda(prenda)) if prenda else ("No encontrada", 404)

def create_prenda():
    collection = db.prendas
    data = request.json
    result = collection.insert_one(data)
    return jsonify({"id": str(result.inserted_id)})

def update_prenda(id):
    collection = db.prendas
    data = request.json
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return ("Actualizada", 200) if result.modified_count else ("No modificada", 404)

def delete_prenda(id):
    collection = db.prendas
    result = collection.delete_one({"_id": ObjectId(id)})
    return ("Eliminada", 200) if result.deleted_count else ("No encontrada", 404)

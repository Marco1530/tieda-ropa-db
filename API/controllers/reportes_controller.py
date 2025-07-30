from flask import jsonify
from config.db import db
from bson.objectid import ObjectId

# 1. Marcas con al menos una venta
def marcas_con_ventas():
    pipeline = [
        {"$lookup": {
            "from": "prendas",
            "localField": "prenda_id",
            "foreignField": "_id",
            "as": "prenda"
        }},
        {"$unwind": "$prenda"},
        {"$group": {"_id": "$prenda.marca"}},
        {"$project": {"marca": "$_id", "_id": 0}}
    ]
    marcas = list(db.ventas.aggregate(pipeline))
    return jsonify(marcas)

# 2. Prendas vendidas con cantidad restante en stock
def prendas_vendidas_stock():
    pipeline = [
        {"$lookup": {
            "from": "prendas",
            "localField": "prenda_id",
            "foreignField": "_id",
            "as": "prenda"
        }},
        {"$unwind": "$prenda"},
        {"$group": {
            "_id": "$prenda._id",
            "nombre": {"$first": "$prenda.nombre"},
            "stock": {"$first": "$prenda.stock"},
            "cantidad_vendida": {"$sum": "$cantidad"}
        }},
        {"$project": {
            "_id": 0,
            "nombre": 1,
            "cantidad_vendida": 1,
            "stock_restante": {"$subtract": ["$stock", "$cantidad_vendida"]}
        }}
    ]
    prendas = list(db.ventas.aggregate(pipeline))
    return jsonify(prendas)

# 3. Top 5 marcas más vendidas
def top_marcas():
    pipeline = [
        {"$lookup": {
            "from": "prendas",
            "localField": "prenda_id",
            "foreignField": "_id",
            "as": "prenda"
        }},
        {"$unwind": "$prenda"},
        {"$group": {"_id": "$prenda.marca", "total": {"$sum": "$cantidad"}}},
        {"$sort": {"total": -1}},
        {"$limit": 5},
        {"$project": {"marca": "$_id", "ventas": "$total", "_id": 0}}
    ]
    top = list(db.ventas.aggregate(pipeline))
    return jsonify(top)

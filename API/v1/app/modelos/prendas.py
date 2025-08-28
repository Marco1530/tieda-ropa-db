from bson.objectid import ObjectId
from app.index import mongo

class PrendaModel:
    @staticmethod
    def obtener_todos():
        prendas_cursor = mongo.db.prendas.find()
        prendas = []
        for prenda in prendas_cursor:
            prenda["_id"] = str(prenda["_id"])
            prendas.append(prenda)
        return prendas

    @staticmethod
    def obtener_por_id(id):
        try:
            prenda = mongo.db.prendas.find_one({"_id": ObjectId(id)})
            if prenda:
                prenda["_id"] = str(prenda["_id"])
            return prenda
        except:
            return None

    @staticmethod
    def crear(prenda_data):
        resultado = mongo.db.prendas.insert_one(prenda_data)
        return str(resultado.inserted_id)

    @staticmethod
    def actualizar(id, datos_actualizados):
        try:
            resultado = mongo.db.prendas.update_one(
                {"_id": ObjectId(id)},
                {"$set": datos_actualizados}
            )
            return resultado.modified_count > 0
        except:
            return False

    @staticmethod
    def eliminar(id):
        try:
            resultado = mongo.db.prendas.delete_one({"_id": ObjectId(id)})
            return resultado.deleted_count > 0
        except:
            return False


from bson.objectid import ObjectId
from app.index import mongo

class VentaModel:
    @staticmethod
    def obtener_todos():
        ventas_cursor = mongo.db.ventas.find()
        ventas = []
        for venta in ventas_cursor:
            venta["_id"] = str(venta["_id"])
            ventas.append(venta)
        return ventas

    @staticmethod
    def obtener_por_id(id):
        try:
            venta = mongo.db.ventas.find_one({"_id": ObjectId(id)})
            if venta:
                venta["_id"] = str(venta["_id"])
            return venta
        except:
            return None

    @staticmethod
    def crear(venta_data):
        resultado = mongo.db.ventas.insert_one(venta_data)
        return str(resultado.inserted_id)

    @staticmethod
    def actualizar(id, datos_actualizados):
        try:
            resultado = mongo.db.ventas.update_one(
                {"_id": ObjectId(id)},
                {"$set": datos_actualizados}
            )
            return resultado.modified_count > 0
        except:
            return False

    @staticmethod
    def eliminar(id):
        try:
            resultado = mongo.db.ventas.delete_one({"_id": ObjectId(id)})
            return resultado.deleted_count > 0
        except:
            return False

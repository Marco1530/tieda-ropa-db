from bson.objectid import ObjectId
from app.index import mongo

class UsuarioModel:
    @staticmethod
    def obtener_todos():
        usuarios_cursor = mongo.db.usuarios.find()
        usuarios = []
        for usuario in usuarios_cursor:
            usuario["_id"] = str(usuario["_id"])
            usuarios.append(usuario)
        return usuarios

    @staticmethod
    def obtener_por_id(id):
        try:
            usuario = mongo.db.usuarios.find_one({"_id": ObjectId(id)})
            if usuario:
                usuario["_id"] = str(usuario["_id"])
            return usuario
        except:
            return None

    @staticmethod
    def crear(usuario_data):
        resultado = mongo.db.usuarios.insert_one(usuario_data)
        return str(resultado.inserted_id)

    @staticmethod
    def actualizar(id, datos_actualizados):
        try:
            resultado = mongo.db.usuarios.update_one(
                {"_id": ObjectId(id)},
                {"$set": datos_actualizados}
            )
            return resultado.modified_count > 0
        except:
            return False

    @staticmethod
    def eliminar(id):
        try:
            resultado = mongo.db.usuarios.delete_one({"_id": ObjectId(id)})
            return resultado.deleted_count > 0
        except:
            return False

from pymongo import MongoClient

client = MongoClient("mongodb+srv://MarcoAriasArias:MarcoAriasArias15@cluster0.qcupw24.mongodb.net/?retryWrites=true&w=majority")


db = client["TiendaDeRopa"]


prendas_collection = db["prendas"]
usuarios_collection = db["usuarios"]
ventas_collection = db["ventas"]
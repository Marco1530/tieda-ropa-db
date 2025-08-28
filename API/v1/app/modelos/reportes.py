from bson.objectid import ObjectId
from app.index import mongo
from datetime import datetime
from collections import defaultdict

class ReportesModel:

    @staticmethod
    def ventas_por_usuario(id_usuario):
        try:
            ventas_cursor = mongo.db.ventas.find({"usuario_id": ObjectId(id_usuario)})
            ventas = []
            for venta in ventas_cursor:
                venta["_id"] = str(venta["_id"])
                venta["usuario_id"] = str(venta["usuario_id"])
                venta["prenda_id"] = str(venta["prenda_id"])
                if isinstance(venta.get("fecha"), datetime):
                    venta["fecha"] = venta["fecha"].isoformat()
                ventas.append(venta)
            return ventas
        except:
            return None

    @staticmethod
    def total_ventas_por_prenda():
        pipeline = [
            {
                "$group": {
                    "_id": "$prenda_id",
                    "total_vendido": {"$sum": "$cantidad"}
                }
            }
        ]
        resultados = list(mongo.db.ventas.aggregate(pipeline))
        reporte = []
        for r in resultados:
            prenda = mongo.db.prendas.find_one({"_id": ObjectId(r["_id"])})
            if prenda:
                nombre_prenda = prenda.get("nombre", "Desconocida")
                stock = prenda.get("stock", 0)   # 👈 incluimos stock
            else:
                nombre_prenda = "Desconocida"
                stock = 0
            reporte.append({
                "prenda_id": str(r["_id"]),
                "nombre_prenda": nombre_prenda,
                "total_vendido": r["total_vendido"],
                "stock": stock   # 👈 ahora el frontend podrá usarlo
            })
        return reporte

    @staticmethod
    def ventas_por_fecha(fecha_inicio, fecha_fin):
        try:
            fecha_inicio_dt = datetime.fromisoformat(fecha_inicio)
            fecha_fin_dt = datetime.fromisoformat(fecha_fin)
        except:
            return None

        pipeline = [
            {"$match": {"fecha": {"$gte": fecha_inicio_dt, "$lte": fecha_fin_dt}}}
        ]
        ventas_cursor = mongo.db.ventas.aggregate(pipeline)
        ventas = []
        for venta in ventas_cursor:
            venta["_id"] = str(venta["_id"])
            venta["usuario_id"] = str(venta["usuario_id"])
            venta["prenda_id"] = str(venta["prenda_id"])
            if isinstance(venta.get("fecha"), datetime):
                venta["fecha"] = venta["fecha"].isoformat()
            ventas.append(venta)
        return ventas

    # -----------------------------
    # NUEVOS MÉTODOS PARA REPORTES
    # -----------------------------

    @staticmethod
    def marcas_con_ventas():
        ventas_cursor = mongo.db.ventas.find()
        marcas_totales = defaultdict(int)

        for venta in ventas_cursor:
            prenda = mongo.db.prendas.find_one({"_id": ObjectId(venta["prenda_id"])})
            if prenda and "marca" in prenda:
                marcas_totales[prenda["marca"]] += venta.get("cantidad", 0)

        reporte = [{"nombre": marca, "total_ventas": total} for marca, total in marcas_totales.items()]
        return reporte

    @staticmethod
    def top_5_marcas():
        ventas_cursor = mongo.db.ventas.find()
        marcas_totales = defaultdict(int)

        for venta in ventas_cursor:
            prenda = mongo.db.prendas.find_one({"_id": ObjectId(venta["prenda_id"])})
            if prenda and "marca" in prenda:
                marcas_totales[prenda["marca"]] += venta.get("cantidad", 0)

        # Ordenar de mayor a menor y tomar los 5 primeros
        top_5 = sorted(marcas_totales.items(), key=lambda x: x[1], reverse=True)[:5]
        reporte = [{"nombre": marca, "ventas": total} for marca, total in top_5]
        return reporte

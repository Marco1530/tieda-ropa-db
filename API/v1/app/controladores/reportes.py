from flask import Blueprint, request, jsonify
from ..modelos.reportes import ReportesModel

reportes_endpoints = Blueprint('reportes_endpoints', __name__)

# Reporte: ventas de un usuario
@reportes_endpoints.route('/reportes/ventas_usuario', methods=['GET'])
def ventas_usuario():
    id_usuario = request.args.get('usuario_id')
    if not id_usuario:
        return jsonify({"error": "Se requiere el parámetro usuario_id"}), 400

    ventas = ReportesModel.ventas_por_usuario(id_usuario)
    if ventas is None:
        return jsonify({"error": "Error al obtener ventas"}), 500
    return jsonify(ventas), 200

# Reporte: total vendido por prenda
@reportes_endpoints.route('/reportes/total_vendido_prenda', methods=['GET'])
def total_vendido_prenda():
    reporte = ReportesModel.total_ventas_por_prenda()
    return jsonify(reporte), 200

# Reporte: ventas en rango de fechas
@reportes_endpoints.route('/reportes/ventas_por_fecha', methods=['GET'])
def ventas_por_fecha():
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')

    if not fecha_inicio or not fecha_fin:
        return jsonify({"error": "Se requieren los parámetros fecha_inicio y fecha_fin en formato ISO"}), 400

    ventas = ReportesModel.ventas_por_fecha(fecha_inicio, fecha_fin)
    if ventas is None:
        return jsonify({"error": "Fechas en formato inválido"}), 400

    return jsonify(ventas), 200

# NUEVO: Marcas con al menos una venta
@reportes_endpoints.route('/reportes/marcas-ventas', methods=['GET'])
def marcas_ventas():
    reporte = ReportesModel.marcas_con_ventas()
    return jsonify(reporte), 200

# NUEVO: Top 5 marcas más vendidas
@reportes_endpoints.route('/reportes/top-marcas', methods=['GET'])
def top_marcas():
    reporte = ReportesModel.top_5_marcas()
    return jsonify(reporte), 200

from flask import Blueprint
from controllers.reportes_controller import marcas_con_ventas, prendas_vendidas_stock, top_marcas

reportes_bp = Blueprint("reportes", __name__)

reportes_bp.route("/marcas-con-ventas", methods=["GET"])(marcas_con_ventas)
reportes_bp.route("/prendas-vendidas-stock", methods=["GET"])(prendas_vendidas_stock)
reportes_bp.route("/top-marcas", methods=["GET"])(top_marcas)
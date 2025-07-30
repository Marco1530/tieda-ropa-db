from flask import Blueprint
from controllers.ventas_controller import *

ventas_bp = Blueprint("ventas", __name__)

ventas_bp.route("/", methods=["GET"])(get_ventas)
ventas_bp.route("/<id>", methods=["GET"])(get_venta)
ventas_bp.route("/", methods=["POST"])(create_venta)
ventas_bp.route("/<id>", methods=["PUT"])(update_venta)
ventas_bp.route("/<id>", methods=["DELETE"])(delete_venta)
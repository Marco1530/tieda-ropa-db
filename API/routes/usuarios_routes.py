from flask import Blueprint
from controllers.usuarios_controller import *

usuarios_bp = Blueprint("usuarios", __name__)

usuarios_bp.route("/", methods=["GET"])(get_usuarios)
usuarios_bp.route("/<id>", methods=["GET"])(get_usuario)
usuarios_bp.route("/", methods=["POST"])(create_usuario)
usuarios_bp.route("/<id>", methods=["PUT"])(update_usuario)
usuarios_bp.route("/<id>", methods=["DELETE"])(delete_usuario)
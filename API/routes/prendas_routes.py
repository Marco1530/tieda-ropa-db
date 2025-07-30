from flask import Blueprint
from controllers.prendas_controller import *

prendas_bp = Blueprint("prendas", __name__)

prendas_bp.route("/", methods=["GET"])(get_prendas)
prendas_bp.route("/<id>", methods=["GET"])(get_prenda)
prendas_bp.route("/", methods=["POST"])(create_prenda)
prendas_bp.route("/<id>", methods=["PUT"])(update_prenda)
prendas_bp.route("/<id>", methods=["DELETE"])(delete_prenda)
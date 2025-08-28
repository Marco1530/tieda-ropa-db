from flask import Blueprint, request, jsonify
from ..modelos.usuarios import UsuarioModel

usuarios_endpoints = Blueprint('usuarios_endpoints', __name__)

@usuarios_endpoints.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    id_usuario = request.args.get('id')

    if id_usuario:
        usuario = UsuarioModel.obtener_por_id(id_usuario)
        if usuario:
            return jsonify(usuario), 200
        return jsonify({"error": "Usuario no encontrado"}), 404

    usuarios = UsuarioModel.obtener_todos()
    return jsonify(usuarios), 200

@usuarios_endpoints.route('/usuarios', methods=['POST'])
def crear_usuario():
    usuario_data = request.json
    usuario_id = UsuarioModel.crear(usuario_data)
    return jsonify({"mensaje": "Usuario creado", "id": usuario_id}), 201

@usuarios_endpoints.route('/usuarios', methods=['PUT'])
def actualizar_usuario():
    id_usuario = request.args.get('id')
    datos_actualizados = request.json

    if UsuarioModel.actualizar(id_usuario, datos_actualizados):
        return jsonify({"mensaje": "Usuario actualizado"}), 200
    return jsonify({"error": "No se pudo actualizar el usuario"}), 400

@usuarios_endpoints.route('/usuarios', methods=['DELETE'])
def eliminar_usuario():
    id_usuario = request.args.get('id')

    if UsuarioModel.eliminar(id_usuario):
        return jsonify({"mensaje": "Usuario eliminado"}), 200
    return jsonify({"error": "No se pudo eliminar el usuario"}), 400

def serialize_usuario(usuario):
    return {
        "id": str(usuario.get("_id")),
        "nombre": usuario.get("nombre"),
        "correo": usuario.get("correo"),
        "telefono": usuario.get("telefono")
    }
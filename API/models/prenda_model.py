def serialize_prenda(prenda):
    return {
        "id": str(prenda.get("_id")),
        "nombre": prenda.get("nombre"),
        "marca": prenda.get("marca"),
        "precio": prenda.get("precio"),
        "stock": prenda.get("stock")
    }
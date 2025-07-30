def serialize_venta(venta):
    return {
        "id": str(venta.get("_id")),
        "usuario_id": str(venta.get("usuario_id")),
        "prenda_id": str(venta.get("prenda_id")),
        "fecha": venta.get("fecha"),
        "cantidad": venta.get("cantidad")
    }
Endpoints: Prendas

1. Obtener todas las prendas

Método: GET

Endpoint: http://127.0.0.1:5000/api/prendas

Descripción: Devuelve una lista con todas las prendas registradas.

Ejemplo de respuesta:

[
  {
    "nombre": "Gorra Casual",
    "marca": "UrbanStyle",
    "precio": 8000,
    "stock": 50
  },
  ...
]

2. Obtener una prenda por ID

Método: GET

Endpoint: http://127.0.0.1:5000/api/prendas/<id>

Descripción: Devuelve los detalles de una prenda específica.

Ejemplo de respuesta:

{
  "nombre": "Sudadera Eco",
  "marca": "EcoTrend",
  "precio": 22000,
  "stock": 25
}

3. Insertar una nueva prenda

Método: POST

Endpoint: http://127.0.0.1:5000/api/prendas

Descripción: Agrega una nueva prenda a la base de datos.

Cuerpo JSON:

{
  "nombre": "Nueva Prenda",
  "marca": "Marca X",
  "precio": 10000,
  "stock": 15
}

Respuesta:

{ "mensaje": "Prenda insertada exitosamente" }

4. Actualizar prenda por ID

Método: PUT

Endpoint: http://127.0.0.1:5000/api/prendas/<id>

Descripción: Actualiza la información de una prenda.

Cuerpo JSON:

{
  "nombre": "Gorra Premium",
  "marca": "UrbanStyle",
  "precio": 8500,
  "stock": 40
}

Respuesta:

{ "mensaje": "Prenda actualizada exitosamente" }

5. Eliminar prenda por ID

Método: DELETE

Endpoint: http://127.0.0.1:5000/api/prendas/<id>

Descripción: Elimina una prenda del sistema.

Respuesta:

{ "mensaje": "Prenda eliminada exitosamente" }

Endpoints: Usuarios

1. Obtener todos los usuarios

Método: GET

Endpoint: http://127.0.0.1:5000/api/usuarios

2. Obtener usuario por ID

Método: GET

Endpoint: http://127.0.0.1:5000/api/usuarios/<id>

3. Insertar nuevo usuario

Método: POST

Endpoint: http://127.0.0.1:5000/api/usuarios

JSON:

{
  "nombre": "Nuevo Usuario",
  "correo": "nuevo@email.com",
  "telefono": "8888-0000"
}

4. Actualizar usuario por ID

Método: PUT

Endpoint: http://127.0.0.1:5000/api/usuarios/<id>

5. Eliminar usuario por ID

Método: DELETE

Endpoint: http://127.0.0.1:5000/api/usuarios/<id>

Endpoints: Ventas

1. Obtener todas las ventas

Método: GET

Endpoint: http://127.0.0.1:5000/api/ventas

2. Obtener venta por ID

Método: GET

Endpoint: http://127.0.0.1:5000/api/ventas/<id>

3. Insertar nueva venta

Método: POST

Endpoint: http://127.0.0.1:5000/api/ventas

JSON:

{
  "usuario_id": "<id_usuario>",
  "prenda_id": "<id_prenda>",
  "fecha": "2025-07-01",
  "cantidad": 2
}

4. Eliminar venta por ID

Método: DELETE

Endpoint: http://127.0.0.1:5000/api/ventas/<id>
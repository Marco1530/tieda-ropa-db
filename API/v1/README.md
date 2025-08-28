Base URL

http://127.0.0.1:5000/admin2/api/v1

GET


Obtener todas las prendas

GET http://127.0.0.1:5000/admin2/api/v1/prendas

Obtener una prenda por ID

GET http://127.0.0.1:5000/admin2/api/v1/prendas?id=6662b613d2e627276b6e7c05


POST

Crear una nueva prenda

POST /prendas
Content-Type: application/json

{
  "nombre": "Gorra Casual",
  "marca": "UrbanStyle",
  "precio": 8000,
  "stock": 50
}


PUT

Actualizar una prenda existente

PUT /prendas?id=6662b613d2e627276b6e7c05
Content-Type: application/json

{
  "nombre": "Gorra Casual Premium",
  "marca": "UrbanStyle",
  "precio": 8500,
  "stock": 40
}


DELETE

Eliminar una prenda por ID

DELETE /prendas?id=6662b613d2e627276b6e7c05


REPORTES

GET /reportes/total_vendido_prenda

[
  {
    "prenda_id": "6662b613d2e627276b6e7c05",
    "nombre_prenda": "Gorra Casual",
    "total_vendido": 12
  }
]
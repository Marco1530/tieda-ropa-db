// Seleccionar o crear la base de datos
use tiendaRopa;

// Inserts 

db.usuarios.insertOne({
  nombre: "Laura Jiménez",
  correo: "laura@email.com",
  telefono: "8888-1234"
});


db.usuarios.insertMany([ //esta se usa para insertar varios el Many
  { nombre: "Carlos Mora", correo: "carlos@email.com", telefono: "8555-4321" },
  { nombre: "Ana Pérez", correo: "ana@email.com", telefono: "8666-7890" }
]);


db.marcas.insertMany([
  { nombre: "UrbanStyle", pais: "Costa Rica" },
  { nombre: "ClassicFit", pais: "EEUU" },
  { nombre: "EcoTrend", pais: "México" }
]);

db.prendas.insertMany([
  { nombre: "Camiseta Oversize", marca: "UrbanStyle", precio: 12000, stock: 30 },
  { nombre: "Pantalón Slim", marca: "ClassicFit", precio: 18000, stock: 20 }
]);


db.ventas.insertMany([
  {
    usuario_id: ObjectId("665f2e421111111111111111"),
    prenda_id: ObjectId("665f2e421222222222222222"),
    fecha: ISODate("2025-06-15"),
    cantidad: 2
  },
  {
    usuario_id: ObjectId("665f2e421111111111111111"),
    prenda_id: ObjectId("665f2e421333333333333333"),
    fecha: ISODate("2025-06-16"),
    cantidad: 1
  }
]);

// Actualizar
db.usuarios.updateOne(
  { nombre: "Laura Jiménez" },
  { $set: { telefono: "8999-0000" } }
);

db.marcas.updateOne(
  { nombre: "ClassicFit" },
  { $set: { pais: "Estados Unidos" } }
);

db.prendas.updateOne(
  { nombre: "Camiseta Oversize" },
  { $inc: { stock: -2 } }
);

// Eliminar
db.usuarios.deleteOne({ nombre: "Ana Pérez" });
db.marcas.deleteOne({ nombre: "EcoTrend" });
db.prendas.deleteOne({ nombre: "Pantalón Slim" });

// Consultas

// COnsulta la cantidad vendida por fecha y filtrada con fecha
db.ventas.aggregate([
  { $match: { fecha: ISODate("2025-06-15") } },
  { $group: { _id: "$fecha", totalVendidas: { $sum: "$cantidad" } } }
]);

// Las que tienen al menos una venta
db.ventas.aggregate([
  {
    $lookup: {
      from: "prendas",
      localField: "prenda_id",
      foreignField: "_id",
      as: "info_prenda"
    }
  },
  { $unwind: "$info_prenda" },
  { $group: { _id: "$info_prenda.marca" } }
]);

// Muestra lo que se ha vendido y su cantidad en stock
db.prendas.aggregate([
  {
    $lookup: {
      from: "ventas",
      localField: "_id",
      foreignField: "prenda_id",
      as: "ventas"
    }
  },
  {
    $project: {
      nombre: 1,
      stock: 1,
      totalVendidas: { $sum: "$ventas.cantidad" }
    }
  }
]);

// Obtiene las mas vendidas y la cantidad de estas 
db.ventas.aggregate([
  {
    $lookup: {
      from: "prendas",
      localField: "prenda_id",
      foreignField: "_id",
      as: "info_prenda"
    }
  },
  { $unwind: "$info_prenda" },
  {
    $group: {
      _id: "$info_prenda.marca",
      totalVentas: { $sum: "$cantidad" }
    }
  },
  { $sort: { totalVentas: -1 } },
  { $limit: 5 }
]);
